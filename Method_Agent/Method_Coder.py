import os
from api_call import process_text_with_images
import argparse


def load_prompt_template(template_path: str) -> str:
    """
    加载提示词模板
    """
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception as e:
        raise Exception(f"加载提示词模板失败: {str(e)}")

def load_markdown_content(markdown_path: str) -> str:
    """
    加载 Markdown 文件内容
    """
    try:
        with open(markdown_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception as e:
        raise Exception(f"加载 Markdown 文件失败: {str(e)}")

def clean_code_result(result: str) -> str:
    """
    清理模型返回的结果，确保是可执行的Python代码
    """
    # 处理可能的转义字符

    print(result)
    if result.startswith('\\n'):
        result = result[2:]
    elif result.startswith('n'):
        result = result[1:]
        
    # 如果代码被markdown代码块包裹，去除它
    if result.startswith("```python"):
        result = result[8:]
    elif result.startswith("```"):
        result = result[3:]
    if result.endswith("```"):
        result = result[:-3]
    
    result = result.strip()
    
    if "```" in result:
        result = result.split("```")[0].strip()
    
    lines = result.split('\n')
    clean_lines = []
    started = False
    
    for line in lines:
        if not started and any(x in line.lower() for x in ["这是", "以下是", "python代码", "代码实现", "实现代码"]):
            continue
        if line.strip() and not line.startswith('#'):
            started = True
        if started:
            clean_lines.append(line)
    
    result = '\n'.join(clean_lines)
    
    # 最后再次检查并清理开头的转义字符
    if result.startswith('\\n'):
        result = result[2:]
    elif result.startswith('n'):
        result = result[1:]
    
    return result.strip()

def save_result(result: str, markdown_path: str, model: str, output_dir: str = None) -> str:
    """
    保存处理结果到Python文件
    Args:
        result: 要保存的代码结果
        markdown_path: markdown文件路径
        model: 使用的模型名称
        output_dir: 输出目录路径，如果为None则使用默认的generated_code目录
    """
    try:
        # 创建输出目录（如果不存在）
        current_dir = os.path.dirname(os.path.abspath(__file__))
        if output_dir is None:
            output_dir = os.path.join(current_dir, "generated_code")
        os.makedirs(output_dir, exist_ok=True)
        
        # 获取markdown文件名（不含扩展名）作为基础名
        base_name = os.path.splitext(os.path.basename(markdown_path))[0]
        
        # 构建输出文件路径（使用.py扩展名）
        output_file = os.path.join(output_dir, f"{base_name}_code.py")
        
        # 直接保存代码
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)
            
        return output_file
    except Exception as e:
        raise Exception(f"保存代码到文件失败: {str(e)}")

def process_markdown_to_code(markdown_path: str, prompt_template_path: str, api_key: str, model: str = "gpt-4.5-preview-2025-02-27", output_dir: str = None) -> str:
    """
    处理 Markdown 文件内容并生成对应的Python代码
    1. 加载提示词模板
    2. 加载 Markdown 内容
    3. 组合提示词和内容
    4. 调用 API 处理
    5. 清理代码结果
    6. 保存代码到文件
    
    Args:
        markdown_path: markdown文件路径
        prompt_template_path: 提示词模板路径
        api_key: API密钥
        model: 使用的模型名称
        output_dir: 输出目录路径
    """
    try:
        # 加载提示词模板
        prompt = load_prompt_template(prompt_template_path)
        
        # 加载 Markdown 内容
        content = load_markdown_content(markdown_path)
        
        # 组合提示词和内容
        combined_text = f"{prompt}\n\n以下是需要转换为代码的文本：\n\n{content}"
        
        # 获取markdown文件所在目录作为图片路径基准
        markdown_dir = os.path.dirname(os.path.abspath(markdown_path))
        
        # 调用 API 处理文本，传递正确的base_path
        result = process_text_with_images(combined_text, api_key, model, base_path=markdown_dir)
        
        # 清理代码结果
        clean_result = clean_code_result(result)
        
        # 保存结果到文件
        output_file = save_result(clean_result, markdown_path, model, output_dir)
        
        return clean_result, output_file
    
    except Exception as e:
        raise Exception(f"处理 Markdown 文件生成代码失败: {str(e)}")

def main():
    """
    主函数，用于测试
    """
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='将Markdown文件转换为Python代码')
    parser.add_argument('markdown_path', help='输入的Markdown文件路径')
    parser.add_argument('--output-dir', help='输出目录路径', default=None)
    args = parser.parse_args()
    
    # 设置文件路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    prompt_template_path = os.path.join(current_dir, "prompt_templates", "Coder.txt")
    api_key = ''
    
    try:
        # 处理文件
        result, output_file = process_markdown_to_code(args.markdown_path, prompt_template_path, api_key, output_dir=args.output_dir)
        print(f"\n代码已保存到文件：{output_file}")
    except Exception as e:
        print(f"错误：{str(e)}")

if __name__ == "__main__":
    main() 