from manim import *

class Page15(Scene):
    def construct(self):
        title = Text("LLM Hallucinations in Software Development", font_size=30).to_edge(UP)
        self.play(Write(title))

        definition_text = Text(
            "Hallucinations occur when LLMs generate outputs that are:\n"
            "- Nonsensical\n"
            "- Factually incorrect\n"
            "- Inaccurate",
            font_size=28,
            line_spacing=0.5
        ).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(definition_text, shift=DOWN))

        consequence_text = Text(
            "Impact in Software Development:",
            font_size=28
        ).next_to(definition_text, DOWN, buff=0.5).shift(LEFT * 2.5)
        self.play(Write(consequence_text))

        consequences = BulletedList(
            "Incomplete implementations",
            "Unexecutable code snippets",
            "Requirement inconsistencies",
            font_size=26,
            dot_scale_factor=0.5
        ).next_to(consequence_text, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(consequences, shift=RIGHT))

        warning = Text(
            "One line of inaccurate code can cause system failures.",
            font_size=26,
            color=RED
        ).next_to(consequences, DOWN, buff=0.6)
        self.play(Write(warning))

        self.wait(2)
        self.wait(28.04)
        self.play(FadeOut(*self.mobjects))