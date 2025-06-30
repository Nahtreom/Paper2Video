import base64
import time
import http.client
import json
import socket
import ssl
import re
import os
from typing import List, Dict, Any, Union, Tuple
from PIL import Image

# 常量定义
MAX_RETRIES = 3
TIMEOUT = 1200
API_HOSTNAME = "api2.aigcbest.top"
API_PATH = "/v1/chat/completions"

class APIClient:
    def __init__(self, api_key: str, model: str = "gpt-4o"):
        self.api_key = api_key
        self.model = model
    
    def encode_image(self, image_path: str) -> str:
        """将图片编码为base64格式"""
        try:
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        except Exception as e:
            raise Exception(f"图片编码失败: {str(e)}")
    
    def extract_images_from_text(self, text: str) -> List[str]:
        """从文本中提取图片路径，格式为 ![](xx/xxx.jpg)，但忽略被引号包裹的情况"""
        # 先找出所有的图片引用
        pattern = r"!\[\]\((.+?)\)"
        matches = []
        
        # 对每个匹配项，检查它是否被引号包裹
        for match in re.finditer(pattern, text):
            start = match.start()
            end = match.end()
            
            # 检查这个匹配是否被引号包裹
            # 向前找最近的引号
            prev_quote = text.rfind("'", 0, start)
            prev_quote2 = text.rfind("`", 0, start)
            prev_quote = max(prev_quote, prev_quote2)
            
            # 向后找最近的引号
            next_quote = text.find("'", end)
            next_quote2 = text.find("`", end)
            if next_quote == -1:
                next_quote = len(text)
            if next_quote2 == -1:
                next_quote2 = len(text)
            next_quote = min(next_quote, next_quote2)
            
            # 如果这个图片引用不在引号内，就添加到结果中
            if prev_quote == -1 or next_quote == -1 or not (prev_quote < start and end < next_quote):
                matches.append(match.group(1))
                
        return matches
    
    def get_image_size(self, image_path: str) -> Tuple[int, int]:
        """获取图片的尺寸 (width, height)"""
        with Image.open(image_path) as img:
            return img.width, img.height
    
    def get_mime_type(self, file_path: str) -> str:
        """根据文件扩展名获取MIME类型"""
        ext = os.path.splitext(file_path)[1].lower()
        mime_types = {
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.png': 'image/png',
            '.gif': 'image/gif',
            '.webp': 'image/webp',
            '.bmp': 'image/bmp',
            '.svg': 'image/svg+xml'
        }
        return mime_types.get(ext, 'application/octet-stream')
    
    def resolve_image_path(self, img_path: str, base_path: str = None) -> str:
        """
        解析图片路径，将相对路径转换为基于base_path的绝对路径
        
        Args:
            img_path: 原始图片路径
            base_path: 基准路径（通常是markdown文件所在目录）
        
        Returns:
            解析后的图片路径
        """
        if os.path.isabs(img_path):
            # 如果已经是绝对路径，直接返回
            return img_path
        
        if base_path:
            # 如果提供了base_path，相对于base_path解析
            resolved_path = os.path.join(base_path, img_path)
            return os.path.abspath(resolved_path)
        else:
            # 如果没有base_path，相对于当前工作目录
            return os.path.abspath(img_path)

    def call_api_with_text_and_images(self, text: str, base_path: str = None) -> str:
        """
        处理文本中的图片引用并调用API
        
        Args:
            text: 要处理的文本
            base_path: 图片路径的基准目录（通常是markdown文件所在目录）
        """
        # 提取图片路径
        image_paths = self.extract_images_from_text(text)
    
        modified_text = text
        offset = 0  # 由于插入新字符，原始索引会发生偏移

        for match in re.finditer(r"!\[\]\((.+?)\)", text):
            img_path = match.group(1)
            try:
                # 解析图片路径
                resolved_img_path = self.resolve_image_path(img_path, base_path)
                width, height = self.get_image_size(resolved_img_path)
                size_str = f"（尺寸：{width}×{height}）"
                insert_pos = match.end() + offset
                modified_text = modified_text[:insert_pos] + size_str + modified_text[insert_pos:]
                offset += len(size_str)  # 更新偏移量
            except Exception as e:
                print(f"读取图片尺寸失败 {img_path}: {e}")

        # 准备消息内容
        content = []
        
        # 保留原始文本中的图片引用
        content.append({"type": "text", "text": modified_text})

        # 添加图片内容
        for img_path in image_paths:
            try:
                # 解析图片路径
                resolved_img_path = self.resolve_image_path(img_path, base_path)
                base64_image = self.encode_image(resolved_img_path)
                mime_type = self.get_mime_type(resolved_img_path)
                image_data_url = f"data:{mime_type};base64,{base64_image}"
                
                content.append({
                    "type": "image_url",
                    "image_url": {
                        "url": image_data_url
                    }
                })
            except Exception as e:
                print(f"处理图片 {img_path} 时出错: {str(e)}")
        
        # 构建API请求payload
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": content
                }
            ],
            "temperature": 1
        }
        
        # 调用API
        return self._call_api(payload)
    
    def call_api_with_text(self, text: str) -> str:
        """简单的纯文本API调用，不处理图片"""
        # 构建API请求payload
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": text
                        }
                    ]
                }
            ],
            "temperature": 1
        }
        
        # 调用API
        return self._call_api(payload)
    
    def _call_api(self, payload: Dict[str, Any]) -> str:
        """发送API请求并处理响应"""
        payload_str = json.dumps(payload)
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        retry_count = 0
        response_content = None

        while retry_count < MAX_RETRIES:
            try:
                conn = http.client.HTTPSConnection(API_HOSTNAME, timeout=TIMEOUT)
                conn.request("POST", API_PATH, payload_str, headers)
                res = conn.getresponse()

                if res.status == 200:
                    data = res.read()
                    response_data = json.loads(data.decode("utf-8"))
                    if response_data.get("choices") and response_data["choices"][0].get("message"):
                        response_content = response_data["choices"][0]["message"].get("content")
                    else:
                        response_content = f"错误：响应中未找到预期的'content'。响应: {response_data}"
                    break  # 成功，跳出重试循环
                else:
                    error_data = res.read().decode('utf-8')
                    print(f"API请求失败，状态码: {res.status} {res.reason}, 错误信息: {error_data}")
                    if 500 <= res.status < 600:  # 服务器端错误，可以尝试重试
                        raise Exception(f"服务器错误: {res.status} {res.reason}, 详情: {error_data}")
                    else:  # 客户端错误 (4xx) 通常不可重试
                        response_content = f"API错误: {res.status} {res.reason}, 详情: {error_data}"
                        break

            except (socket.timeout, ssl.SSLError, ConnectionResetError, ConnectionRefusedError, 
                   http.client.RemoteDisconnected, http.client.NotConnected, 
                   http.client.CannotSendRequest, http.client.ResponseNotReady) as e:
                retry_count += 1
                print(f"网络或连接错误 (尝试 {retry_count}/{MAX_RETRIES}): {e}")
                if retry_count >= MAX_RETRIES:
                    response_content = f"错误：达到最大重试次数后连接失败。最后错误: {e}"
                    break
                print(f"等待 {5 * retry_count} 秒后重试...")  # 简单的退避策略
                time.sleep(5 * retry_count)
            except json.JSONDecodeError as e:
                response_content = f"错误：无法解析API响应为JSON。错误: {e}, 响应内容: {data.decode('utf-8') if 'data' in locals() else 'N/A'}"
                print(response_content)
                break  # JSON解析错误通常不可重试
            except Exception as e:
                print(f"发生未知错误: {e}")
                response_content = f"错误：发生未知错误。{e}"
                break  # 其他未知错误，停止
            finally:
                if 'conn' in locals() and conn:
                    conn.close()

        return response_content if response_content else "未能获取模型响应"


def process_text_with_images(text: str, api_key: str, model: str = "gpt-4o", base_path: str = None) -> str:
    """
    处理包含图片的文本
    
    Args:
        text: 要处理的文本
        api_key: API密钥
        model: 使用的模型
        base_path: 图片路径的基准目录（通常是markdown文件所在目录）
    """
    client = APIClient(api_key=api_key, model=model)
    return client.call_api_with_text_and_images(text, base_path)

def process_text(text: str, api_key: str, model: str = "gpt-4o") -> str:
    """简单的纯文本处理函数"""
    client = APIClient(api_key=api_key, model=model)
    return client.call_api_with_text(text)


if __name__ == "__main__":
    key = ''
    
    text_result = process_text_with_images("![](test.jpg)", key)
    print("", text_result)
    
