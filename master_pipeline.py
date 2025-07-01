#!/usr/bin/env python3
"""
EduAgent Master Pipeline
完整的学术论文到教学视频的自动化处理主流程

使用方法:
python master_pipeline.py path/to/paper.md path/to/images [--output-base-dir output_directory]

流程:
1. 调用document_processor.py切分论文为四个章节
2. 依次调用各个Agent的pipeline处理对应章节
3. 最后统一进行人机交互
"""

import os
import sys
import subprocess
import argparse
import time
import shutil
import json
from datetime import datetime
from pathlib import Path

def print_separator(char="=", length=100):
    """打印分隔线"""
    print(char * length)

def print_header():
    """打印标题"""
    print_separator("=")
    print("🎓 EduAgent Master Pipeline - 学术论文到教学视频的完整自动化处理")
    print_separator("=")

def print_step(step_number, step_name, description=""):
    """打印步骤信息"""
    print_separator("-")
    print(f"📍 阶段 {step_number}: {step_name}")
    if description:
        print(f"   {description}")
    print(f"   开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print_separator("-")

def run_command(command, description="", cwd=None, capture_output=False):
    """执行命令并处理错误"""
    return run_command_with_env(command, description, cwd, capture_output, None)

def run_command_with_env(command, description="", cwd=None, capture_output=False, env=None):
    """执行命令并处理错误，支持自定义环境变量"""
    print(f"🔄 执行命令: {' '.join(command)}")
    if description:
        print(f"   {description}")
    if cwd:
        print(f"   工作目录: {cwd}")
    
    # 设置环境变量
    if env is None:
        env = os.environ.copy()
    else:
        # 确保包含基本的Python环境变量
        base_env = os.environ.copy()
        base_env.update(env)
        env = base_env
    
    env['PYTHONUNBUFFERED'] = '1'
    env['PYTHONIOENCODING'] = 'utf-8'
    
    try:
        if capture_output:
            result = subprocess.run(command, check=True, capture_output=True, text=True, cwd=cwd, env=env)
            print("✅ 命令执行成功")
            return result.stdout
        else:
            # 实时输出模式
            process = subprocess.Popen(
                command, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT,
                text=True,
                universal_newlines=True,
                bufsize=0,  # 完全无缓冲，确保进度条实时显示
                env=env,
                cwd=cwd
            )
            
            # 实时读取并打印输出
            current_progress_line = ""  # 记录当前进度条状态
            
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    clean_output = output.rstrip()
                    if clean_output:
                        # 检查是否是进度条输出
                        is_progress = any([
                            "总体进度:" in clean_output and "|" in clean_output,
                            "%" in clean_output and "|" in clean_output,
                            clean_output.startswith("进度:"),
                            "Processing:" in clean_output and "%" in clean_output,
                            clean_output.count('█') > 3,  # 进度条字符
                            clean_output.count('▓') > 3,  # 进度条字符
                            clean_output.count('░') > 3,  # 进度条字符
                            clean_output.count('■') > 3,  # 进度条字符
                            clean_output.startswith('\r')
                        ])
                        
                        if is_progress:
                            # 这是进度条，使用回车覆盖显示
                            clean_line = clean_output.lstrip('\r')
                            print(f"\r   {clean_line}", end='', flush=True)
                            current_progress_line = clean_line
                        else:
                            # 普通输出
                            if current_progress_line:
                                # 如果之前有进度条，先换行
                                print()
                                current_progress_line = ""
                            
                            # 过滤重复的前缀
                            if not clean_output.startswith('📊'):
                                print(f"   {clean_output}")
                            sys.stdout.flush()
            
            # 如果最后有进度条，确保换行
            if current_progress_line:
                print()
            
            return_code = process.poll()
            if return_code == 0:
                print("✅ 命令执行成功")
                return True
            else:
                print(f"❌ 命令执行失败，返回码: {return_code}")
                return False
                
    except subprocess.CalledProcessError as e:
        print(f"❌ 命令执行失败: {e}")
        if e.stdout:
            print("标准输出:")
            print(e.stdout)
        if e.stderr:
            print("错误输出:")
            print(e.stderr)
        return False
    except Exception as e:
        print(f"❌ 命令执行出现异常: {e}")
        return False

def validate_inputs(paper_path, images_dir):
    """验证输入参数"""
    print("🔍 验证输入参数...")
    
    # 验证论文文件
    if not os.path.exists(paper_path):
        raise FileNotFoundError(f"论文文件不存在: {paper_path}")
    
    if not paper_path.lower().endswith(('.md', '.markdown')):
        raise ValueError(f"论文文件必须是Markdown格式: {paper_path}")
    
    print(f"✅ 论文文件验证通过: {paper_path}")
    
    # 验证图片目录
    if not os.path.exists(images_dir):
        raise FileNotFoundError(f"图片目录不存在: {images_dir}")
    
    if not os.path.isdir(images_dir):
        raise ValueError(f"图片路径不是目录: {images_dir}")
    
    print(f"✅ 图片目录验证通过: {images_dir}")

def setup_master_directories(paper_path, output_base_dir):
    """设置主输出目录结构"""
    paper_name = Path(paper_path).stem
    
    # 创建主目录结构
    dirs = {
        'base': output_base_dir,
        'sections': os.path.join(output_base_dir, 'sections'),
        'intro_output': os.path.join(output_base_dir, 'intro_agent_output'),
        'method_output': os.path.join(output_base_dir, 'method_agent_output'),
        'experiment_output': os.path.join(output_base_dir, 'experiment_agent_output'),
        'conclusion_output': os.path.join(output_base_dir, 'conclusion_agent_output'),
        'final_results': os.path.join(output_base_dir, 'final_results')
    }
    
    # 创建所有目录
    for dir_name, dir_path in dirs.items():
        os.makedirs(dir_path, exist_ok=True)
        print(f"📁 创建目录: {dir_path}")
    
    return dirs

def step1_section_splitting(paper_path, sections_dir):
    """步骤1: 调用document_processor.py切分论文"""
    print_step(1, "论文章节切分", "使用document_processor.py将论文切分为四个主要章节")
    
    # 检查document_processor.py是否存在
    document_processor_path = os.path.join(os.getcwd(), "document_processor.py")
    if not os.path.exists(document_processor_path):
        raise FileNotFoundError("未找到document_processor.py文件")
    
    # 执行切分命令
    command = [sys.executable, "document_processor.py", paper_path, sections_dir]
    success = run_command(command, "切分论文为Introduction、Methods、Experiments、Conclusion四个章节")
    
    if not success:
        raise RuntimeError("论文切分失败")
    
    # 检查切分结果
    paper_name = Path(paper_path).stem
    expected_sections = ['Introduction', 'Methods', 'Experiments', 'Conclusion']
    section_files = {}
    
    for section in expected_sections:
        section_file = os.path.join(sections_dir, f"{paper_name}_{section}.md")
        if os.path.exists(section_file):
            section_files[section] = section_file
            print(f"✅ 找到章节文件: {section_file}")
        else:
            print(f"⚠️  未找到章节文件: {section_file}")
    
    if not section_files:
        raise RuntimeError("未找到任何章节文件，切分可能失败")
    
    return section_files

def step2_process_agents(section_files, images_dir, dirs):
    """步骤2: 依次调用各个Agent处理对应章节"""
    print_step(2, "Agent处理流程", "依次调用Intro、Method、Experiment、Conclusion Agent")
    
    # Agent配置
    agents_config = [
        {
            'name': 'Introduction',
            'folder': 'Intro_Agent',
            'output_dir': dirs['intro_output'],
            'section_key': 'Introduction'
        },
        {
            'name': 'Methods',
            'folder': 'Method_Agent', 
            'output_dir': dirs['method_output'],
            'section_key': 'Methods'
        },
        {
            'name': 'Experiments',
            'folder': 'Experiment_Agent',
            'output_dir': dirs['experiment_output'],
            'section_key': 'Experiments'
        },
        {
            'name': 'Conclusion',
            'folder': 'Conclusion_Agent',
            'output_dir': dirs['conclusion_output'],
            'section_key': 'Conclusion'
        }
    ]
    
    processed_results = {}
    
    for i, agent_config in enumerate(agents_config, 1):
        agent_name = agent_config['name']
        agent_folder = agent_config['folder']
        output_dir = agent_config['output_dir']
        section_key = agent_config['section_key']
        
        print(f"\n🤖 处理 {agent_name} Agent ({i}/4)")
        
        # 检查章节文件是否存在
        if section_key not in section_files:
            print(f"⚠️  跳过 {agent_name} Agent: 未找到对应的章节文件")
            continue
            
        section_file = section_files[section_key]
        
        # 检查Agent目录是否存在
        if not os.path.exists(agent_folder):
            print(f"⚠️  跳过 {agent_name} Agent: 目录不存在 {agent_folder}")
            continue
            
        pipeline_path = os.path.join(agent_folder, "pipeline.py")
        if not os.path.exists(pipeline_path):
            print(f"⚠️  跳过 {agent_name} Agent: pipeline.py不存在")
            continue
        
        # 构建命令（设置环境变量跳过交互）
        command = [
            sys.executable, "pipeline.py", 
            os.path.abspath(section_file),
            "--output-base-dir", os.path.abspath(output_dir),
            "--images-dir", os.path.abspath(images_dir)
        ]
        
        print(f"📂 输入文件: {section_file}")
        print(f"📁 输出目录: {output_dir}")
        print(f"📷 图片目录: {images_dir}")
        
        # 设置环境变量跳过交互式编辑
        env = os.environ.copy()
        env['SKIP_INTERACTIVE'] = '1'
        
        # 执行Agent pipeline，传递修改后的环境变量
        success = run_command_with_env(
            command, 
            f"处理{agent_name}章节",
            cwd=agent_folder,
            env=env
        )
        
        if success:
            processed_results[agent_name] = {
                'section_file': section_file,
                'output_dir': output_dir,
                'status': 'success'
            }
            print(f"✅ {agent_name} Agent 处理完成")
        else:
            processed_results[agent_name] = {
                'section_file': section_file,
                'output_dir': output_dir,
                'status': 'failed'
            }
            print(f"❌ {agent_name} Agent 处理失败")
    
    return processed_results

def step3_collect_results(processed_results, final_results_dir):
    """步骤3: 收集和整理所有生成的文件"""
    print_step(3, "结果收集", "收集所有Agent生成的文件到最终结果目录")
    
    collected_files = {
        'segmentation': [],
        'split_pages': [],
        'code_files': [],
        'speech_files': []
    }
    
    for agent_name, result in processed_results.items():
        if result['status'] != 'success':
            continue
            
        output_dir = result['output_dir']
        agent_final_dir = os.path.join(final_results_dir, agent_name.lower())
        os.makedirs(agent_final_dir, exist_ok=True)
        
        print(f"\n📦 收集 {agent_name} Agent 的结果...")
        
        # 查找生成的文件
        for root, dirs, files in os.walk(output_dir):
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, output_dir)
                
                # 确定文件类型
                if file.endswith('_split.md'):
                    file_type = 'segmentation'
                elif file.endswith('.md') and 'split_pages' in root:
                    file_type = 'split_pages'
                elif file.endswith('_code.py'):
                    file_type = 'code_files'
                elif file.endswith('_speech.txt'):
                    file_type = 'speech_files'
                else:
                    continue
                
                # 复制文件到最终结果目录
                dest_path = os.path.join(agent_final_dir, rel_path)
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                shutil.copy2(file_path, dest_path)
                
                collected_files[file_type].append({
                    'agent': agent_name,
                    'original_path': file_path,
                    'final_path': dest_path,
                    'filename': file
                })
                
                print(f"   📄 {file_type}: {file}")
    
    return collected_files

