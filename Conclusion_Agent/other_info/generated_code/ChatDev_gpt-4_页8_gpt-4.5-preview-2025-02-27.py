from manim import *

class InceptionPrompting(Scene):
    def construct(self):
        title = Text("Inception Prompting Mechanism in ChatDev", font_size=30).to_edge(UP)
        self.play(Write(title))

        intro_text = Text(
            "ChatDev employs inception prompting for:", font_size=24
        ).next_to(title, DOWN, buff=0.5)

        bullet_points = VGroup(
            Text("• initiating agent communication", font_size=22),
            Text("• sustaining agent communication", font_size=22),
            Text("• concluding agent communication", font_size=22),
            Text("to ensure robust and efficient workflow.", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT).next_to(intro_text, DOWN, buff=0.3)

        self.play(FadeIn(intro_text), FadeIn(bullet_points))

        prompt_box = RoundedRectangle(height=3.5, width=5.5, corner_radius=0.2, color=BLUE)
        prompt_box.next_to(bullet_points, DOWN, buff=0.5)

        pi_text = MathTex(r"\mathsf{P}_I", font_size=24, color=YELLOW).move_to(prompt_box.get_left()+ LEFT*0.7 + UP)
        pa_text = MathTex(r"\mathsf{P}_A", font_size=24, color=GREEN).move_to(prompt_box.get_left()+ LEFT*0.7 + DOWN)

        prompts_symmetrical = Text("Symmetrical Prompts", font_size=22).next_to(prompt_box.get_top(), DOWN, buff=0.2)

        prompt_details = VGroup(
            Text("- Subtask Overview & Objectives", font_size=18),
            Text("- Specialized Roles", font_size=18),
            Text("- Accessible External Tools", font_size=18),
            Text("- Communication Protocols", font_size=18),
            Text("- Termination Conditions", font_size=18),
            Text("- Constraints (avoid undesirable behaviors)", font_size=18),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to(prompt_box.get_center())

        self.play(FadeIn(prompt_box), Write(prompts_symmetrical))
        self.play(Write(prompt_details))
        self.play(Write(pi_text), Write(pa_text))

        agents_text = Text("Instantiate Agents via Hypnotizing LLMs:", font_size=22).next_to(prompt_box, DOWN, buff=0.5)
        agents_formula = MathTex(r"\mathcal{T} \leftarrow \mathsf{P}_I, \quad \mathcal{A} \leftarrow \mathsf{P}_A", font_size=26).next_to(agents_text, DOWN, buff=0.3)

        self.play(FadeIn(agents_text), Write(agents_formula))

        self.wait(2)
        self.wait(31.20)
        self.play(FadeOut(*self.mobjects))