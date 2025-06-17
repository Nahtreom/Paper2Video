from manim import *

class DPA2Descriptor(Scene):
    def construct(self):
        # Title and Figure
        title = Text("DPA-2 Descriptor Architecture", font_size=36, color=WHITE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        figure = ImageMobject("images/7783bd91822eacb5f8a6d8cb0b7c926aa1ef12a504594f75808a8e611e0373d5.jpg")
        figure.scale(0.6).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(figure))
        self.wait(2)

        # Page 2: Multi-channel representation
        para1_title = Text("DPA-2 uses three channels to represent atomic interactions:", font_size=26)
        line1 = MathTex(r"\bullet\ \text{Single-atom channel } f_i^*", font_size=26)
        line2 = MathTex(r"\bullet\ \text{Rotationally invariant pairwise channel } g_{ij}", font_size=26)
        line3 = MathTex(r"\bullet\ \text{Rotationally equivariant pairwise channel } h_{ij}", font_size=26)

        group1 = VGroup(para1_title, line1, line2, line3).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        group1.next_to(figure, DOWN, buff=0.5)
        self.play(FadeIn(group1))
        self.wait(4)
        self.play(FadeOut(group1))

        # Page 3: Environment encoder
        para2_lines = VGroup(
            Text("Pairwise features are initialized by the 'env' module,", font_size=26),
            MathTex(r" \text{which captures local geometry within cutoff radius}r_c^0 \text{ to } r_c^1", font_size=26),
            MathTex(r"\text{Single-atom features} f_i \text{are initialized by a repinit layer.}", font_size=26),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(figure, DOWN, buff=0.5)

        self.play(FadeIn(para2_lines))
        self.wait(4)
        self.play(FadeOut(para2_lines))

        # Page 4: 12-layer repformer
        para3_lines = VGroup(
            Text("Then, features are updated through 12 repformer layers:", font_size=26),
            MathTex(r"\bullet\ f_i \text{ updated by conv, symmetrization, MLP, self-attention}", font_size=26),
            MathTex(r"\bullet\ g_{ij} \text{ updated by MLP, dot-product, gated attention}", font_size=26)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(figure, DOWN, buff=0.5)

        self.play(FadeIn(para3_lines))
        self.wait(4)
        self.play(FadeOut(para3_lines))

        # Page 5: Physical consistency
        para4_lines = VGroup(
            Text("DPA-2 is physically consistent:", font_size=26),
            Text("• Respects translational, rotational, permutational symmetry", font_size=24),
            MathTex(r"\bullet\ F_i = - \nabla_{r_i} E", font_size=26),
            MathTex(r"\bullet\ \Xi_{\alpha\beta} = \sum_\gamma (-\nabla_{h_{\gamma\alpha}} E) h_{\gamma\beta}", font_size=26),
            Text("• All modules are 2nd-order continuous for energy conservation", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(figure, DOWN, buff=0.5)

        self.play(FadeIn(para4_lines))
        self.wait(5)
        self.play(FadeOut(para4_lines))

        # Page 6: Generalization capability
        para5 = Text(
            "Multi-task pretraining enables DPA-2 to generalize better\n"
            "than single-task or prior models like MACE.\n"
            "Its WARMSE on energy and forces shows clear improvements\n"
            "on diverse downstream molecular systems.",
            font_size=26
        ).next_to(figure, DOWN, buff=0.5)

        self.play(Write(para5))
        self.wait(5)

        # Fade out everything
        self.play(FadeOut(para5), FadeOut(figure), FadeOut(title))
