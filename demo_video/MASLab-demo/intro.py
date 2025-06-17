from manim import *

class PaperIntro(Scene):
    def construct(self):

        title = Text("Introduction", font_size=50)
        self.play(FadeIn(title))
        self.wait(2)
        self.play(FadeOut(title))

        # 2. Motivation: Limitations of Single LLMs with background
        motiv_bg = Text("LLMs power countless applications, yet struggle with reliability.", font_size=24, slant=ITALIC)
        motiv_bg.move_to(ORIGIN)
        self.play(Write(motiv_bg))
        self.wait(1)
        self.play(FadeOut(motiv_bg))

        motiv_title = Text("Motivation: Limitations of Single LLMs", font_size=36)
        motivations = BulletedList(
            "Remarkable success and broad applications of LLMs",
            "Unreliable and random generation",
            "Hallucinations",
            "Difficulty with complex, multi-step tasks",
            dot_scale_factor=1.2
        )
        group1 = VGroup(motiv_title, motivations).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        self.play(Write(motiv_title), FadeIn(motivations, shift=DOWN))
        self.wait(3)
        self.play(FadeOut(group1))

        # 3. Emergence of Multi-Agent Systems (MAS) with background
        mas_bg = Text("Enter MAS: collaborative agents designed to complement each other.", font_size=24, slant=ITALIC)
        mas_bg.move_to(UP * 2.5)
        self.play(Write(mas_bg))
        self.wait(1)

        circle = Circle(radius=0.7, color=BLUE).shift(LEFT * 2)
        circle_text = Text("LLM", font_size=24).move_to(circle.get_center())
        square = Square(side_length=1.4, color=GREEN).shift(RIGHT * 2)
        square_text = Text("MAS", font_size=24).move_to(square.get_center())
        arrow = Arrow(start=circle.get_right(), end=square.get_left(), buff=0.1)
        diagram = VGroup(circle, circle_text, square, square_text, arrow)
        self.play(Create(circle), Write(circle_text))
        self.play(Create(arrow))
        self.play(Create(square), Write(square_text))
        self.wait(2)
        self.play(FadeOut(mas_bg), FadeOut(diagram))


        mas_title = Text("LLM-based Multi-Agent Systems (MAS)", font_size=36)
        mas_points = BulletedList(
            "Multiple agents with distinct roles and contexts",
            "Collaborative solving of complex tasks",
            "Applications: code generation, math problem-solving, research, data synthesis",
            dot_scale_factor=1.2
        ).scale(0.75)
        group2 = VGroup(mas_title, mas_points).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        self.play(Write(mas_title), FadeIn(mas_points, shift=DOWN))
        self.wait(3)
        self.play(FadeOut(group2))

        # 4. Challenges in the Field with background
        chal_bg = Text("Yet, MAS research remains scattered across isolated repos.", font_size=24, slant=ITALIC)
        chal_bg.move_to(ORIGIN)
        self.play(Write(chal_bg))
        self.wait(1)
        self.play(FadeOut(chal_bg))

        chal_title = Text("Challenges: Lack of Unified Codebase", font_size=36)
        challenges = BulletedList(
            "Redundant implementation effort",
            "Unfair comparisons across varied codebases",
            "High entry barrier for newcomers",
            dot_scale_factor=1.2
        )
        group3 = VGroup(chal_title, challenges).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        self.play(Write(chal_title), FadeIn(challenges, shift=DOWN))
        self.wait(3)
        self.play(FadeOut(group3))

        # 5. MASLab Contributions with background
        contrib_bg = Text("Our solution: a unified, standardized framework.", font_size=24, slant=ITALIC)
        contrib_bg.move_to(UP * 2.5)
        self.play(Write(contrib_bg))
        self.wait(1)

        image = ImageMobject("images/496ce22754d7598012e9454bfca972cb509eab51f39fcf42d0319d9fe0ac2a22.jpg")
        image.scale(0.95)
        self.play(FadeIn(image))
        self.wait(3)
        self.play(FadeOut(image),FadeOut(contrib_bg))

        contrib_title = Text("MASLab: Our Contributions", font_size=36)
        contributions = BulletedList(
            "Unified codebase integrating 20+ established MAS methods",
            "Standardized evaluations on diverse benchmarks",
            "Streamlined high-level structure for easy extension",
            dot_scale_factor=1.2
        )
        group4 = VGroup(contrib_title, contributions).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        self.play(Write(contrib_title), FadeIn(contributions, shift=DOWN))
        self.wait(3)
        self.play(FadeOut(group4))
