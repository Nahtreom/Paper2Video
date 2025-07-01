from manim import *

class MemoryTypesScene(Scene):
    def construct(self):
        title = Text("Handling Memory in Chat Chain", font_size=30).to_edge(UP)
        self.play(Write(title))

        issue_text = Text(
            "LLMs have limited context length,\npreventing full communication history.\nSolution: Segment memory by phases.",
            line_spacing=1.2,
            font_size=24
        ).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(issue_text))

        short_term_box = Rectangle(width=5.5, height=1.2, color=BLUE).next_to(issue_text, DOWN, buff=1.0).shift(LEFT*3)
        short_term_label = Text("Short-term Memory", font_size=22, color=BLUE).move_to(short_term_box.get_center())

        long_term_box = Rectangle(width=5.5, height=1.2, color=GREEN).next_to(short_term_box, DOWN, buff=0.7)
        long_term_label = Text("Long-term Memory", font_size=22, color=GREEN).move_to(long_term_box.get_center())

        short_term_desc = Text(
            "Sustains dialogue continuity\nwithin a single phase",
            font_size=20,
            line_spacing=1.2
        ).next_to(short_term_box, RIGHT, buff=0.5)

        long_term_desc = Text(
            "Preserves context awareness\nacross different phases",
            font_size=20,
            line_spacing=1.2
        ).next_to(long_term_box, RIGHT, buff=0.5)

        self.play(FadeIn(short_term_box), Write(short_term_label))
        self.play(Write(short_term_desc))

        self.play(FadeIn(long_term_box), Write(long_term_label))
        self.play(Write(long_term_desc))

        self.wait(2)
        self.wait(14.68)
        self.play(FadeOut(*self.mobjects))