from manim import *

class MemoryUpdate(Scene):
    def construct(self):
        title = Text("Memory Iterative Update at Time Step t+1", font_size=30).to_edge(UP)
        self.play(Write(title))

        instructor = Rectangle(height=1, width=2, color=BLUE).shift(LEFT * 4 + UP)
        assistant = Rectangle(height=1, width=2, color=GREEN).shift(RIGHT * 4 + UP)
        instructor_label = Text("Instructor", font_size=24).next_to(instructor, UP)
        assistant_label = Text("Assistant", font_size=24).next_to(assistant, UP)

        memory_box = RoundedRectangle(height=1, width=5, color=ORANGE, corner_radius=0.2).shift(DOWN * 2)
        memory_label = Text("Short-Term Memory", font_size=24).next_to(memory_box, UP)

        self.play(FadeIn(instructor), FadeIn(instructor_label),
                  FadeIn(assistant), FadeIn(assistant_label),
                  FadeIn(memory_box), FadeIn(memory_label))

        instruction_arrow = Arrow(start=memory_box.get_top(), end=instructor.get_bottom(), color=BLUE)
        response_arrow = Arrow(start=instructor.get_right(), end=assistant.get_left(), color=GREEN)
        update_memory_arrow = Arrow(start=assistant.get_bottom(), end=memory_box.get_top(), color=ORANGE)

        instruction_eq = MathTex(
            r"\mathscr{T}_{t+1}^{i} = \mathscr{T}(\mathcal{M}_{t}^{i})", font_size=32
        ).next_to(instructor, DOWN)

        response_eq = MathTex(
            r"\mathscr{A}_{t+1}^{i} = \mathscr{A}(\mathcal{M}_{t}^{i}, \mathscr{T}_{t+1}^{i})", font_size=32
        ).next_to(assistant, DOWN)

        memory_update_eq = MathTex(
            r"\mathscr{M}_{t+1}^{i} = \mathscr{M}_{t}^{i} \cup (\mathscr{T}_{t+1}^{i}, \mathscr{A}_{t+1}^{i})",
            font_size=32
        ).next_to(memory_box, DOWN)

        self.play(FadeIn(instruction_arrow), Write(instruction_eq))
        self.play(FadeIn(response_arrow), Write(response_eq))
        self.play(FadeIn(update_memory_arrow), Write(memory_update_eq))

        self.wait(2)