from manim import *

class LAMWorkflow(Scene):
    def construct(self):
        # Title
        title = Text("LAM Workflow Overview", font_size=36, color=WHITE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Display workflow diagram
        diagram = ImageMobject("images/ce347d23ebe844d595de81e25e2ea94ad9505af253f5f34f923984bd6d2317eb.jpg")
        diagram.scale(0.8).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(diagram))
        self.wait(2)

        # 1. Pre-training phase
        pre = Text(
            "1. Pre-training:\n"
            "• Share a unified descriptor across all DFT-labeled datasets\n"
            "• Each dataset has its own energy-fitting network\n"
            "• Descriptor parameters optimized on all data, fitting nets on their own data",
            font_size=24,
            color=WHITE
        ).next_to(diagram, DOWN, buff=0.5)
        self.play(Write(pre))
        self.wait(3)
        self.play(FadeOut(pre))

        # 2. Fine-tuning for downstream tasks
        fine = Text(
            "2. Fine-tuning:\n"
            "• Initialize with the pre-trained descriptor\n"
            "• Fitting network: either reinitialize or inherit from a pre-training task\n"
            "• Adapt quickly to new PES modeling tasks",
            font_size=24,
            color=WHITE
        ).next_to(diagram, DOWN, buff=0.5)
        self.play(Write(fine))
        self.wait(3)
        self.play(FadeOut(fine))

        # 3. Knowledge distillation
        distill = Text(
            "3. Knowledge Distillation:\n"
            "• Use fine-tuned model as teacher to label MD data\n"
            "• Train a simpler student model for speed\n"
            "• Iterate: sample configurations where student error is high\n"
            "• End when student matches teacher accuracy",
            font_size=24,
            color=WHITE
        ).next_to(diagram, DOWN, buff=0.5)
        self.play(Write(distill))
        self.wait(3)
        self.play(FadeOut(distill), FadeOut(diagram))

        # Closing
        pretrain_box = Rectangle(width=3.5, height=1, color=BLUE)
        pretrain_label = Text("Pre-training", font_size=22, color=WHITE).move_to(pretrain_box)

        finetune_box = Rectangle(width=3.5, height=1, color=YELLOW)
        finetune_label = Text("Fine-tuning", font_size=22, color=WHITE).move_to(finetune_box)

        distill_box = Rectangle(width=3.5, height=1, color=GREEN)
        distill_label = Text("Distillation", font_size=22, color=WHITE).move_to(distill_box)

        # group together and arrange horizontally
        workflow_boxes = VGroup(
            VGroup(pretrain_box, pretrain_label),
            VGroup(finetune_box, finetune_label),
            VGroup(distill_box, distill_label)
        ).arrange(RIGHT, buff=1).shift(UP * 0.5)

        # arrows between steps
        arrow1 = Arrow(start=pretrain_box.get_right(), end=finetune_box.get_left(), buff=0.1)
        arrow2 = Arrow(start=finetune_box.get_right(), end=distill_box.get_left(), buff=0.1)

        # outcome text
        outcome = Text("→ High Accuracy & Efficiency", font_size=26, color=WHITE).next_to(workflow_boxes, DOWN, buff=0.8)

        # animate
        self.play(Create(pretrain_box), Write(pretrain_label))
        self.play(Create(finetune_box), Write(finetune_label))
        self.play(Create(distill_box), Write(distill_label))
        self.play(Create(arrow1), Create(arrow2))
        self.play(Write(outcome))
        self.wait(3)