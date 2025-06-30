from manim import *

class ChatDevIntro(Scene):
    def construct(self):
        title = Text("ChatDev: A Chat-powered Software Development Framework", font_size=30).to_edge(UP)
        self.play(Write(title))

        description = Text(
            "Multiple software agents collaborate with social roles:\n"
            "Requirements analysts, Professional programmers, Test engineers", font_size=24
        ).next_to(title, DOWN, buff=0.5)

        self.play(FadeIn(description))

        rect_chain = Rectangle(width=5, height=1, color=BLUE)
        chat_chain_text = Text("Chat chain for subtasks decomposition", font_size=22).move_to(rect_chain.get_center())
        chat_chain = VGroup(rect_chain, chat_chain_text).next_to(description, DOWN, buff=0.5)

        self.play(FadeIn(chat_chain))

        rect_com = Rectangle(width=5, height=1, color=GREEN)
        com_text = Text("Communicative Dehallucination:\n"
                        "Agents request detailed info before responding", font_size=22).move_to(rect_com.get_center())
        com_pattern = VGroup(rect_com, com_text).next_to(chat_chain, DOWN, buff=0.5)

        self.play(FadeIn(com_pattern))

        img = ImageMobject("ChatDev_images/79021ce9de0bd97d75fc696a609821851154d2323b1123cd2b2b71870afbd198.jpg")
        img.scale(0.7).next_to(com_pattern, DOWN, buff=0.5)

        self.play(FadeIn(img))

        self.wait(2)