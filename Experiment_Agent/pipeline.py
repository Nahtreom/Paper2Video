#!/usr/bin/env python3
"""
Method_Agent Complete Pipeline Script
完整的学术论文到教学视频的自动化处理流程

使用方法:
python pipeline.py path/to/paper.md [--output-base-dir output_directory]

流程:
1. Method_Brain.py - AI智能分割论文
2. split.py - 物理分割为独立页面文件
3. batch_coder.py - 批量生成Manim代码
4. batch_speecher.py - 批量生成演讲稿
"""

import os
import sys
import subprocess
import argparse
import time
import shutil
from datetime import datetime
from pathlib import Path

def print_separator(char="=", length=80):
    """打印分隔线"""
    print(char * length)

def print_step(step_number, step_name, description=""):
    """打印步骤信息"""
    print_separator()
    print(f"[STEP] 步骤 {step_number}: {step_name}")
    if description:
        print(f"   {description}")
    print(f"   开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print_separator("-")

def run_command(command, description="", real_time_output=False):
    """执行命令并处理错误"""
    print(f"[PROC] 执行命令: {' '.join(command)}")
    if description:
        print(f"   {description}")
    
    try:
        if real_time_output:
            # 实时输出模式，适用于长时间运行的命令
            # 添加PYTHONUNBUFFERED环境变量强制无缓冲输出
            env = os.environ.copy()
            env['PYTHONUNBUFFERED'] = '1'
            env['PYTHONIOENCODING'] = 'utf-8'
            
            print("[PROC] 启动实时输出模式...")
            
            process = subprocess.Popen(
                command, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT,
                text=True,
                universal_newlines=True,
                bufsize=0,  # 改为0，完全无缓冲
                env=env
            )
            
            # 实时读取并打印输出
            output_lines = []
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    clean_output = output.rstrip()
                    if clean_output:  # 只打印非空行
                        print(f"[PROG] {clean_output}")
                        sys.stdout.flush()
                        output_lines.append(clean_output)
            
            # 等待进程完成并获取返回码
            return_code = process.poll()
            if return_code == 0:
                print("[OK] 命令执行成功")
                return True
            else:
                print(f"[ERR] 命令执行失败，返回码: {return_code}")
                return False
        else:
            # 传统模式，适用于快速命令
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            print("[OK] 命令执行成功")
            if result.stdout:
                print("输出:")
                print(result.stdout)
            return True
    except subprocess.CalledProcessError as e:
        print(f"[ERR] 命令执行失败: {e}")
        if e.stdout:
            print("标准输出:")
            print(e.stdout)
        if e.stderr:
            print("错误输出:")
            print(e.stderr)
        return False
    except Exception as e:
        print(f"[ERR] 命令执行出现异常: {e}")
        return False

def validate_input_file(paper_path):
    """验证输入文件"""
    if not os.path.exists(paper_path):
        raise FileNotFoundError(f"输入文件不存在: {paper_path}")
    
    if not paper_path.lower().endswith(('.md', '.markdown')):
        raise ValueError(f"输入文件必须是Markdown格式: {paper_path}")
    
    print(f"[OK] 输入文件验证通过: {paper_path}")

def setup_directories(paper_path, output_base_dir):
    """设置和创建所需的目录结构"""
    paper_name = Path(paper_path).stem
    
    # 创建基础输出目录结构
    dirs = {
        'base': output_base_dir,
        'segmentation': os.path.join(output_base_dir, f"{paper_name}_segmentation"),
        'split_pages': os.path.join(output_base_dir, f"{paper_name}_segmentation", "split_pages"),
        'generated_code': os.path.join(output_base_dir, f"{paper_name}_generated_code"),
        'generated_speech': os.path.join(output_base_dir, f"{paper_name}_generated_speech")
    }
    
    # 创建所有目录
    for dir_name, dir_path in dirs.items():
        os.makedirs(dir_path, exist_ok=True)
        print(f"[DIR] 创建目录: {dir_path}")
    
    return dirs

def copy_images_directory(images_dir, target_dirs):
    """
    将图片目录复制到目标目录中
    
    Args:
        images_dir: 源图片目录路径
        target_dirs: 目标目录列表
    """
    if not images_dir or not os.path.exists(images_dir):
        if images_dir:
            print(f"[WARN]  图片目录不存在: {images_dir}")
        else:
            print("[IMG] 未指定图片目录，跳过图片复制")
        return
    
    images_dir = os.path.abspath(images_dir)
    images_dirname = os.path.basename(images_dir)
    
    print(f"[IMG] 开始复制图片目录: {images_dir}")
    
    copied_count = 0
    failed_count = 0
    
    for target_dir in target_dirs:
        try:
            if os.path.exists(target_dir):
                dest_path = os.path.join(target_dir, images_dirname)
                
                # 如果目标目录已存在，先删除
                if os.path.exists(dest_path):
                    shutil.rmtree(dest_path)
                    print(f"   [DEL]  删除已存在的目录: {dest_path}")
                
                # 复制图片目录
                shutil.copytree(images_dir, dest_path)
                print(f"   [OK] 复制到: {dest_path}")
                copied_count += 1
            else:
                print(f"   [WARN]  目标目录不存在: {target_dir}")
                failed_count += 1
                
        except Exception as e:
            print(f"   [ERR] 复制到 {target_dir} 失败: {str(e)}")
            failed_count += 1
    
    print(f"[IMG] 图片目录复制完成: 成功 {copied_count} 个，失败 {failed_count} 个")

def step1_brain_segmentation(paper_path, segmentation_dir):
    """步骤1: 使用Method_Brain.py进行AI智能分割"""
    print_step(1, "AI智能分割", "使用Method_Brain.py将论文分割为逻辑页面")
    
    print("[LIST] AI智能分割说明:")
    print("   • 使用GPT-4.5模型分析论文逻辑结构")
    print("   • 根据内容语义自然分割为适合视频展示的页面")
    print("   • 每页控制在15秒视频时长内")
    print("   • 保持原文内容不变，只进行逻辑划分")
    print()
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    brain_script = os.path.join(current_dir, "Method_Brain.py")
    
    command = [sys.executable, brain_script, paper_path, segmentation_dir]
    
    success = run_command(command, "AI分析论文结构并生成分割版本")
    if not success:
        raise RuntimeError("AI智能分割失败")
    
    return True

def step2_physical_split(segmentation_dir, split_pages_dir):
    """步骤2: 使用split.py进行物理分割"""
    print_step(2, "物理分割", "使用split.py将分割后的文档拆分为独立页面文件")
    
    print("[LIST] 物理分割说明:")
    print("   • 将AI分割的完整文档按页面标记拆分")
    print("   • 每页生成独立的Markdown文件")
    print("   • 便于后续批量处理和管理")
    print()
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    split_script = os.path.join(current_dir, "split.py")
    
    # 查找AI分割生成的文件
    segmentation_files = [f for f in os.listdir(segmentation_dir) if f.endswith('_split.md')]
    if not segmentation_files:
        raise FileNotFoundError(f"在 {segmentation_dir} 中未找到AI分割生成的文件")
    
    segmentation_file = os.path.join(segmentation_dir, segmentation_files[0])
    print(f"[FILE] 找到分割文件: {segmentation_file}")
    
    command = [sys.executable, split_script, segmentation_file, split_pages_dir]
    
    success = run_command(command, "将分割文档拆分为独立的页面文件")
    if not success:
        raise RuntimeError("物理分割失败")
    
    # 验证分割结果
    page_files = [f for f in os.listdir(split_pages_dir) if f.endswith('.md')]
    print(f"[TARGET] 物理分割完成! 成功生成 {len(page_files)} 个页面文件")
    
    return True

def step3_batch_coding(split_pages_dir, generated_code_dir):
    """步骤3: 使用batch_coder.py批量生成代码"""
    print_step(3, "批量代码生成", "使用batch_coder.py为每个页面生成Manim动画代码")
    
    print("[LIST] 批量代码生成说明:")
    print("   • 使用GPT-4.5为每个页面生成Manim动画Python代码")
    print("   • 自动处理图片引用和尺寸适配")
    print("   • 包含动画效果: Write(), FadeIn(), 等")
    print("   • 控制视频时长在15秒以内")
    print("   • 处理时间: 每页约30-90秒")
    print()
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    batch_coder_script = os.path.join(current_dir, "batch_coder.py")
    
    command = [sys.executable, batch_coder_script, split_pages_dir, generated_code_dir]
    
    print("[PROC] 开始批量代码生成，将实时显示每个文件的处理进度...")
    success = run_command(command, "为每个页面生成对应的Manim动画Python代码", real_time_output=True)
    if not success:
        raise RuntimeError("批量代码生成失败")
    
    # 验证生成结果
    code_files = [f for f in os.listdir(generated_code_dir) if f.endswith('.py')]
    print(f"[TARGET] 代码生成完成! 成功生成 {len(code_files)} 个Python代码文件")
    
    return True

def step4_batch_speech(split_pages_dir, generated_code_dir, generated_speech_dir):
    """步骤4: 使用batch_speecher.py批量生成演讲稿"""
    print_step(4, "批量演讲稿生成", "使用batch_speecher.py为每个页面生成演讲稿")
    
    print("[LIST] 批量演讲稿生成说明:")
    print("   • 结合论文内容和Manim代码生成配音文本")
    print("   • 保持页面间逻辑连贯性")
    print("   • 使用中文口语化表达")
    print("   • 控制配音时长在30秒以内")
    print("   • 处理时间: 每页约20-60秒")
    print()
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    batch_speecher_script = os.path.join(current_dir, "batch_speecher.py")
    
    command = [sys.executable, batch_speecher_script, split_pages_dir, generated_code_dir, generated_speech_dir]
    
    print("[PROC] 开始批量演讲稿生成，将实时显示每个文件对的处理进度...")
    success = run_command(command, "为每个页面生成对应的演讲稿", real_time_output=True)
    if not success:
        raise RuntimeError("批量演讲稿生成失败")
    
    # 验证生成结果
    speech_files = [f for f in os.listdir(generated_speech_dir) if f.endswith('.txt')]
    print(f"[TARGET] 演讲稿生成完成! 成功生成 {len(speech_files)} 个演讲稿文件")
    
    return True

def collect_generated_files(dirs):
    """收集所有生成的文件信息"""
    files = {}
    
    # 收集分割页面文件
    split_pages_dir = dirs['split_pages']
    if os.path.exists(split_pages_dir):
        page_files = [f for f in os.listdir(split_pages_dir) if f.endswith('.md')]
        for f in sorted(page_files):
            files[f] = {
                'path': os.path.join(split_pages_dir, f),
                'type': '  页面文件',
                'category': 'split_pages'
            }
    
    # 收集代码文件
    code_dir = dirs['generated_code']
    if os.path.exists(code_dir):
        code_files = [f for f in os.listdir(code_dir) if f.endswith('.py')]
        for f in sorted(code_files):
            files[f] = {
                'path': os.path.join(code_dir, f),
                'type': '  代码文件',
                'category': 'generated_code'
            }
    
    # 收集演讲稿文件
    speech_dir = dirs['generated_speech']
    if os.path.exists(speech_dir):
        speech_files = [f for f in os.listdir(speech_dir) if f.endswith('.txt')]
        for f in sorted(speech_files):
            files[f] = {
                'path': os.path.join(speech_dir, f),
                'type': '  演讲稿',
                'category': 'generated_speech'
            }
    
    # 收集分割文档
    segmentation_dir = dirs['segmentation']
    if os.path.exists(segmentation_dir):
        split_files = [f for f in os.listdir(segmentation_dir) if f.endswith('_split.md')]
        for f in sorted(split_files):
            files[f] = {
                'path': os.path.join(segmentation_dir, f),
                'type': '[FILE] 分割文档',
                'category': 'segmentation'
            }
    
    return files

def print_file_list(files):
    """打印文件列表"""
    print_separator("=")
    print("[LIST] 生成的文件完整列表:")
    print_separator("-")
    
    # 按类别分组显示
    categories = {
        'segmentation': '[FILE] 分割文档',
        'split_pages': '  页面文件', 
        'generated_code': '  代码文件',
        'generated_speech': '  演讲稿'
    }
    
    for category, category_name in categories.items():
        category_files = [filename for filename, info in files.items() if info['category'] == category]
        if category_files:
            print(f"\n{category_name}:")
            for filename in sorted(category_files):
                print(f"   • {filename}")
    
    print(f"\n[PROG] 总计: {len(files)} 个文件")
    print_separator("-")

def interactive_file_editor(files):
    """交互式文件编辑器"""
    print("🔧 进入交互式文件查看/编辑模式")
    print("   • 输入文件名 (支持部分匹配) 来查看或编辑文件")
    print("   • 输入 'list' 或 'ls' 重新显示文件列表") 
    print("   • 输入 'q' 退出交互模式")
    print_separator("-")
    
    while True:
        try:
            user_input = input("\n[FIND] 请输入文件名 (或 'q' 退出): ").strip()
            
            if user_input.lower() in ['q', 'quit', 'exit']:
                print("[BYE] 退出交互模式")
                break
            
            if user_input.lower() in ['list', 'ls', 'l']:
                print_file_list(files)
                continue
            
            if not user_input:
                print("[ALERT] 请输入有效的文件名")
                continue
            
            # 查找匹配的文件
            matched_files = []
            for filename, info in files.items():
                if user_input.lower() in filename.lower():
                    matched_files.append((filename, info))
            
            if not matched_files:
                print(f"[ALERT] 未找到匹配 '{user_input}' 的文件")
                print("[TIP] 提示: 可以输入 'list' 查看所有文件")
                continue
            
            if len(matched_files) == 1:
                # 只有一个匹配，直接打开
                filename, info = matched_files[0]
                file_path = info['path']
                file_type = info['type']
                
                print(f"[OPEN] 打开 {file_type}: {filename}")
                print(f"   路径: {file_path}")
                
                # 使用vim打开文件
                try:
                    subprocess.run(['vim', file_path], check=True)
                    print(f"[OK] 文件编辑完成: {filename}")
                except subprocess.CalledProcessError as e:
                    print(f"[ERR] 打开文件失败: {e}")
                except FileNotFoundError:
                    print("[ERR] 未找到vim编辑器，请确保vim已安装")
                    print("[TIP] 您也可以使用其他编辑器手动打开文件:")
                    print(f"   {file_path}")
                except KeyboardInterrupt:
                    print(f"\n[WARN] 编辑被中断")
                
            else:
                # 多个匹配，让用户选择
                print(f"[FIND] 找到 {len(matched_files)} 个匹配的文件:")
                for i, (filename, info) in enumerate(matched_files, 1):
                    print(f"   {i}. {info['type']} {filename}")
                
                try:
                    choice = input("请输入序号选择文件 (或回车取消): ").strip()
                    if choice:
                        index = int(choice) - 1
                        if 0 <= index < len(matched_files):
                            filename, info = matched_files[index]
                            file_path = info['path']
                            file_type = info['type']
                            
                            print(f"[OPEN] 打开 {file_type}: {filename}")
                            
                            try:
                                subprocess.run(['vim', file_path], check=True)
                                print(f"[OK] 文件编辑完成: {filename}")
                            except subprocess.CalledProcessError as e:
                                print(f"[ERR] 打开文件失败: {e}")
                            except FileNotFoundError:
                                print("[ERR] 未找到vim编辑器，请确保vim已安装")
                                print(f"[TIP] 您也可以手动打开文件: {file_path}")
                            except KeyboardInterrupt:
                                print(f"\n[WARN] 编辑被中断")
                        else:
                            print("[ALERT] 无效的序号")
                except ValueError:
                    print("[ALERT] 请输入有效的数字")
                except KeyboardInterrupt:
                    print(f"\n[WARN] 操作被中断")
        
        except KeyboardInterrupt:
            print(f"\n[BYE] 退出交互模式")
            break
        except EOFError:
            print(f"\n[BYE] 退出交互模式")
            break

def print_final_summary(dirs, paper_path, start_time):
    """打印最终总结"""
    end_time = time.time()
    duration = end_time - start_time
    
    print_separator("=")
    print("[DONE] Method 部分 Pipeline 执行完成！")
    print_separator("-")
    print(f"[FILE] 输入文件: {paper_path}")
    print(f"[TIME]  总耗时: {duration:.2f} 秒 ({duration/60:.1f} 分钟)")
    print(f"[DIR] 输出目录: {dirs['base']}")
    print("\n[OPEN] 生成的文件结构:")
    print(f"   ├── [DIR] 分割结果: {os.path.relpath(dirs['segmentation'])}")
    print(f"   │   ├── *_split.md (AI智能分割的完整文档)")
    print(f"   │   └── split_pages/ (独立页面文件)")
    print(f"   ├── [DIR] 代码文件: {os.path.relpath(dirs['generated_code'])}")
    print(f"   │   └── *_code.py (Manim动画Python代码)")
    print(f"   └── [DIR] 演讲稿: {os.path.relpath(dirs['generated_speech'])}")
    print(f"       └── *_speech.txt (配音文本)")
    
    # 统计生成的文件数量
    try:
        page_count = len([f for f in os.listdir(dirs['split_pages']) if f.endswith('.md')])
        code_count = len([f for f in os.listdir(dirs['generated_code']) if f.endswith('.py')])
        speech_count = len([f for f in os.listdir(dirs['generated_speech']) if f.endswith('.txt')])
        
        print(f"\n[PROG] 生成统计:")
        print(f"     页面数量: {page_count}")
        print(f"     代码文件: {code_count}")
        print(f"     演讲稿: {speech_count}")
        
        if page_count == code_count == speech_count:
            print(f"   [OK] 所有文件生成完整，页面匹配完美!")
        else:
            print(f"   [WARN]  文件数量不匹配，请检查生成结果")
    except Exception as e:
        print(f"   统计文件数量时出错: {e}")
    
    print_separator("=")

def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="Method_Agent 完整Pipeline - 从学术论文到教学视频的自动化处理",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
    python pipeline.py paper/ChatDev.md
    python pipeline.py paper/MASLab.md --output-base-dir ./output
    python pipeline.py paper/ChatDev.md --images-dir ./ChatDev_images --output-base-dir ./output
        """
    )
    
    parser.add_argument(
        'paper_path',
        help='输入的学术论文Markdown文件路径'
    )
    
    parser.add_argument(
        '--output-base-dir',
        default='./pipeline_output',
        help='输出基础目录路径 (默认: ./pipeline_output)'
    )
    
    parser.add_argument(
        '--images-dir',
        help='图片目录路径，将被复制到生成代码和分割页面目录中'
    )
    
    args = parser.parse_args()
    
    start_time = time.time()
    
    try:
        print_separator("=")
        print(f"  Method_Agent Pipeline 启动")
        print(f"[FILE] 输入文件: {args.paper_path}")
        print(f"[DIR] 输出目录: {args.output_base_dir}")
        if args.images_dir:
            print(f"[IMG] 图片目录: {args.images_dir}")
        print_separator("=")
        
        # 验证输入文件
        validate_input_file(args.paper_path)
        
        # 设置目录结构
        dirs = setup_directories(args.paper_path, args.output_base_dir)
        
        # 执行Pipeline步骤
        step1_brain_segmentation(args.paper_path, dirs['segmentation'])
        step2_physical_split(dirs['segmentation'], dirs['split_pages'])
        
        # 复制图片目录到相应位置
        if args.images_dir:
            print_separator("=")
            print("[IMG] 图片目录复制")
            print("   将指定的图片目录复制到生成代码和分割页面目录中")
            print_separator("-")
            
            target_dirs = [dirs['split_pages'], dirs['generated_code']]
            copy_images_directory(args.images_dir, target_dirs)
        
        step3_batch_coding(dirs['split_pages'], dirs['generated_code'])
        step4_batch_speech(dirs['split_pages'], dirs['generated_code'], dirs['generated_speech'])
        
        # 打印最终总结
        print_final_summary(dirs, args.paper_path, start_time)
        
        # 收集生成的文件
        generated_files = collect_generated_files(dirs)
        
        # 显示文件列表
        print_file_list(generated_files)
        
        # 检查是否跳过交互式编辑
        skip_interactive = os.environ.get('SKIP_INTERACTIVE', '').lower() in ['1', 'true', 'yes']
        
        if skip_interactive:
            print("  检测到SKIP_INTERACTIVE环境变量，跳过交互式编辑")
        else:
            # 进入交互式编辑模式
            if generated_files:
                interactive_file_editor(generated_files)
            else:
                print("[WARN] 未找到生成的文件，跳过交互式编辑")
        
        print("\n[DONE] Pipeline 全部完成！感谢使用 Experiment_Agent！")
        
    except KeyboardInterrupt:
        print("\n[WARN] 用户中断了Pipeline执行")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERR] Pipeline执行失败: {str(e)}")
        print("请检查错误信息并重试")
        sys.exit(1)

if __name__ == "__main__":
    main() 