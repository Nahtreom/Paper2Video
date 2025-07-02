import re
import sys
import ast

def get_indentation(file_path):
    """
    获取文件最后一个非空行的缩进
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 从后向前查找最后一个非空行
        for line in reversed(lines):
            if line.strip():
                # 计算前导空格数量
                return len(line) - len(line.lstrip())
        return 0
    except Exception:
        return 0

def extract_animation_times(file_path):
    """
    从manim代码文件中提取所有self.wait()和self.play()调用的时间总和
    
    Args:
        file_path (str): manim代码文件的路径
    
    Returns:
        float: 所有动画和等待时间的总和
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        total_time = 0
        
        # 计算wait时间
        wait_pattern = r'self\.wait\((.*?)\)'
        wait_calls = re.findall(wait_pattern, content)
        
        for wait_arg in wait_calls:
            if not wait_arg:  # 如果wait()没有参数
                total_time += 1  # 默认等待时间为1秒
            else:
                try:
                    # 尝试评估参数（处理数字表达式）
                    wait_time = eval(wait_arg)
                    total_time += float(wait_time)
                except:
                    print(f"警告：无法解析等待时间参数: {wait_arg}")
                    continue
        
        # 计算play次数
        play_pattern = r'self\.play\('
        play_calls = re.findall(play_pattern, content)
        total_time += len(play_calls)  # 每个play算作1秒
        
        return total_time
    
    except FileNotFoundError:
        print(f"错误：找不到文件 {file_path}")
        return None
    except Exception as e:
        print(f"错误：处理文件时发生错误: {str(e)}")
        return None

def add_wait_time(file_path, additional_time):
    """
    在文件末尾添加额外的wait时间和FadeOut效果
    """
    try:
        # 获取当前文件的缩进
        indent = get_indentation(file_path)
        indent_str = " " * indent
        
        # 在文件末尾添加wait语句和FadeOut效果
        with open(file_path, 'a') as f:
            f.write(f"\n{indent_str}self.wait({additional_time:.2f})")
            f.write(f"\n{indent_str}self.play(FadeOut(*self.mobjects))")
        
        print(f"已在文件末尾添加：")
        print(f"1. self.wait({additional_time:.2f})")
        print(f"2. self.play(FadeOut(*self.mobjects))")
        return True
    except Exception as e:
        print(f"错误：添加动画效果时发生错误: {str(e)}")
        return False

def main():
    if len(sys.argv) != 3:
        print("用法: python wait_time_calculator.py <目标时长（秒）> <manim文件路径>")
        sys.exit(1)
    
    try:
        target_duration = float(sys.argv[1])
        file_path = sys.argv[2]
        
        total_time = extract_animation_times(file_path)
        
        if total_time is not None:
            print(f"\n分析结果：")
            print(f"总时长 (wait + play): {total_time:.2f} 秒")
            print(f"目标时长: {target_duration:.2f} 秒")
            difference = target_duration - total_time - 1  
            print(f"时间差值: {difference:.2f} 秒")
            
            if difference > 0:
                print(f"建议：需要增加 {difference:.2f} 秒的时间")
                # 自动添加额外的wait时间和FadeOut效果
                if add_wait_time(file_path, difference):
                    print("✓ 已自动添加所需的等待时间和淡出效果")
            elif difference < 0:
                print(f"建议：需要减少 {abs(difference):.2f} 秒的时间")
            else:
                print("完美匹配！当前总时长正好达到目标时长")
    
    except ValueError:
        print("错误：目标时长必须是一个有效的数字")
        sys.exit(1)

if __name__ == "__main__":
    main() 