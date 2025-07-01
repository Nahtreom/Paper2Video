from manim import *

class AgentizationScene(Scene):
    def construct(self):
        title = Text("Agentization", font_size=30).to_edge(UP)
        self.play(Write(title))

        text1 = Text(
            "ChatDev reduces intervention\nby prompt engineering\nat subtask round start.", 
            font_size=26, line_spacing=1.2
        ).next_to(title, DOWN, buff=0.5)

        loop_box = RoundedRectangle(width=4, height=2, corner_radius=0.2).next_to(text1, DOWN, buff=0.5)
        loop_text = Text("Automated\ncommunication loop", font_size=24).move_to(loop_box.get_center())

        issues_title = Text("Challenges:", font_size=26).next_to(loop_box, DOWN, buff=0.5).align_to(title, LEFT)
        
        issue_list = VGroup(
            Text("- Role Flipping", font_size=24),
            Text("- Instruction Repeating", font_size=24),
            Text("- Fake Replies", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT).next_to(issues_title, DOWN, aligned_edge=LEFT)

        arrow = Arrow(start=loop_box.get_bottom(), end=issues_title.get_top(), buff=0.1)

        consequence = Text(
            "Hinders productive\ncommunication and solutions",
            font_size=26, color=RED
        ).next_to(issue_list, DOWN, buff=0.5)

        self.play(FadeIn(text1, shift=DOWN))
        self.wait(1)
        self.play(FadeIn(loop_box), Write(loop_text))
        self.wait(1)
        self.play(GrowArrow(arrow), Write(issues_title))
        self.wait(1)
        self.play(LaggedStart(*[FadeIn(item, shift=DOWN) for item in issue_list], lag_ratio=0.3))
        self.wait(1)
        self.play(FadeIn(consequence, shift=UP))
        self.wait(2)
        self.wait(9.00)
        self.play(FadeOut(*self.mobjects))