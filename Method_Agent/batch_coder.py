import os
import sys
import glob
import subprocess
import re
from datetime import datetime

def print_separator(char="=", length=50):
    """打印分隔线"""
    print(char * length)

def format_time():
    """返回格式化的当前时间"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def process_markdown_folder(input_folder: str, output_dir: str):
    """
    处理指定文件夹下的所有markdown文件
    
    Args:
        input_folder: 输入文件夹路径
        output_dir: 输出目录路径
    """
    print_separator()
    print(f"[{format_time()}] 开始批量处理任务")
    print(f"输入文件夹: {input_folder}")
    print(f"输出目录: {output_dir}")
    
    # 获取输入文件夹的绝对路径
    input_folder = os.path.abspath(input_folder)
    output_dir = os.path.abspath(output_dir)
    
    # 确保输入文件夹存在
    if not os.path.exists(input_folder):
        print(f"\n❌ 错误：输入文件夹 '{input_folder}' 不存在")
        return
    
    # 创建输出目录（如果不存在）
    os.makedirs(output_dir, exist_ok=True)
    print(f"📁 输出目录已准备: {output_dir}")
    
    # 获取所有markdown文件
    markdown_files = []
    for ext in ['*.md', '*.markdown']:
        markdown_files.extend(glob.glob(os.path.join(input_folder, '**', ext), recursive=True))
    
    if not markdown_files:
        print(f"\n⚠️  警告：在文件夹 '{input_folder}' 中没有找到markdown文件")
        return
    
    # 对文件进行排序
    def get_sort_key(file_path):
        # 获取文件名（不含路径和扩展名）
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        # 提取所有数字序列
        numbers = re.findall(r'\d+', base_name)
        # 如果找到数字，将其转换为整数列表；如果没有数字，返回空列表
        return [int(num) for num in numbers] if numbers else []
    
    # 按数字序列排序
    markdown_files.sort(key=get_sort_key)
    
    total_files = len(markdown_files)
    print(f"\n📝 找到 {total_files} 个markdown文件待处理")
    print("\n📋 处理顺序：")
    for i, file in enumerate(markdown_files, 1):
        relative_path = os.path.relpath(file, input_folder)
        print(f"   {i}. {relative_path}")
    print_separator("-")
    
    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    method_coder_path = os.path.join(current_dir, 'Method_Coder.py')
    
    # 处理统计
    success_count = 0
    failed_files = []
    
    # 处理每个markdown文件
    for index, markdown_file in enumerate(markdown_files, 1):
        relative_path = os.path.relpath(markdown_file, input_folder)
        print(f"\n[{format_time()}] 处理文件 ({index}/{total_files}): {relative_path}")
        
        try:
            subprocess.run([
                sys.executable,
                method_coder_path,
                markdown_file,
                '--output-dir', output_dir
            ], check=True)
            success_count += 1
            print(f"✅ 成功处理文件: {relative_path}")
            
        except subprocess.CalledProcessError as e:
            failed_files.append(relative_path)
            print(f"❌ 处理失败: {relative_path}")
            print(f"   错误信息: {str(e)}")
            continue
            
        # 显示进度
        progress = (index / total_files) * 100
        print(f"进度: [{index}/{total_files}] {progress:.1f}%")
        print_separator("-")
    
    # 打印总结报告
    print_separator()
    print(f"\n📊 处理完成！总结报告:")
    print(f"总文件数: {total_files}")
    print(f"成功处理: {success_count}")
    print(f"处理失败: {len(failed_files)}")
    
    if failed_files:
        print("\n❌ 以下文件处理失败:")
        for file in failed_files:
            print(f"   - {file}")
    
    print(f"\n✨ 生成的代码已保存到: {os.path.relpath(output_dir, os.getcwd())}")
    print_separator()

def main():
    """
    主函数
    """
    import argparse
    
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='批量处理文件夹中的markdown文件')
    parser.add_argument('input_folder', help='包含markdown文件的输入文件夹路径')
    parser.add_argument('output_dir', help='代码输出目录路径')
    
    args = parser.parse_args()
    
    # 处理文件夹
    process_markdown_folder(args.input_folder, args.output_dir)

if __name__ == "__main__":
    main() 