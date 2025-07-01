from manim import *

class RoleCustomizationScene(Scene):
    def construct(self):
        title = Text("Role Customization Operation", font_size=30).to_edge(UP)
        self.play(Write(title))

        formula_T = MathTex(r"\mathcal{T} = \rho(LLM, \mathsf{P}_I)").scale(1.2)
        formula_A = MathTex(r"\mathcal{A} = \rho(LLM, \mathsf{P}_A)").scale(1.2)
        formulas = VGroup(formula_T, formula_A).arrange(DOWN, buff=0.5).shift(UP * 0.5)

        rho_explain = Text(r"where $\rho$ is the role customization operation,",
                           font_size=24).next_to(formulas, DOWN, buff=0.7)
        rho_explain2 = Text(r"implemented via system message assignment.",
                            font_size=24).next_to(rho_explain, DOWN, buff=0.3)

        frame = SurroundingRectangle(formulas, color=BLUE)

        self.play(Write(formulas[0]))
        self.play(Write(formulas[1]))
        self.play(Create(frame))
        self.play(FadeIn(rho_explain), FadeIn(rho_explain2))

        self.wait(2)
        self.wait(8.92)
        self.play(FadeOut(*self.mobjects))