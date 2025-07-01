from manim import *

class ChatDevExplanation(Scene):
    def construct(self):
        title = Text("ChatDev: Subtask Communication Efficiency", font_size=30).to_edge(UP)
        self.play(Write(title))

        statement = Text(
            "By sharing solutions to each subtask rather\n"
            "than full communication history, ChatDev:",
            font_size=26,
            line_spacing=1.2
        ).next_to(title, DOWN, buff=0.8)

        self.play(FadeIn(statement))

        points = VGroup(
            Text("• Minimizes information overload", font_size=24),
            Text("• Enhances concentration on individual tasks", font_size=24),
            Text("• Encourages targeted cooperation", font_size=24),
            Text("• Facilitates cross-phase context continuity", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(statement, DOWN, buff=0.6)

        for item in points:
            self.play(Write(item), run_time=1.5)

        diagram = VGroup(
            Rectangle(width=2.5, height=1.5).set_stroke(color=BLUE),
            Text("Subtask 1\nSolution", font_size=20)
        ).arrange(DOWN, buff=0.1).to_edge(DOWN, buff=0.8).shift(LEFT * 3)

        arrow = Arrow(start=diagram.get_right(), end=diagram.get_right()+RIGHT*2, stroke_width=2)

        diagram2 = VGroup(
            Rectangle(width=2.5, height=1.5).set_stroke(color=GREEN),
            Text("Subtask 2\nSolution", font_size=20)
        ).arrange(DOWN, buff=0.1).next_to(arrow, RIGHT)

        self.play(FadeIn(diagram), FadeIn(diagram2), GrowArrow(arrow))

        self.wait(1)
        self.wait(11.76)
        self.play(FadeOut(*self.mobjects))