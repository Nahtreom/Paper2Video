from manim import *

class DehallucinationConcept(Scene):
    def construct(self):
        title = Text("Communicative Dehallucination", font_size=30).to_edge(UP)
        self.play(Write(title))

        explanation = Text(
            "Coding hallucinations occur when instructions are vague or\n"
            "general, making precise compliance difficult for agents.",
            font_size=24
        ).next_to(title, DOWN, buff=0.5)

        self.play(FadeIn(explanation))

        issue_box = RoundedRectangle(width=6.5, height=1.2, corner_radius=0.15).next_to(explanation, DOWN, buff=0.5)
        issue_text = Text("Issue: Agent struggles with unclear instructions", font_size=22).move_to(issue_box.get_center())
        self.play(FadeIn(issue_box), Write(issue_text))

        arrow = Arrow(start=issue_box.get_bottom(), end=issue_box.get_bottom() + DOWN*1.2)
        self.play(GrowArrow(arrow))

        solution_box = RoundedRectangle(width=7, height=1.5, corner_radius=0.15, color=GREEN).next_to(arrow, DOWN)
        solution_text = Text("Proposed Method:\nCommunicative Dehallucination", font_size=22).move_to(solution_box.get_center())
        self.play(FadeIn(solution_box), Write(solution_text))

        detail_explain = Text(
            "Assistant proactively requests more detailed suggestions\n"
            "before providing formal responses.",
            font_size=22,
            color=YELLOW
        ).next_to(solution_box, DOWN, buff=0.5)

        self.play(FadeIn(detail_explain))

        self.wait(2)
        self.wait(18.92)
        self.play(FadeOut(*self.mobjects))