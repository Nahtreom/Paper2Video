from manim import *

class AgentsCollaborationScene(Scene):
    def construct(self):
        title = Text("Agent Collaboration in Subtask", font_size=30).to_edge(UP)
        self.play(Write(title))

        instructor = Circle(radius=0.6, color=BLUE).shift(LEFT*4 + UP)
        instructor_label = Text("Instructor\n(Agent T)", font_size=20).next_to(instructor, DOWN)
        
        assistant = Circle(radius=0.6, color=GREEN).shift(RIGHT*4 + UP)
        assistant_label = Text("Assistant\n(Agent A)", font_size=20).next_to(assistant, DOWN)

        self.play(FadeIn(instructor), Write(instructor_label))
        self.play(FadeIn(assistant), Write(assistant_label))

        arrow_T_A = Arrow(start=instructor.get_right(), end=assistant.get_left(), buff=0.2)
        arrow_A_T = Arrow(start=assistant.get_left(), end=instructor.get_right(), buff=0.2, color=ORANGE).shift(DOWN*0.5)

        dialogue = Text("Multi-turn Dialogue (C)", font_size=22).move_to(DOWN*0.5)
        
        self.play(GrowArrow(arrow_T_A), GrowArrow(arrow_A_T), FadeIn(dialogue))

        solutions_text = Text("Solution Extraction (τ)", font_size=22, color=YELLOW).move_to(DOWN*2)
        self.play(Write(solutions_text))

        examples_text = BulletedList(
            "Textual Solutions (e.g., software definitions)",
            "Code Solutions (e.g., initial source code)"
        ).scale(0.6).next_to(solutions_text, DOWN, buff=0.3)

        self.play(FadeIn(examples_text))
        
        self.wait(3)
        self.wait(19.44)
        self.play(FadeOut(*self.mobjects))