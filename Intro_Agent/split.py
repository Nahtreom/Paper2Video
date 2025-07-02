import os
import re
import argparse

def split_markdown_by_pages(input_file: str, output_dir: str):
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    # 获取原文件名（不带扩展名）
    base_filename = os.path.splitext(os.path.basename(input_file))[0]

    # 读取原始文件
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 用正则匹配每一页（以"# 页 x"开头）
    pages = re.split(r'(?=# 页 \d+)', content)

    # 遍历每一页并保存为单独的 markdown 文件
    for i, page in enumerate(pages):
        if page.strip():  # 跳过空内容
            match = re.match(r'# 页 (\d+)', page)
            if match:
                page_num = match.group(1)
                output_filename = f"{base_filename}_页{page_num}.md"
            else:
                # 如果没匹配到，使用索引作为后备
                output_filename = f"{base_filename}_页{i+1}.md"
            output_path = os.path.join(output_dir, output_filename)
            with open(output_path, 'w', encoding='utf-8') as out_file:
                out_file.write(page.strip())
            print(f"[OK] 生成：{output_filename}")

def main():
    """
    主函数，处理命令行参数
    """
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='将包含多页的Markdown文件按页分割为多个单独文件')
    parser.add_argument('input_file', help='输入的Markdown文件路径')
    parser.add_argument('output_dir', help='输出目录路径')
    
    args = parser.parse_args()
    
    # 检查输入文件是否存在
    if not os.path.exists(args.input_file):
        print(f"[ERR] 错误：输入文件 '{args.input_file}' 不存在")
        return
    
    print(f"[FILE] 输入文件: {args.input_file}")
    print(f"[DIR] 输出目录: {args.output_dir}")
    print("[PROC] 开始分割文件...")
    
    try:
        # 执行分割操作
        split_markdown_by_pages(args.input_file, args.output_dir)
        print(f"\n  分割完成！文件已保存到: {args.output_dir}")
    except Exception as e:
        print(f"[ERR] 分割失败: {str(e)}")

if __name__ == '__main__':
    main()
