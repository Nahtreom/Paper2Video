from manim import *

class AgenticWorkflowScene(Scene):
    def construct(self):
        title = Text("Agentic Task-Solving Formulation", font_size=30).to_edge(UP)
        self.play(Write(title))

        formulation = MathTex(
            r"\mathcal{C} &= \langle \mathcal{P}^{1}, \mathcal{P}^{2}, \dotsc, \mathcal{P}^{|\mathcal{C}|} \rangle \\",
            r"\mathcal{P}^{i} &= \langle \mathcal{T}^{1}, \mathcal{T}^{2}, \dotsc, \mathcal{T}^{|\mathcal{P}^{i}|} \rangle \\",
            r"\mathcal{T}^{j} &= \tau\left(\mathsf{C}(\mathbb{Z}, \mathcal{A})\right)\\",
            r"\mathsf{C}(\mathbb{Z}, \mathcal{A}) &= \langle \mathbb{Z}\mathcal{A}, \mathcal{A}\mathbb{Z} \rangle_{\odot}"
        ).scale(0.8).next_to(title, DOWN, buff=0.8)

        box1 = SurroundingRectangle(formulation[0], color=BLUE, buff=0.15)
        box2 = SurroundingRectangle(formulation[1], color=GREEN, buff=0.15)
        box3 = SurroundingRectangle(formulation[2], color=ORANGE, buff=0.15)
        box4 = SurroundingRectangle(formulation[3], color=RED, buff=0.15)

        self.play(Write(formulation[0]))
        self.play(FadeIn(box1))
        self.wait(0.5)

        self.play(Write(formulation[1]))
        self.play(FadeIn(box2))
        self.wait(0.5)

        self.play(Write(formulation[2]))
        self.play(FadeIn(box3))
        self.wait(0.5)

        self.play(Write(formulation[3]))
        self.play(FadeIn(box4))

        self.wait(2)
        self.wait(10.78)
        self.play(FadeOut(*self.mobjects))