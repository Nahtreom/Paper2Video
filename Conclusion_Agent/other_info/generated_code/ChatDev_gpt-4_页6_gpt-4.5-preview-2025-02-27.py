from manim import *

class DualAgentCommunication(Scene):
    def construct(self):
        title = Text("Dual-Agent Communication Design", font_size=30).to_edge(UP)
        self.play(Write(title))

        step1 = Text("Simplifies communications by avoiding complex multi-agent topologies.", font_size=24)
        step2 = Text("Previous task's solutions bridge smoothly to the next phase.", font_size=24)
        step3 = Text("Chain-style structure guides agents clearly on communication.", font_size=24)
        step4 = Text("Transparent view allows examining intermediate solutions.", font_size=24)

        steps_group = VGroup(step1, step2, step3, step4).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(title, DOWN, buff=0.6)

        rect1 = SurroundingRectangle(step1, color=BLUE)
        rect2 = SurroundingRectangle(step2, color=GREEN)
        rect3 = SurroundingRectangle(step3, color=ORANGE)
        rect4 = SurroundingRectangle(step4, color=PURPLE)

        self.play(FadeIn(step1), Create(rect1))
        self.wait(1.5)

        self.play(FadeIn(step2), ReplacementTransform(rect1, rect2))
        self.wait(1.5)

        self.play(FadeIn(step3), ReplacementTransform(rect2, rect3))
        self.wait(1.5)

        self.play(FadeIn(step4), ReplacementTransform(rect3, rect4))
        self.wait(1.5)

        benefits = BulletedList(
            "Effective consensus",
            "Smooth subtask transitions",
            "Enhanced cooperation",
            "Transparent and trackable process",
            font_size=24
        ).next_to(steps_group, DOWN, buff=0.8)

        self.play(FadeIn(benefits))
        self.wait(2)
        self.wait(15.96)
        self.play(FadeOut(*self.mobjects))