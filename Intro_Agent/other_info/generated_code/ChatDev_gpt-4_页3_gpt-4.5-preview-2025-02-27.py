from manim import *

class ChatDevWaterfall(Scene):
    def construct(self):
        title = Text("ChatDev Waterfall Model", font_size=30).to_edge(UP)
        self.play(Write(title))

        intro_text = Text(
            "Challenges in LLM-based software generation:", font_size=26
        ).next_to(title, DOWN, buff=0.4)
        
        challenge = Text(
            "Transforming textual requirements into functional software in one step.",
            font_size=22, line_spacing=1.4
        ).next_to(intro_text, DOWN, buff=0.3)
        self.play(FadeIn(intro_text), Write(challenge))

        waterfall_txt = Text(
            "Inspired by waterfall model principles, ChatDev uses:", font_size=24
        ).next_to(challenge, DOWN, buff=0.6)
        self.play(FadeIn(waterfall_txt))

        phases_group = VGroup(
            Rectangle(width=2.5, height=1, color=BLUE).set_fill(BLUE, opacity=0.2).set_opacity(0.5).set_stroke(width=1.5),
            Rectangle(width=2.5, height=1, color=GREEN).set_fill(GREEN, opacity=0.2).set_opacity(0.5).set_stroke(width=1.5),
            Rectangle(width=2.5, height=1, color=ORANGE).set_fill(ORANGE, opacity=0.2).set_opacity(0.5).set_stroke(width=1.5)
        ).arrange(RIGHT, buff=0.5).next_to(waterfall_txt, DOWN, buff=0.8)

        phases_labels = ["Design", "Coding", "Testing"]
        phases_texts = VGroup(*[
            Text(label, font_size=22).move_to(phases_group[i].get_center())
            for i, label in enumerate(phases_labels)
        ])

        self.play(FadeIn(phases_group))
        for text in phases_texts:
            self.play(Write(text))

        coding_subtasks = VGroup(
            Text("Code Writing", font_size=20),
            Text("Code Completion", font_size=20)
        ).arrange(DOWN, buff=0.2).next_to(phases_group[1], DOWN, buff=0.3)
        subtasks_box1 = SurroundingRectangle(coding_subtasks, color=GREEN, buff=0.2, stroke_width=1.2)

        testing_subtasks = VGroup(
            Text("Code Review (Static)", font_size=20),
            Text("System Testing (Dynamic)", font_size=20)
        ).arrange(DOWN, buff=0.2).next_to(phases_group[2], DOWN, buff=0.3)
        subtasks_box2 = SurroundingRectangle(testing_subtasks, color=ORANGE, buff=0.2, stroke_width=1.2)

        self.play(FadeIn(subtasks_box1), Write(coding_subtasks))
        self.play(FadeIn(subtasks_box2), Write(testing_subtasks))

        self.wait(2)
        self.wait(21.00)
        self.play(FadeOut(*self.mobjects))