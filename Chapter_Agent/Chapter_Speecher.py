import os
import json
import argparse
import sys

# 添加根目录到Python路径，以便导入根目录的api_call
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_call import process_text_with_images


def load_config(config_path: str = None) -> dict:
    """
    加载配置文件
    """
    if config_path is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)  # 上一级目录（根目录）
        config_path = os.path.join(parent_dir, "config.json")
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        raise Exception(f"加载配置文件失败: {str(e)}")

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

def load_python_content(python_path: str) -> str:
    """
    加载 Python 文件内容
    """
    try:
        with open(python_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception as e:
        raise Exception(f"加载 Python 文件失败: {str(e)}")

def load_previous_speech(speech_path: str) -> str:
    """
    加载上一个页面的讲稿内容
    """
    try:
        with open(speech_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception as e:
        raise Exception(f"加载上一个页面的讲稿失败: {str(e)}")

def save_result(result: str, markdown_path: str, python_path: str, model: str, output_dir: str = None) -> str:
    """
    保存处理结果到演讲稿文件
    """
    try:
        # 如果没有指定输出目录，使用默认目录
        if output_dir is None:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            output_dir = os.path.join(current_dir, "MASLab_generated_speech")
        
        # 创建输出目录（如果不存在）
        os.makedirs(output_dir, exist_ok=True)
        
        # 获取markdown文件名（不含扩展名）作为基础名
        base_name = os.path.splitext(os.path.basename(markdown_path))[0]
        
        # 构建输出文件路径
        output_file = os.path.join(output_dir, f"{base_name}_speech.txt")
        
        # 直接保存模型生成的结果
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)
            
        return output_file
    except Exception as e:
        raise Exception(f"保存演讲稿到文件失败: {str(e)}")

def process_content_to_speech(markdown_path: str, python_path: str, previous_speech_path: str, prompt_template_path: str, api_key: str, model: str = "gpt-4.5-preview", output_dir: str = None) -> str:
    """
    处理 Markdown 和 Python 文件内容并生成演讲稿
    1. 加载提示词模板
    2. 加载 Markdown 内容
    3. 加载 Python 代码
    4. 加载上一个页面的讲稿
    5. 组合提示词和内容
    6. 调用 API 处理
    7. 保存演讲稿到文件
    """
    try:
        # 加载提示词模板
        prompt = load_prompt_template(prompt_template_path)
        
        # 加载 Markdown 内容
        content = load_markdown_content(markdown_path)
        
        # 加载 Python 代码内容
        code_content = load_python_content(python_path)
        
        # 加载上一个页面的讲稿内容
        previous_speech = load_previous_speech(previous_speech_path)
        
        # 组合提示词和内容
        combined_text = f"{prompt}\n\n上一个页面的讲稿内容如下：\n\n{previous_speech}\n\n论文原文的内容如下：\n\n{content}\n\n其对应的manim脚本内容如下：\n\n{code_content}"
        
        # 获取markdown文件所在目录作为图片路径基准
        markdown_dir = os.path.dirname(os.path.abspath(markdown_path))
        
        # 调用 API 处理文本，传递正确的base_path
        result = process_text_with_images(combined_text, api_key, model, base_path=markdown_dir)
        
        # 保存结果到文件
        output_file = save_result(result, markdown_path, python_path, model, output_dir)
        
        return result, output_file
    
    except Exception as e:
        raise Exception(f"处理文件生成演讲稿失败: {str(e)}")

def main():
    """
    主函数，用于测试
    """
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='将Markdown和Python文件转换为演讲稿')
    parser.add_argument('markdown_path', help='输入的Markdown文件路径')
    parser.add_argument('python_path', help='输入的Python文件路径')
    parser.add_argument('previous_speech_path', nargs='?', help='上一个页面的讲稿txt文件路径（可选）')
    parser.add_argument('output_dir', nargs='?', help='演讲稿输出目录路径（可选）')
    parser.add_argument('--prompt-template', help='提示词模板路径', default=None)
    
    args = parser.parse_args()
    
    # 设置提示词模板路径
    if args.prompt_template is None:
        # 使用默认路径（从上一级目录的prompt_template读取）
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)  # 上一级目录（根目录）
        prompt_template_path = os.path.join(parent_dir, "prompt_template", "Method_Speecher.txt")
    else:
        prompt_template_path = args.prompt_template
    
    # 如果没有提供上一个页面的讲稿路径，使用默认文件（从上一级目录读取）
    if args.previous_speech_path is None:
        previous_speech_path = os.path.join(parent_dir, "prompt_template", "Speecher-1.txt")
        print(f"未提供上一个页面的讲稿文件，使用默认文件: {previous_speech_path}")
    else:
        previous_speech_path = args.previous_speech_path
    
    # 输出目录（可选）
    output_dir = args.output_dir
    if output_dir:
        print(f"使用指定的输出目录: {output_dir}")
    else:
        print(f"使用默认输出目录: MASLab_generated_speech")
    
    # 从配置文件加载API key和model
    config = load_config()
    api_key = config['api_key']
    model = config['model']
    
    try:
        # 处理文件
        result, output_file = process_content_to_speech(args.markdown_path, args.python_path, previous_speech_path, prompt_template_path, api_key, model, output_dir=output_dir)
        print("生成的演讲稿：")
        print(result)
        print(f"\n演讲稿已保存到文件：{output_file}")
    except Exception as e:
        print(f"错误：{str(e)}")

if __name__ == "__main__":
    main() 