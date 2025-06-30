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

def extract_page_number(filename: str) -> list:
    """
    从文件名中提取页码数字
    返回所有数字的列表，用于排序和匹配
    """
    base_name = os.path.splitext(os.path.basename(filename))[0]
    
    # 优先查找"页"字后面的数字
    page_match = re.search(r'页(\d+)', base_name)
    if page_match:
        return [int(page_match.group(1))]
    
    # 如果没有找到"页"字，回退到提取所有数字
    numbers = re.findall(r'\d+', base_name)
    return [int(num) for num in numbers] if numbers else []

def find_matching_files(markdown_folder: str, python_folder: str):
    """
    在两个文件夹中找到配对的markdown和python文件
    
    Args:
        markdown_folder: markdown文件夹路径
        python_folder: python文件夹路径
    
    Returns:
        list of tuples: 配对的(markdown_file, python_file)列表
    """
    # 获取所有文件
    markdown_files = []
    for ext in ['*.md', '*.markdown']:
        markdown_files.extend(glob.glob(os.path.join(markdown_folder, '**', ext), recursive=True))
    
    python_files = glob.glob(os.path.join(python_folder, '**', '*.py'), recursive=True)
    
    # 创建python文件的查找字典，键为页码数字列表的元组
    python_dict = {}
    for py_file in python_files:
        numbers = extract_page_number(py_file)
        if numbers:
            numbers_tuple = tuple(numbers)
            python_dict[numbers_tuple] = py_file
    
    # 查找匹配的文件对
    matched_pairs = []
    unmatched_markdowns = []
    
    for md_file in markdown_files:
        numbers = extract_page_number(md_file)
        if numbers:
            numbers_tuple = tuple(numbers)
            if numbers_tuple in python_dict:
                matched_pairs.append((md_file, python_dict[numbers_tuple]))
            else:
                unmatched_markdowns.append(md_file)
    
    return matched_pairs, unmatched_markdowns

def process_file_pairs(markdown_folder: str, python_folder: str, output_dir: str):
    """
    处理配对的文件
    """
    print_separator()
    print(f"[{format_time()}] 开始批量处理任务")
    print(f"Markdown文件夹: {markdown_folder}")
    print(f"Python文件夹: {python_folder}")
    print(f"输出目录: {output_dir}")
    
    # 获取文件夹的绝对路径
    markdown_folder = os.path.abspath(markdown_folder)
    python_folder = os.path.abspath(python_folder)
    output_dir = os.path.abspath(output_dir)
    
    # 确保文件夹存在
    if not os.path.exists(markdown_folder):
        print(f"\n❌ 错误：Markdown文件夹 '{markdown_folder}' 不存在")
        return
    if not os.path.exists(python_folder):
        print(f"\n❌ 错误：Python文件夹 '{python_folder}' 不存在")
        return
    
    # 创建输出目录（如果不存在）
    os.makedirs(output_dir, exist_ok=True)
    print(f"📁 输出目录已准备: {output_dir}")
    
    # 查找配对的文件
    matched_pairs, unmatched_markdowns = find_matching_files(markdown_folder, python_folder)
    
    if not matched_pairs:
        print(f"\n⚠️  警告：没有找到配对的文件")
        return
    
    # 对配对按markdown文件名中的数字排序
    matched_pairs.sort(key=lambda x: extract_page_number(x[0]))
    
    total_pairs = len(matched_pairs)
    print(f"\n📝 找到 {total_pairs} 对配对文件")
    
    # 显示处理顺序
    print("\n📋 处理顺序：")
    for i, (md_file, py_file) in enumerate(matched_pairs, 1):
        md_relative = os.path.relpath(md_file, markdown_folder)
        py_relative = os.path.relpath(py_file, python_folder)
        print(f"   {i}. {md_relative} ↔️ {py_relative}")
    
    if unmatched_markdowns:
        print("\n⚠️  以下Markdown文件未找到匹配的Python文件：")
        for md_file in unmatched_markdowns:
            print(f"   - {os.path.relpath(md_file, markdown_folder)}")
    
    print_separator("-")
    
    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    method_speecher_path = os.path.join(current_dir, 'Method_Speecher.py')
    
    # 默认的previous_speech文件路径（用于第一个文件）
    default_previous_speech = os.path.join(current_dir, "prompt_templates", "Speecher-1.txt")
    
    # 处理统计
    success_count = 0
    failed_pairs = []
    previous_speech_path = default_previous_speech  # 第一个文件使用默认路径
    
    # 处理每对文件
    for index, (md_file, py_file) in enumerate(matched_pairs, 1):
        md_relative = os.path.relpath(md_file, markdown_folder)
        py_relative = os.path.relpath(py_file, python_folder)
        print(f"\n[{format_time()}] 处理文件对 ({index}/{total_pairs}):")
        print(f"   Markdown: {md_relative}")
        print(f"   Python: {py_relative}")
        print(f"   Previous Speech: {os.path.relpath(previous_speech_path, current_dir)}")
        
        try:
            # 构建命令参数，包含输出目录
            cmd_args = [
                sys.executable,
                method_speecher_path,
                md_file,
                py_file,
                previous_speech_path,  # 上一个页面的讲稿路径
                output_dir            # 输出目录
            ]
            
            subprocess.run(cmd_args, check=True)
            success_count += 1
            print(f"✅ 成功处理文件对")
            
            # 计算当前文件生成的演讲稿路径，作为下一个文件的previous_speech_path
            md_base_name = os.path.splitext(os.path.basename(md_file))[0]
            current_speech_path = os.path.join(output_dir, f"{md_base_name}_speech.txt")
            
            # 检查生成的演讲稿文件是否存在
            if os.path.exists(current_speech_path):
                previous_speech_path = current_speech_path  # 更新为下一次使用
                print(f"🔗 下一个文件将使用此演讲稿作为上下文: {os.path.basename(current_speech_path)}")
            else:
                print(f"⚠️  警告：未找到生成的演讲稿文件 {current_speech_path}")
                print(f"   下一个文件将继续使用: {os.path.relpath(previous_speech_path, current_dir)}")
            
        except subprocess.CalledProcessError as e:
            failed_pairs.append((md_relative, py_relative))
            print(f"❌ 处理失败")
            print(f"   错误信息: {str(e)}")
            print(f"   下一个文件将继续使用: {os.path.relpath(previous_speech_path, current_dir)}")
            continue
            
        # 显示进度
        progress = (index / total_pairs) * 100
        print(f"进度: [{index}/{total_pairs}] {progress:.1f}%")
        print_separator("-")
    
    # 打印总结报告
    print_separator()
    print(f"\n📊 处理完成！总结报告:")
    print(f"总文件对数: {total_pairs}")
    print(f"成功处理: {success_count}")
    print(f"处理失败: {len(failed_pairs)}")
    
    if failed_pairs:
        print("\n❌ 以下文件对处理失败:")
        for md_file, py_file in failed_pairs:
            print(f"   - Markdown: {md_file}")
            print(f"     Python: {py_file}")
    
    print(f"\n✨ 生成的演讲稿已保存到 {os.path.relpath(output_dir, os.getcwd())} 目录")
    print_separator()

def main():
    """
    主函数
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='批量处理配对的Markdown和Python文件')
    parser.add_argument('markdown_folder', help='包含Markdown文件的文件夹路径')
    parser.add_argument('python_folder', help='包含Python文件的文件夹路径')
    parser.add_argument('output_dir', help='演讲稿输出目录路径')
    
    args = parser.parse_args()
    
    process_file_pairs(args.markdown_folder, args.python_folder, args.output_dir)

if __name__ == "__main__":
    main()