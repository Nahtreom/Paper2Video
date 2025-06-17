from manim import *

class MASLabSummary(Scene):
    def construct(self):

        title = Text("Conclusion", font_size=50)
        self.play(FadeIn(title))
        self.wait(2)
        self.play(FadeOut(title))

        title = Text("MASLab: A Unified Codebase for MAS", font_size=45).to_edge(UP)

        bullet_points = BulletedList(
            "Integrates 20+ validated MAS methods",
            "Covers the full pipeline: data to evaluation",
            "Streamlined structure for easy development",
            "Benchmarks: 10+ tasks, 8 LLMs",
            "Analyzes protocol-induced ranking variance",
            "Open-source, evolving with the community",
            font_size=40
        ).next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeIn(bullet_points, shift=UP))
        self.wait(2)
