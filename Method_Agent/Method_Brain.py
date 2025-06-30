import os
import argparse
from api_call import process_text


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

def save_result(result: str, markdown_path: str, model: str, output_dir: str) -> str:
    """
    保存处理结果到文件
    """
    try:
        # 创建输出目录（如果不存在）
        os.makedirs(output_dir, exist_ok=True)
        
        # 获取 markdown 文件名（不含扩展名）
        markdown_name = os.path.splitext(os.path.basename(markdown_path))[0]
        
        # 构建输出文件路径
        output_file = os.path.join(output_dir, f"{markdown_name}_split.md")
        
        # 保存结果到文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)
            
        return output_file
    except Exception as e:
        raise Exception(f"保存结果到文件失败: {str(e)}")

def process_markdown_with_prompt(markdown_path: str, prompt_template_path: str, api_key: str, output_dir: str, model: str = "gpt-4.5-preview-2025-02-27") -> str:
    """
    处理 Markdown 文件内容
    1. 加载提示词模板
    2. 加载 Markdown 内容
    3. 组合提示词和内容
    4. 调用 API 处理
    5. 保存结果到文件
    """
    try:
        # 加载提示词模板
        prompt = load_prompt_template(prompt_template_path)
        
        # 加载 Markdown 内容
        content = load_markdown_content(markdown_path)
        
        # 组合提示词和内容
        combined_text = f"{prompt}\n\n以下是需要划分的文本：\n\n{content}"
        
        # 调用 API 处理文本
        result = process_text(combined_text, api_key, model)
        
        # 保存结果到文件
        output_file = save_result(result, markdown_path, model, output_dir)
        
        return result, output_file
    
    except Exception as e:
        raise Exception(f"处理 Markdown 文件失败: {str(e)}")

def main():
    """
    主函数，处理命令行参数
    """
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='使用AI智能分割Markdown文件为逻辑页面')
    parser.add_argument('input_file', help='输入的Markdown文件路径')
    parser.add_argument('output_dir', help='输出目录路径')
    
    args = parser.parse_args()
    
    # 检查输入文件是否存在
    if not os.path.exists(args.input_file):
        print(f"❌ 错误：输入文件 '{args.input_file}' 不存在")
        return
    
    # 设置固定的提示词模板路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    prompt_template_path = os.path.join(current_dir, "prompt_templates", "Brain.txt")
    
    # 检查提示词模板是否存在
    if not os.path.exists(prompt_template_path):
        print(f"❌ 错误：提示词模板文件 '{prompt_template_path}' 不存在")
        return
    
    print(f"📄 输入文件: {args.input_file}")
    print(f"📁 输出目录: {args.output_dir}")
    print(f"🧠 提示词模板: prompt_templates/Brain.txt")
    print("🔄 开始AI智能分割...")
    
    api_key = ''
    
    try:
        # 处理文件
        result, output_file = process_markdown_with_prompt(args.input_file, prompt_template_path, api_key, args.output_dir)
        print("\n✅ 分割完成！")
        print("📝 处理结果预览：")
        print("-" * 50)
        print(result[:500] + "..." if len(result) > 500 else result)
        print("-" * 50)
        print(f"\n✨ 分割结果已保存到: {output_file}")
    except Exception as e:
        print(f"❌ 分割失败: {str(e)}")

if __name__ == "__main__":
    main() 