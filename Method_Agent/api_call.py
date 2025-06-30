import base64
import time
from openai import OpenAI
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

class APIClient:
    def __init__(self, api_key: str, model: str = "gpt-4o"):
        self.api_key = api_key
        self.model = model
        # 初始化 OpenAI 客户端
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://yeysai.com/v1/",
        )
    
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
        
        # 调用API
        return self._call_api(content)
    
    def call_api_with_text(self, text: str) -> str:
        """简单的纯文本API调用，不处理图片"""
        content = [
            {
                "type": "text",
                "text": text
            }
        ]
        
        # 调用API
        return self._call_api(content)
    
    def _call_api(self, content: List[Dict[str, Any]]) -> str:
        """发送API请求并处理响应"""
        retry_count = 0
        response_content = None

        while retry_count < MAX_RETRIES:
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "user",
                            "content": content
                        }
                    ],
                    max_tokens=1000,
                    temperature=1
                )
                
                if response.choices and response.choices[0].message:
                    response_content = response.choices[0].message.content
                else:
                    response_content = f"错误：响应中未找到预期的'content'。响应: {response}"
                break  # 成功，跳出重试循环

            except Exception as e:
                retry_count += 1
                print(f"API调用错误 (尝试 {retry_count}/{MAX_RETRIES}): {e}")
                if retry_count >= MAX_RETRIES:
                    response_content = f"错误：达到最大重试次数后API调用失败。最后错误: {e}"
                    break
                print(f"等待 {5 * retry_count} 秒后重试...")  # 简单的退避策略
                time.sleep(5 * retry_count)

        return response_content if response_content else "未能获取模型响应"


def process_text_with_images(text: str, api_key: str, model: str = "gpt-4.5-preview", base_path: str = None) -> str:
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

def process_text(text: str, api_key: str, model: str = "gpt-4.5-preview") -> str:
    """简单的纯文本处理函数"""
    client = APIClient(api_key=api_key, model=model)
    return client.call_api_with_text(text)


