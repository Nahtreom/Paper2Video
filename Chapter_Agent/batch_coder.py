import os
import sys
import glob
import subprocess
import re
import time
from datetime import datetime

def print_separator(char="=", length=50):
    """打印分隔线"""
    print(char * length)

def format_time():
    """返回格式化的当前时间"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def print_progress_bar(current, total, width=50, prefix="进度"):
    """打印进度条"""
    percent = (current / total) * 100
    filled = int(width * current // total)
    bar = '█' * filled + '░' * (width - filled)
    print(f"\r{prefix}: |{bar}| {current}/{total} ({percent:.1f}%)", end='', flush=True)

def format_duration(seconds):
    """格式化时间显示"""
    if seconds < 60:
        return f"{seconds:.0f}秒"
    elif seconds < 3600:
        return f"{seconds//60:.0f}分{seconds%60:.0f}秒"
    else:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return f"{hours:.0f}小时{minutes:.0f}分"

def process_markdown_folder(input_folder: str, output_dir: str, prompt_template: str = None):
    """
    处理指定文件夹下的所有markdown文件
    
    Args:
        input_folder: 输入文件夹路径
        output_dir: 输出目录路径
        prompt_template: 提示词模板路径
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
        print(f"\n[ERR] 错误：输入文件夹 '{input_folder}' 不存在")
        return
    
    # 创建输出目录（如果不存在）
    os.makedirs(output_dir, exist_ok=True)
    print(f"[DIR] 输出目录已准备: {output_dir}")
    
    # 获取所有markdown文件
    markdown_files = []
    for ext in ['*.md', '*.markdown']:
        markdown_files.extend(glob.glob(os.path.join(input_folder, '**', ext), recursive=True))
    
    if not markdown_files:
        print(f"\n[WARN]  警告：在文件夹 '{input_folder}' 中没有找到markdown文件")
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
    print(f"\n 找到 {total_files} 个markdown文件待处理")
    print(f"[TIME]  预估总时长: {total_files * 60}~{total_files * 90} 秒 (每个文件约60-90秒)")
    print("\n[LIST] 处理顺序：")
    for i, file in enumerate(markdown_files, 1):
        relative_path = os.path.relpath(file, input_folder)
        print(f"   {i}. {relative_path}")
    print_separator("-")
    
    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    method_coder_path = os.path.join(current_dir, 'Chapter_Coder.py')
    
    # 处理统计
    success_count = 0
    failed_files = []
    start_time = time.time()
    
    print(f"\n 开始批量代码生成...")
    
    # 处理每个markdown文件
    for index, markdown_file in enumerate(markdown_files, 1):
        relative_path = os.path.relpath(markdown_file, input_folder)
        
        # 显示当前文件信息
        print(f"\n[FILE] 正在处理: {relative_path}")
        print(f" 进度: {index}/{total_files}")
        
        # 显示进度条
        print_progress_bar(index-1, total_files, prefix="总体进度")
        print()  # 换行
        
        file_start_time = time.time()
        
        try:
            print(f"[PROC] 启动Manim代码生成器...")
            cmd_args = [
                sys.executable,
                method_coder_path,
                markdown_file,
                '--output-dir', output_dir
            ]
            
            # 如果提供了prompt_template参数，添加到命令中
            if prompt_template:
                cmd_args.extend(['--prompt-template', prompt_template])
            
            subprocess.run(cmd_args, check=True)
            
            file_duration = time.time() - file_start_time
            success_count += 1
            print(f"[OK] 完成！耗时: {format_duration(file_duration)}")
            
        except subprocess.CalledProcessError as e:
            file_duration = time.time() - file_start_time
            failed_files.append(relative_path)
            print(f"[ERR] 处理失败 (耗时: {format_duration(file_duration)})")
            print(f"   错误信息: {str(e)}")
            continue
        
        # 计算预估剩余时间
        elapsed_time = time.time() - start_time
        avg_time_per_file = elapsed_time / index
        remaining_files = total_files - index
        estimated_remaining = avg_time_per_file * remaining_files
        
        # 更新完成的进度条
        print_progress_bar(index, total_files, prefix="总体进度")
        print(f" - 剩余: {remaining_files}个文件, 预估时间: {format_duration(estimated_remaining)}")
        
        if index < total_files:  # 不是最后一个文件
            print_separator("-")
    
    # 计算总耗时
    total_duration = time.time() - start_time
    avg_time = total_duration / total_files if total_files > 0 else 0
    
    # 打印最终进度条（100%）
    print_progress_bar(total_files, total_files, prefix="总体进度")
    print(" - 全部完成！")
    
    # 打印总结报告
    print_separator()
    print(f"\n[TARGET] 代码生成完成! 成功生成 {success_count} 个Python代码文件")
    print_separator("-")
    print(f"[PROG] 详细统计:")
    print(f"   • 总文件数: {total_files}")
    print(f"   • 成功生成: {success_count}")
    print(f"   • 生成失败: {len(failed_files)}")
    print(f"   • 成功率: {(success_count/total_files*100):.1f}%")
    print(f"   • 总耗时: {format_duration(total_duration)}")
    print(f"   • 平均耗时: {format_duration(avg_time)}/文件")
    
    if failed_files:
        print(f"\n[ERR] 以下 {len(failed_files)} 个文件处理失败:")
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
    parser.add_argument('--prompt-template', help='提示词模板路径', default=None)
    
    args = parser.parse_args()
    
    # 处理文件夹
    process_markdown_folder(args.input_folder, args.output_dir, args.prompt_template)

if __name__ == "__main__":
    main() 