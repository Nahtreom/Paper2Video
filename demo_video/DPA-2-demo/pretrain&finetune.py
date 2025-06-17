from manim import *

class DPA2Generalization(Scene):
    def construct(self):
        # Title
        title = Text("Generalization of Multi-task Pretrained DPA-2", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Table 2 image
        table_image = ImageMobject("images/e780f8bbdb5581a6accf921121e4554d76ac8df6c3efb6d1833a444bdffd80a2.jpg")
        table_image.scale(0.7).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(table_image))
        self.wait(2)

        # Page 1: Benchmarks on single-task
        page1 = Tex(
            r"""
            Before multi-tasking, DPA-2 is evaluated on benchmarks: \\
            $\bullet$ On ANI-1x: better accuracy than reported baseline \\
            $\bullet$ On OC20: comparable to GemNet-OC84, better than Equiformer V2, NequIP, MACE \\
            $\Rightarrow$ Competitive performance even with single-task pretraining
            """,
            font_size=28
        ).next_to(table_image, DOWN, buff=0.4)
        self.play(Write(page1))
        self.wait(5)
        self.play(FadeOut(page1))

        # Page 2: Multi-task training performance
        page2 = Tex(
            r"""
            Multi-task training uses all datasets: \\
            $\bullet$ Only slight degradation on pretraining datasets \\
            $\bullet$ Force WARMSE: 116.3 meV/Å (vs. 111.1 meV/Å) \\
            $\bullet$ Energy WARMSE: 18.6 meV/atom (vs. 14.9 meV/atom)
            """,
            font_size=28
        ).next_to(table_image, DOWN, buff=0.4)
        self.play(Write(page2))
        self.wait(5)
        self.play(FadeOut(page2))

        # Page 3: Zero-shot generalization
        page3 = Tex(
            r"""
            DPA-2 zero-shot generalization: \\
            $\bullet$ Evaluated on downstream datasets without fine-tuning \\
            $\bullet$ Multi-task DPA-2 outperforms single-task and MACE-MP-0 \\
            $\Rightarrow$ Gains mainly due to multi-task pretraining, not just architecture
            """,
            font_size=28
        ).next_to(table_image, DOWN, buff=0.4)
        self.play(Write(page3))
        self.wait(6)
        self.play(FadeOut(page3))

        # Page 4: Fine-tuning benefits
        page4 = Tex(
            r"""
            Fine-tuning on downstream tasks further improves accuracy: \\
            $\bullet$ DPA-2 initialized from pretraining converges faster \\
            $\bullet$ Needs less data to achieve same error level \\
            $\bullet$ E.g. H2O-PBE0TS-MD: 100x data saved for same energy RMSE
            """,
            font_size=28
        ).next_to(table_image, DOWN, buff=0.4)
        self.play(Write(page4))
        self.wait(6)

        # End
        self.play(FadeOut(page4), FadeOut(table_image), FadeOut(title))
