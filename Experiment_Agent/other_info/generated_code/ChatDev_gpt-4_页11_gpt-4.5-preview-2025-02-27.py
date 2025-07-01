from manim import *

class ShortTermMemory(Scene):
    def construct(self):
        title = Text("Short-term Memory Representation", font_size=30).to_edge(UP)
        self.play(Write(title))

        description = Text(
            "Short-term memory records an agent's current phase utterances,\n"
            "aiding context-aware decision-making.",
            font_size=24,
            line_spacing=1.2
        ).next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(description))

        definitions = MathTex(r"""
            \text{At time } t \text{ during phase } \mathcal{P}^i,\quad
            \mathcal{T}_t^i:\text{ instructor's instruction}, \quad
            \mathcal{A}_t^i:\text{ assistant's response}
        """, font_size=26).next_to(description, DOWN, buff=0.5)
        self.play(Write(definitions))

        mem_box = SurroundingRectangle(definitions, color=BLUE, buff=0.2)
        self.play(Create(mem_box))

        memory_equation = MathTex(
            r"\mathcal{M}_t^i = \langle (\mathcal{T}_1^i, \mathcal{A}_1^i), (\mathcal{T}_2^i, \mathcal{A}_2^i), \dots, (\mathcal{T}_t^i, \mathcal{A}_t^i)\rangle",
            font_size=26
        ).next_to(mem_box, DOWN, buff=0.6)
        self.play(FadeIn(memory_equation))

        self.wait(3)
        self.wait(11.16)
        self.play(FadeOut(*self.mobjects))