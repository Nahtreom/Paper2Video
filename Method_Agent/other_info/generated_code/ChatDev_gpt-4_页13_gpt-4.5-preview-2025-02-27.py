from manim import *

class DialogueMemory(Scene):
    def construct(self):
        title = Text("Perceiving Dialogues through Phases", font_size=30).to_edge(UP)
        self.play(Write(title))

        intro_text = Text(
            "Chat chain transmits solutions as long-term memories", font_size=24
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))

        memory_eq1 = MathTex(
            r"\mathcal{I}_{1}^{i+1} = \tilde{\mathcal{M}}^{i} \cup \mathsf{P}_{\mathcal{Z}}^{i+1}"
        ).next_to(intro_text, DOWN, buff=0.7)

        memory_eq2 = MathTex(
            r"\tilde{\mathcal{M}}^{i} = \bigcup_{j=1}^{i}\tau(\mathcal{M}_{|\mathcal{M}^{j}|}^{j})"
        ).next_to(memory_eq1, DOWN, buff=0.5)

        self.play(FadeIn(memory_eq1))
        self.wait(1)
        self.play(FadeIn(memory_eq2))
        self.wait(1)

        prompt_explain = Text(
            r"Here, $\mathsf{P}$ is a predetermined prompt at each phase start.",
            font_size=22,
        ).next_to(memory_eq2, DOWN, buff=0.8)
        self.play(Write(prompt_explain))

        box = SurroundingRectangle(memory_eq1, color=YELLOW, buff=0.2)
        self.play(Create(box))

        self.wait(4)
        self.wait(10.68)
        self.play(FadeOut(*self.mobjects))