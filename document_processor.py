#!/usr/bin/env python3
"""
文档处理程序

简化版本：只需要输入markdown路径和输出目录，从config.json读取配置，从txt文件读取prompt
添加章节切分功能
"""

import os
import sys
import json
"""
文档处理程序

简化版本：只需要输入markdown路径和输出目录，从config.json读取配置，从txt文件读取prompt
添加章节切分功能
"""

import os
import sys
import json
import re
from api_call import process_text

def load_config():
    """从config.json加载配置"""
    config_file = "config.json"
    if not os.path.exists(config_file):
        # 创建默认配置文件（移除prompt_template_file配置项）
        default_config = {
            "api_key": "your-api-key-here",
            "model": "gpt-4.5-preview"
        }
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, ensure_ascii=False, indent=2)
        print(f"已创建默认配置文件 {config_file}，请修改其中的 api_key")
        sys.exit(1)
    
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # 检查必要的配置项
        if config.get("api_key") == "your-api-key-here":
            print("请在 config.json 中设置正确的 api_key")
            sys.exit(1)
            
        return config
    except Exception as e:
        print(f"读取配置文件失败: {e}")
        sys.exit(1)

def load_prompt_template() -> str:
    """从固定路径加载prompt模板"""
    template_file = "prompt_template/Central.txt"
    
    # 确保prompt_template目录存在
    template_dir = os.path.dirname(template_file)
    if not os.path.exists(template_dir):
        os.makedirs(template_dir, exist_ok=True)
        print(f"创建提示词目录: {template_dir}")
    
    if not os.path.exists(template_file):
        # 创建默认的prompt模板文件（使用Central.txt的内容）
        default_prompt = """你是一名学术写作助理，请你阅读以下完整文章内容，识别出其中属于以下四个部分的章节标题：

1.Introduction

2.方法（Methods / Methodology）

3.实验（Experiments / Experimental Setup / Evaluation）

4.结论（Conclusion / Discussion / Summary）

请你以如下格式输出每个部分对应的章节标题（只给出大标题即可哦～）：

Introduction: <对应章节标题>
Methods: <对应章节标题>
Experiments: <对应章节标题>
Conclusion: <对应章节标题>

以下是文章内容："""
        
        with open(template_file, 'w', encoding='utf-8') as f:
            f.write(default_prompt)
        print(f"已创建默认prompt模板文件: {template_file}")
    
    try:
        with open(template_file, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception as e:
        print(f"读取prompt模板文件失败: {e}")
        return "请分析以下学术论文内容并识别章节结构："

def read_file_content(file_path: str) -> str:
    """读取文件内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"文件未找到: {file_path}")
    except Exception as e:
        raise Exception(f"读取文件时出错: {str(e)}")

def parse_section_mapping(model_output: str) -> dict:
    """解析大模型输出的章节映射"""
    sections = {}
    lines = model_output.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if ':' in line:
            # 匹配格式如：Introduction: 1 Introduction
            parts = line.split(':', 1)
            if len(parts) == 2:
                section_type = parts[0].strip()
                original_section = parts[1].strip()
                sections[section_type] = original_section
    
    return sections

def extract_section_number(title_line: str) -> str:
    """从标题行中提取章节编号"""
    # 移除开头的#号和空格
    title_text = re.sub(r'^#+\s*', '', title_line).strip()
    # 提取开头的数字部分（可能包含小数点）
    match = re.match(r'^(\d+(?:\.\d+)*)', title_text)
    return match.group(1) if match else ""

def is_subsection(parent_num: str, current_num: str) -> bool:
    """判断current_num是否是parent_num的子章节"""
    if not parent_num or not current_num:
        return False
    
    # 如果current_num以parent_num开头且后面跟着小数点，则是子章节
    return current_num.startswith(parent_num + ".")

def find_section_content(markdown_content: str, section_identifier: str) -> str:
    """在markdown中找到指定章节的内容"""
    lines = markdown_content.split('\n')
    content_lines = []
    in_section = False
    found_line = None
    
    print(f"  正在搜索章节: '{section_identifier}'")
    
    # 创建多种可能的标题模式
    # 1. 直接匹配：# 1 Introduction
    pattern1 = rf'^#+\s*{re.escape(section_identifier)}\s*$'
    # 2. 包含匹配：# 任何内容 1 Introduction 任何内容
    pattern2 = rf'^#+\s*.*{re.escape(section_identifier)}.*$'
    # 3. 如果有数字开头，也尝试只匹配后面的文字部分
    section_text_only = re.sub(r'^\d+\s+', '', section_identifier).strip()
    pattern3 = rf'^#+\s*\d+\s+{re.escape(section_text_only)}\s*$' if section_text_only != section_identifier else None
    
    patterns = [pattern1, pattern2]
    if pattern3:
        patterns.append(pattern3)
    
    print(f"  使用的匹配模式:")
    for i, pattern in enumerate(patterns, 1):
        print(f"    模式{i}: {pattern}")
    
    # 搜索匹配的标题行
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        if line_stripped.startswith('#'):
            print(f"  检查第{i+1}行标题: '{line_stripped}'")
            
            # 检查是否匹配任何模式
            for j, pattern in enumerate(patterns):
                if re.match(pattern, line_stripped, re.IGNORECASE):
                    print(f"    ✓ 匹配成功 (模式{j+1})")
                    found_line = i
                    in_section = True
                    content_lines.append(line)
                    break
            
            if found_line is not None:
                break
    
    if found_line is None:
        print(f"  ✗ 未找到匹配的标题行")
        return ""
    
    print(f"  ✓ 找到起始行: 第{found_line+1}行")
    
    # 获取起始标题的级别和章节号
    start_title_level = len(re.match(r'^(#+)', lines[found_line]).group(1))
    start_section_number = extract_section_number(lines[found_line])
    print(f"  章节级别: {start_title_level} 级标题")
    print(f"  章节编号: '{start_section_number}'")
    
    # 从找到的行开始，收集内容直到下一个非子章节标题
    for i in range(found_line + 1, len(lines)):
        line = lines[i]
        
        # 检查是否是标题行
        if re.match(r'^#+\s*\S', line):  # # 后面可以没有空格，但必须有内容
            current_level = len(re.match(r'^(#+)', line).group(1))
            current_section_number = extract_section_number(line)
            print(f"    发现第{i+1}行标题: '{line.strip()}' (级别: {current_level}, 编号: '{current_section_number}')")
            
            # 判断是否应该停止收集
            should_stop = False
            
            if current_level < start_title_level:
                # 遇到更高级标题，停止
                should_stop = True
                print(f"    遇到更高级标题({current_level}级 < {start_title_level}级)，停止收集")
            elif current_level == start_title_level:
                # 同级标题，检查是否是子章节
                if start_section_number and current_section_number:
                    if is_subsection(start_section_number, current_section_number):
                        print(f"    这是子章节({current_section_number} 是 {start_section_number} 的子章节)，继续收集")
                    else:
                        should_stop = True
                        print(f"    这是同级或其他章节({current_section_number} 不是 {start_section_number} 的子章节)，停止收集")
                else:
                    # 无法判断章节号，按原逻辑处理
                    should_stop = True
                    print(f"    无法判断章节关系，按同级标题处理，停止收集")
            else:
                # 更低级标题，继续收集
                print(f"    这是更低级标题({current_level}级 > {start_title_level}级)，继续收集")
            
            if should_stop:
                print(f"  章节结束于第{i+1}行: '{line.strip()}'")
                break
        
        content_lines.append(line)
    
    result = '\n'.join(content_lines)
    print(f"  提取了 {len(content_lines)} 行内容")
    return result

def save_sections(sections: dict, markdown_content: str, output_dir: str, base_filename: str):
    """保存切分的章节到指定目录"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"创建输出目录: {output_dir}")
    
    saved_sections = []
    
    for section_type, section_identifier in sections.items():
        print(f"\n正在提取章节: {section_type} -> {section_identifier}")
        
        # 在markdown中找到对应的内容
        section_content = find_section_content(markdown_content, section_identifier)
        
        if section_content:
            # 构建文件名
            filename = f"{base_filename}_{section_type}.md"
            filepath = os.path.join(output_dir, filename)
            
            # 保存文件
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(section_content)
            
            print(f"✓ 已保存: {filepath}")
            saved_sections.append((section_type, filepath))
        else:
            print(f"✗ 警告: 未找到章节 '{section_identifier}' 的内容")
    
    return saved_sections

def process_document(markdown_path: str, output_dir: str, config: dict) -> str:
    """处理markdown文档"""
    
    # 检查文件是否存在
    if not os.path.exists(markdown_path):
        raise FileNotFoundError(f"Markdown 文件不存在: {markdown_path}")
    
    # 读取文档内容
    print(f"正在读取文档: {markdown_path}")
    document_content = read_file_content(markdown_path)
    
    # 加载prompt模板（使用固定路径）
    print(f"正在加载prompt模板: prompt_template/Central.txt")
    prompt_template = load_prompt_template()
    
    # 构建完整的prompt
    full_prompt = f"{prompt_template}\n\n\n{document_content}"
    
    # 调用API处理
    print(f"正在使用模型 {config['model']} 处理文档...")
    try:
        result = process_text(
            full_prompt, 
            config["api_key"], 
            config["model"]
        )
    except Exception as e:
        raise Exception(f"API 调用失败: {str(e)}")
    
    # 解析章节映射
    print("\n正在解析章节映射...")
    sections = parse_section_mapping(result)
    
    if sections:
        print(f"找到 {len(sections)} 个章节:")
        for section_type, section_id in sections.items():
            print(f"  {section_type}: {section_id}")
        
        # 切分并保存章节
        base_filename = os.path.splitext(os.path.basename(markdown_path))[0]
        
        print(f"\n正在切分文档到目录: {output_dir}")
        saved_sections = save_sections(sections, document_content, output_dir, base_filename)
        
        print(f"\n章节切分完成，共保存 {len(saved_sections)} 个文件")
    else:
        print("未找到有效的章节映射信息")
    
    return result

def main():
    """主函数"""
    if len(sys.argv) != 3:
        print("使用方法: python document_processor.py <markdown文件路径> <输出目录>")
        print("示例: python document_processor.py README.md ./sections")
        sys.exit(1)
    
    markdown_path = sys.argv[1]
    output_dir = sys.argv[2]
    
    try:
        # 加载配置
        config = load_config()
        
        # 处理文档
        result = process_document(markdown_path, output_dir, config)
        
        # 打印结果
        print("\n" + "="*80)
        print("大模型分析结果:")
        print("="*80)
        print(result)
        
    except Exception as e:
        print(f"错误: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 
