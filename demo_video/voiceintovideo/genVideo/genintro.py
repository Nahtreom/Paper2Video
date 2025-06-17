from manim import *
from moviepy.editor import VideoFileClip
import os

def get_audio_duration(video_path):
    try:
        # 获取绝对路径
        abs_path = os.path.abspath(video_path)
        print(f"正在读取: {abs_path}")
        # 加载视频文件
        clip = VideoFileClip(abs_path)
        # 检查是否有音频轨道
        if clip.audio:
            duration = clip.audio.duration
            print(f"音频时长: {duration:.2f} 秒")
        else:
            print("警告: 未检测到音频轨道")
            duration = 10
            
        clip.close()
        return duration
    except Exception as e:
        print(f"错误: {e}")
        return 10  # 默认返回值
    
class Scene1(Scene):
    def construct(self):
        audio_path = "voice1.mp4"
        duration = get_audio_duration(audio_path)
        title = Text("Introduction", font_size=50)
        self.play(FadeIn(title))
        self.wait(duration)
        # self.play(FadeOut(title))

class Scene2(Scene):
    def construct(self):
        audio_path = "voice2.mp4"
        duration = get_audio_duration(audio_path)
        motiv_bg = Text("LLMs power countless applications, yet struggle with reliability.", font_size=24, slant=ITALIC)
        motiv_bg.move_to(ORIGIN)
        self.play(Write(motiv_bg))
        self.wait(duration)
        # self.play(FadeOut(motiv_bg))

class Scene3(Scene):
    def construct(self):
        motiv_title = Text("Motivation: Limitations of Single LLMs", font_size=36)
        motivations = Text(
            "- Remarkable success and broad applications of LLMs\n"
            "- Unreliable and random generation\n"
            "- Hallucinations\n"
            "- Difficulty with complex, multi-step tasks",
            font_size=24
        )
        motiv_title.to_edge(UP)
        motivations.next_to(motiv_title, DOWN)
        self.play(Write(motiv_title))
        self.play(Write(motivations))
        self.wait()