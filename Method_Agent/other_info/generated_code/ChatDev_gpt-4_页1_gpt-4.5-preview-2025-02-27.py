from manim import *

class ChatDevIntro(Scene):
    def construct(self):
        title = Text("ChatDev: Chat-powered Software Development Framework", font_size=30).to_edge(UP)

        phases = VGroup(
            Rectangle(width=2.5, height=1, color=BLUE).set_fill(BLUE, opacity=0.2).shift(LEFT*4),
            Rectangle(width=2.5, height=1, color=BLUE).set_fill(BLUE, opacity=0.2).shift(LEFT*1.3),
            Rectangle(width=2.5, height=1, color=BLUE).set_fill(BLUE, opacity=0.2).shift(RIGHT*1.4),
            Rectangle(width=2.5, height=1, color=BLUE).set_fill(BLUE, opacity=0.2).shift(RIGHT*4),
        )
        phases_labels = VGroup(
            Text("Requirement", font_size=20).move_to(phases[0]),
            Text("Design", font_size=20).move_to(phases[1]),
            Text("Implementation", font_size=20).move_to(phases[2]),
            Text("Testing", font_size=20).move_to(phases[3]),
        )
        phases_group = VGroup(phases, phases_labels).shift(UP*0.7)

        arrows = VGroup(
            Arrow(phases[0].get_right(), phases[1].get_left(), buff=0.1),
            Arrow(phases[1].get_right(), phases[2].get_left(), buff=0.1),
            Arrow(phases[2].get_right(), phases[3].get_left(), buff=0.1),
        )

        roles = BulletedList(
            "Requirement analysts",
            "Professional programmers",
            "Test engineers",
            font_size=22
        ).to_edge(LEFT, buff=1).shift(DOWN*1)

        chat_chain_box = RoundedRectangle(width=5.5, height=1.2, color=GREEN).set_fill(GREEN, opacity=0.2).to_edge(RIGHT, buff=1).shift(DOWN*1)
        chat_chain_label = Text("Chat Chain: Split phases into subtasks\nmulti-turn communications", font_size=20).move_to(chat_chain_box)

        dehallucination = Text(
            "Communicative Dehallucination:\nAgents request detailed information\nbefore responding directly",
            font_size=20
        ).to_edge(DOWN, buff=0.5)

        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeIn(phases_group, arrows))
        self.wait(0.5)
        self.play(FadeIn(roles))
        self.wait(1)
        self.play(FadeIn(chat_chain_box), Write(chat_chain_label))
        self.wait(1)
        self.play(Write(dehallucination))
        self.wait(2)