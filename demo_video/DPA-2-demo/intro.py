from manim import *

class DPA2Overview(Scene):
    def construct(self):
        # Title
        title = Text("Understanding DPA-2: A Large Atomic Model", font_size=36, color=WHITE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # I. Background
        background = Text("I. Background: PES is key for simulations", font_size=30, color=WHITE).shift(UP * 2)
        qm = Text("Quantum Methods: Accurate but Slow", font_size=24, color=WHITE).shift(UP * 1)
        eff = Text("Empirical Force Fields: Fast but Inaccurate", font_size=24, color=WHITE).shift(DOWN * 1)
        arrow = Arrow(start=qm.get_bottom(), end=eff.get_top(), buff=0.2, color=WHITE)
        self.play(Write(background))
        self.wait(0.5)
        self.play(FadeIn(qm), FadeIn(eff), GrowArrow(arrow))
        self.wait(2)
        self.play(FadeOut(background), FadeOut(qm), FadeOut(eff), FadeOut(arrow))

        # II. Challenges
        challenges = Text("II. Challenges", font_size=30, color=WHITE).shift(UP * 2)
        dft_cost = Text("DFT labeling is expensive", font_size=24, color=WHITE).shift(UP * 0.7)
        generalization = Text("MLPs have poor generalization", font_size=24, color=WHITE).shift(DOWN * 0.7)
        self.play(Write(challenges))
        self.wait(0.5)
        self.play(FadeIn(dft_cost), FadeIn(generalization))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in [challenges, dft_cost, generalization]])

        # III. Training Strategies
        strategy_title = Text("III. Single-task vs Multi-task Training", font_size=30, color=WHITE).shift(UP * 2)
        single = Text("Single-task", font_size=24, color=WHITE).shift(LEFT * 3)
        multi = Text("Multi-task", font_size=24, color=WHITE).shift(RIGHT * 3)
        box1 = Rectangle(width=3.5, height=1.2, color=WHITE).move_to(single)
        box2 = Rectangle(width=3.5, height=1.2, color=WHITE).move_to(multi)
        s_text = Text("More consistent, less flexible", font_size=20).move_to(single).shift(DOWN * 1.5)
        m_text = Text("More general, adaptable to tasks", font_size=20).move_to(multi).shift(DOWN * 1.5)
        self.play(Write(strategy_title))
        self.wait(0.5)
        self.play(FadeIn(box1), FadeIn(box2), FadeIn(single), FadeIn(multi))
        self.play(Write(s_text), Write(m_text))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in [strategy_title, single, multi, box1, box2, s_text, m_text]])

        # IV. Requirements for LAMs
        req_title = Text("IV. What Makes a Good LAM?", font_size=30, color=WHITE).shift(UP * 2)
        bullet_list = BulletedList(
            "1. High generalizability",
            "2. Symmetry: translation, rotation, permutation",
            "3. Energy conservation: forces from gradients",
            "4. Smoothness: up to 2nd-order derivatives",
            font_size=24,
            color=WHITE
        )
        self.play(Write(req_title))
        self.wait(0.5)
        self.play(FadeIn(bullet_list))
        self.wait(3)
        self.play(FadeOut(req_title), FadeOut(bullet_list))

        # V. DPA-2 Contribution
        dpa_title = Text("V. DPA-2 Contributions", font_size=30, color=WHITE).shift(UP * 2)
        dpa_summary = BulletedList(
            "Fulfills key LAM requirements",
            "Trained on diverse tasks and systems",
            "Applicable to materials, drugs, batteries",
            "Captures deep chemical representation",
            font_size=24,
            color=WHITE
        )
        self.play(Write(dpa_title))
        self.wait(0.5)
        self.play(FadeIn(dpa_summary))
        self.wait(3)
        self.play(FadeOut(dpa_title), FadeOut(dpa_summary))

        # Ending
        end_text = Text("DPA-2: A foundation for universal ML potentials", font_size=28, color=WHITE)
        self.play(Write(end_text))
        self.wait(3)