def step4_interactive_editor(collected_files):
    """步骤4: 统一的人机交互编辑环节"""
    print_step(4, "人机交互编辑", "提供统一的文件编辑和查看界面")
    
    # 统计文件
    total_files = sum(len(files) for files in collected_files.values())
    
    if total_files == 0:
        print("⚠️  没有找到生成的文件，跳过交互式编辑")
        return
    
    print(f"📊 找到 {total_files} 个生成的文件:")
    for file_type, files in collected_files.items():
        if files:
            print(f"   📁 {file_type}: {len(files)} 个文件")
            for file_info in files:
                print(f"      • {file_info['agent']}: {file_info['filename']}")
    
    print("\n🎮 交互式编辑说明:")
    print("   • 输入 'list' 查看所有文件")
    print("   • 输入文件名或关键词搜索并编辑文件")
    print("   • 输入 'summary' 查看处理总结")
    print("   • 输入 'quit' 或 'exit' 退出")
    print("   • 按 Ctrl+C 退出")
    
    # 创建文件索引
    all_files = []
    for file_type, files in collected_files.items():
        for file_info in files:
            all_files.append({
                'type': file_type,
                'agent': file_info['agent'],
                'filename': file_info['filename'],
                'path': file_info['final_path']
            })
    
    while True:
        try:
            user_input = input("\n🎯 请输入命令 (或文件名): ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 退出交互模式")
                break
                
            if user_input.lower() == 'list':
                print("\n📋 所有生成的文件:")
                for i, file_info in enumerate(all_files, 1):
                    print(f"   {i:2d}. [{file_info['agent']}] {file_info['type']}: {file_info['filename']}")
                continue
                
            if user_input.lower() == 'summary':
                print_processing_summary(collected_files)
                continue
            
            # 搜索文件
            matched_files = []
            for file_info in all_files:
                if (user_input.lower() in file_info['filename'].lower() or 
                    user_input.lower() in file_info['agent'].lower() or
                    user_input.lower() in file_info['type'].lower()):
                    matched_files.append(file_info)
            
            if not matched_files:
                print(f"❗ 未找到匹配 '{user_input}' 的文件")
                continue
            
            if len(matched_files) == 1:
                # 只有一个匹配，直接打开
                file_info = matched_files[0]
                print(f"📂 打开文件: [{file_info['agent']}] {file_info['filename']}")
                
                try:
                    subprocess.run(['vim', file_info['path']], check=True)
                    print(f"✅ 文件编辑完成")
                except subprocess.CalledProcessError as e:
                    print(f"❌ 打开文件失败: {e}")
                except FileNotFoundError:
                    print("❌ 未找到vim编辑器")
                    print(f"💡 文件路径: {file_info['path']}")
                except KeyboardInterrupt:
                    print(f"\n⚠️ 编辑被中断")
            else:
                # 多个匹配，让用户选择
                print(f"🔍 找到 {len(matched_files)} 个匹配的文件:")
                for i, file_info in enumerate(matched_files, 1):
                    print(f"   {i}. [{file_info['agent']}] {file_info['type']}: {file_info['filename']}")
                
                try:
                    choice = input("请输入序号选择文件 (或回车取消): ").strip()
                    if choice:
                        index = int(choice) - 1
                        if 0 <= index < len(matched_files):
                            file_info = matched_files[index]
                            print(f"📂 打开文件: [{file_info['agent']}] {file_info['filename']}")
                            
                            try:
                                subprocess.run(['vim', file_info['path']], check=True)
                                print(f"✅ 文件编辑完成")
                            except subprocess.CalledProcessError as e:
                                print(f"❌ 打开文件失败: {e}")
                            except FileNotFoundError:
                                print("❌ 未找到vim编辑器")
                                print(f"💡 文件路径: {file_info['path']}")
                            except KeyboardInterrupt:
                                print(f"\n⚠️ 编辑被中断")
                        else:
                            print("❗ 无效的序号")
                except ValueError:
                    print("❗ 请输入有效的数字")
                except KeyboardInterrupt:
                    print(f"\n⚠️ 操作被中断")
        
        except KeyboardInterrupt:
            print(f"\n👋 退出交互模式")
            break
        except EOFError:
            print(f"\n👋 退出交互模式")
            break

