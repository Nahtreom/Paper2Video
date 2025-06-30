from manim import *

class ChatDevFramework(Scene):
    def construct(self):
        title = Text("ChatDev: Chat-Powered Software Development Framework", font_size=30).to_edge(UP)
        self.play(FadeIn(title))

        image = ImageMobject("ChatDev_images/79021ce9de0bd97d75fc696a609821851154d2323b1123cd2b2b71870afbd198.jpg")
        image.scale(0.7).next_to(title, DOWN)

        caption = Text(
            "Figure 1: ChatDev integrates LLM agents with social roles,\ncollaborating autonomously on software solutions.",
            font_size=22
        ).next_to(image, DOWN)

        self.play(FadeIn(image))
        self.play(Write(caption))

        self.wait(2)
        self.wait(14.00)
        self.play(FadeOut(*self.mobjects))