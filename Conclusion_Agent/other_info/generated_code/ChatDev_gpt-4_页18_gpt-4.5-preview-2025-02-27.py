from manim import *

class CommunicativeDehallucination(Scene):
    def construct(self):
        title = Text("Communicative Dehallucination with Role Reversal", font_size=30).to_edge(UP)
        self.play(Write(title))

        assistant_role = Text("Assistant as Instructor-like Role", font_size=26, color=BLUE).next_to(title, DOWN, buff=0.6)
        self.play(FadeIn(assistant_role))

        explanation = Text(
            "Proactively asks precise external dependency information\n"
            "(e.g., exact name, related class)\nbefore delivering a response.",
            font_size=24,
            line_spacing=1.2
        ).next_to(assistant_role, DOWN, buff=0.5)
        self.play(Write(explanation))

        instructor_feedback = Text("Instructor provides specific modification suggestions", font_size=24, color=GREEN).next_to(explanation, DOWN, buff=0.6)
        self.play(FadeIn(instructor_feedback))

        optimization_action = Text("Assistant executes precise optimization", font_size=24).next_to(instructor_feedback, DOWN, buff=0.6)
        self.play(FadeIn(optimization_action))

        model_equation = MathTex(r"\langle \mathcal{T} \to \mathcal{A},"
                                 r"\langle \mathcal{A} \to \mathcal{I},"
                                 r"\mathcal{I}\sim\mathcal{A}\rangle_\odot,"
                                 r"\mathcal{A}\sim\mathcal{I}\rangle_\odot",
                                 font_size=32).next_to(optimization_action, DOWN, buff=0.6)
        self.play(Write(model_equation))

        self.wait(2)
        self.wait(15.60)
        self.play(FadeOut(*self.mobjects))