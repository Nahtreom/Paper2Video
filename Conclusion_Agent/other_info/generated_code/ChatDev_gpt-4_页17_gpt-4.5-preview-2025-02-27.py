from manim import *

class CommunicationPattern(Scene):
    def construct(self):
        title = Text("Vanilla Communication Pattern", font_size=30).to_edge(UP)
        self.play(Write(title))

        explanation = Text(
            "The communication pattern between\n"
            "the instructor (𝒯) and assistant (𝒜)\n"
            "follows a straightforward pattern:",
            font_size=24
        ).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(explanation))

        pattern = MathTex(
            r"\langle \mathcal{T} \to \mathcal{A}, \mathcal{A} \sim \mathcal{T}\rangle_{\mathcal{O}}",
            font_size=40
        ).next_to(explanation, DOWN, buff=0.5)
        self.play(Write(pattern))

        instructor_box = Rectangle(color=BLUE, height=1.0, width=2.5)
        instructor_label = Text("Instructor (𝒯)", font_size=20).move_to(instructor_box.get_center())
        instructor = VGroup(instructor_box, instructor_label).to_edge(LEFT, buff=1.5).shift(DOWN*1.5)

        assistant_box = Rectangle(color=GREEN, height=1.0, width=2.5)
        assistant_label = Text("Assistant (𝒜)", font_size=20).move_to(assistant_box.get_center())
        assistant = VGroup(assistant_box, assistant_label).to_edge(RIGHT, buff=1.5).shift(DOWN*1.5)

        arrow = Arrow(start=instructor_box.get_right(), end=assistant_box.get_left(), buff=0.1)
        response_arrow = Arrow(start=assistant_box.get_left(), end=instructor_box.get_right(), buff=0.1).shift(DOWN*0.5)

        self.play(FadeIn(instructor), FadeIn(assistant))
        self.play(GrowArrow(arrow))
        self.wait(0.2)
        self.play(GrowArrow(response_arrow))

        self.wait(2)
        self.wait(6.12)
        self.play(FadeOut(*self.mobjects))