def print_processing_summary(collected_files):
    """打印处理总结"""
    print("\n📊 处理总结:")
    print_separator("-")
    
    for file_type, files in collected_files.items():
        if files:
            agents = set(file['agent'] for file in files)
            print(f"📁 {file_type}: {len(files)} 个文件")
            for agent in sorted(agents):
                agent_files = [f for f in files if f['agent'] == agent]
                print(f"   • {agent}: {len(agent_files)} 个文件")

def print_final_summary(dirs, paper_path, processed_results, start_time):
    """打印最终总结"""
    end_time = time.time()
    duration = end_time - start_time
    
    print_separator("=")
    print("🎉 EduAgent Master Pipeline 执行完成！")
    print_separator("-")
    print(f"📄 输入论文: {paper_path}")
    print(f"⏱️  总耗时: {duration:.2f} 秒 ({duration/60:.1f} 分钟)")
    print(f"📁 输出目录: {dirs['base']}")
    
    # 统计处理结果
    success_count = sum(1 for result in processed_results.values() if result['status'] == 'success')
    total_count = len(processed_results)
    
    print(f"\n📊 Agent处理统计:")
    print(f"   总计: {total_count} 个Agent")
    print(f"   成功: {success_count} 个")
    print(f"   失败: {total_count - success_count} 个")
    
    for agent_name, result in processed_results.items():
        status = "✅" if result['status'] == 'success' else "❌"
        print(f"   {status} {agent_name} Agent")
    
    print(f"\n📂 生成的文件结构:")
    print(f"   ├── 📁 sections/ (论文章节切分)")
    print(f"   ├── 📁 intro_agent_output/ (Introduction处理结果)")
    print(f"   ├── 📁 method_agent_output/ (Methods处理结果)")
    print(f"   ├── 📁 experiment_agent_output/ (Experiments处理结果)")
    print(f"   ├── 📁 conclusion_agent_output/ (Conclusion处理结果)")
    print(f"   └── 📁 final_results/ (整理后的最终结果)")
    
    print_separator("=")

