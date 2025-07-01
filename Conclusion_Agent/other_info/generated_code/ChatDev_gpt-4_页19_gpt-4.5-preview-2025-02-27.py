from manim import *

class CommunicationMechanism(Scene):
    def construct(self):
        title = Text("Communication Mechanism for Optimization", font_size=30).to_edge(UP)
        self.play(Write(title))
        
        explanation_1 = Text(
            "Solves one concrete issue at a time",
            font_size=26
        ).next_to(title, DOWN, buff=0.8)

        self.play(FadeIn(explanation_1))

        arrow_down = Arrow(start=explanation_1.get_bottom(), end=explanation_1.get_bottom() + DOWN*1.2)
        self.play(GrowArrow(arrow_down))

        explanation_2 = Text(
            "Needs multiple rounds of communication",
            font_size=26
        ).next_to(arrow_down, DOWN, buff=0.2)

        self.play(FadeIn(explanation_2))

        arrow_down_2 = Arrow(start=explanation_2.get_bottom(), end=explanation_2.get_bottom() + DOWN*1.2)
        self.play(GrowArrow(arrow_down_2))

        explanation_3 = VGroup(
            Text("Fine-grained information exchange", font_size=26),
            Text("Optimizes potential problems efficiently", font_size=26)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(arrow_down_2, DOWN, buff=0.2)

        self.play(FadeIn(explanation_3))

        box = SurroundingRectangle(explanation_3, color=BLUE, buff=0.2)
        self.play(Create(box))

        explanation_4 = Text(
            "Practically reduces coding hallucinations",
            font_size=26, color=YELLOW
        ).next_to(box, DOWN, buff=0.4)

        self.play(Write(explanation_4))

        self.wait(1)
        self.wait(8.40)
        self.play(FadeOut(*self.mobjects))