from manim import *

class LAMDatasets(Scene):
    def construct(self):
        # Title
        title = Text("LAM Pre-training Dataset Overview", font_size=36, color=WHITE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Slide 1: Key Criteria
        criteria = Text(
            "Key Criteria for Pre-training Data:\n"
            "1. Broad coverage of chemical and configurational spaces\n"
            "   – Ensures scenarios encountered downstream are represented\n"
            "2. High-quality labels from diverse DFT settings\n"
            "   – Supports robust multi-task learning and zero-shot generalization",
            font_size=24,
            color=WHITE,
            line_spacing=1.2
        ).next_to(title, DOWN, buff=0.7)
        self.play(Write(criteria))
        self.wait(4)
        self.play(FadeOut(criteria))

        # Slide 2: Table 1 – Dataset List
        table1 = ImageMobject("images/5fd6638d6d9b99668baa6224e682763082018fa38dfc269de3edc63de4660bf0.jpg")
        table1.scale(0.5).next_to(title, DOWN, buff=0.3)
        caption1 = Text(
            "Table 1 | Overview of Pre-training and Downstream Datasets\n"
            "Includes alloys, cathodes, clusters, drug-like molecules, perovskites, and more",
            font_size=20,
            color=WHITE,
            line_spacing=1.1
        ).next_to(table1, DOWN, buff=0.3)
        self.play(FadeIn(table1), Write(caption1))
        self.wait(5)
        self.play(FadeOut(table1), FadeOut(caption1))

        # Slide 3: Table 2 – Zero-Shot Errors
        table2 = ImageMobject("images/e780f8bbdb5581a6accf921121e4554d76ac8df6c3efb6d1833a444bdffd80a2.jpg")
        table2.scale(0.75).next_to(title, DOWN, buff=0.5)
        caption2 = Text(
            "Table 2 | Zero-Shot Generalization Errors\n"
            "DPA-2 achieves low error across unseen downstream tasks, demonstrating strong transferability",
            font_size=20,
            color=WHITE,
            line_spacing=1.1
        ).next_to(table2, DOWN, buff=0.3)
        self.play(FadeIn(table2), Write(caption2))
        self.wait(5)
        self.play(FadeOut(table2), FadeOut(caption2))

        # Slide 4: Summary
        summary = Text(
            "Summary:\n"
            "- Carefully curated and weighted datasets provide comprehensive chemistry coverage\n"
            "- Multi-task pre-training embeds rich knowledge for fast downstream adaptation\n"
            "- DPA-2 shows outstanding zero-shot performance on diverse tasks",
            font_size=24,
            color=WHITE,
            line_spacing=1.2
        ).next_to(title, DOWN, buff=0.7)
        self.play(Write(summary))
        self.wait(5)