def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="EduAgent Master Pipeline - 学术论文到教学视频的完整自动化处理",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
    python master_pipeline.py paper/ChatDev.md ./ChatDev_images
    python master_pipeline.py paper/ChatDev.md ./images --output-base-dir ./output
        """
    )
    
    parser.add_argument(
        'paper_path',
        help='输入的学术论文Markdown文件路径'
    )
    
    parser.add_argument(
        'images_dir',
        help='图片目录路径'
    )
    
    parser.add_argument(
        '--output-base-dir',
        default='./master_output',
        help='输出基础目录路径 (默认: ./master_output)'
    )
    
    args = parser.parse_args()
    
    start_time = time.time()
    
    try:
        print_header()
        print(f"📄 输入论文: {args.paper_path}")
        print(f"📷 图片目录: {args.images_dir}")
        print(f"📁 输出目录: {args.output_base_dir}")
        print_separator("=")
        
        # 验证输入
        validate_inputs(args.paper_path, args.images_dir)
        
        # 设置目录结构
        dirs = setup_master_directories(args.paper_path, args.output_base_dir)
        
        # 执行主流程
        section_files = step1_section_splitting(args.paper_path, dirs['sections'])
        processed_results = step2_process_agents(section_files, args.images_dir, dirs)
        collected_files = step3_collect_results(processed_results, dirs['final_results'])
        
        # 打印最终总结
        print_final_summary(dirs, args.paper_path, processed_results, start_time)
        
        # 统一的人机交互
        step4_interactive_editor(collected_files)
        
        print("\n🎉 所有流程完成！感谢使用 EduAgent Master Pipeline！")
        
    except KeyboardInterrupt:
        print("\n⚠️ 用户中断了Pipeline执行")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Pipeline执行失败: {str(e)}")
        print("请检查错误信息并重试")
        sys.exit(1)

if __name__ == "__main__":
    main() 