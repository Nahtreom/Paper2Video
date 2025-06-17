from manim import *

class MethodsOverview(Scene):
    def construct(self):

        title = Text("MASLab", font_size=50)
        self.play(FadeIn(title))
        self.wait(2)
        self.play(FadeOut(title))

        # 2. High-level description
        desc = Text("MASLab: A unified codebase for over 20 LLM-based MAS methods.", font_size=30).to_edge(UP)
        self.play(Write(desc))
        self.wait(2)


        # 3. Pipeline diagram (Figure 2)
        pipeline_img = ImageMobject("images/5d91264720ed37c71991312343749f3e480b5eca2b20ca9fc3de25a2c821b865.jpg")
        pipeline_img.scale(1.0).move_to(ORIGIN)
        self.play(FadeIn(pipeline_img))
        self.wait(3)
        self.play(FadeOut(pipeline_img))

        # 4. Table of Methods (Table 1)
        table_img = ImageMobject("images/6f9afd366df9d08a4b85d87a25003dc98010f4d80a995106004ef166196776c2.jpg")
        table_img.scale(0.8).move_to(ORIGIN)
        self.play(FadeIn(table_img))
        self.wait(5)
        self.play(FadeOut(table_img))
        self.play(FadeOut(desc))

        # 5. Key aspects title
        aspects_title = Text("Key Aspects of MASLab Inference", font_size=48)
        self.play(Write(aspects_title))
        self.wait(1)
        self.play(FadeOut(aspects_title))

        # Helper: manual bullet list with larger font
        def bullet_list(items, font_size=36):
            texts = VGroup(*[Text("• " + item, font_size=font_size) for item in items])
            texts.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
            return texts

        # 6. Aspect 1: Streamlined Representation
        a1_title = Text("1. Streamlined Representation", font_size=48).to_edge(UP)
        a1_points = bullet_list([
            "Abstract each method as Python class",
            "Common base class for LLM requests & token tracking",
            "Modular inference functions for clear steps"
        ])
        a1_points.next_to(a1_title, DOWN, buff=1)
        self.play(Write(a1_title), FadeIn(a1_points, shift=DOWN))
        self.wait(3)
        self.play(FadeOut(a1_title), FadeOut(a1_points))

        # 7. Aspect 2: Consistent Inputs
        a2_title = Text("2. Consistent Inputs", font_size=48).to_edge(UP)
        a2_points = bullet_list([
            "Unified preprocessing pipeline",
            "Identical data for all methods",
            "Eliminates dataset discrepancies"
        ])
        a2_points.next_to(a2_title, DOWN, buff=1)
        self.play(Write(a2_title), FadeIn(a2_points, shift=DOWN))
        self.wait(3)
        self.play(FadeOut(a2_title), FadeOut(a2_points))

        # 8. Aspect 3: Shared Resources
        a3_title = Text("3. Shared Resources", font_size=48).to_edge(UP)
        a3_points = bullet_list([
            "Unified LLM & tool interfaces",
            "Sandboxed code execution & web/image utilities",
            "Extensible with open-source developments"
        ])
        a3_points.next_to(a3_title, DOWN, buff=1)
        self.play(Write(a3_title), FadeIn(a3_points, shift=DOWN))
        self.wait(3)
        self.play(FadeOut(a3_title), FadeOut(a3_points))

        # 9. Aspect 4: Unified Configurations
        a4_title = Text("4. Unified Configurations", font_size=48).to_edge(UP)
        a4_points = bullet_list([
            "Standardized LLM & tool settings",
            "Aligned token limits & timeouts",
            "Ensures fair algorithmic comparison"
        ])
        a4_points.next_to(a4_title, DOWN, buff=1)
        self.play(Write(a4_title), FadeIn(a4_points, shift=DOWN))
        self.wait(3)
        self.play(FadeOut(a4_title), FadeOut(a4_points))