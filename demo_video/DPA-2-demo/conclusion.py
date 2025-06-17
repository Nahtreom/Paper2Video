from manim import *

class DPA2Conclusion(Scene):
    def construct(self):
        # Title
        title = Text("Conclusion and Outlook", font_size=36, color=WHITE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Page 1: Summary of DPA-2 Model
        summary = Text(
            "DPA-2 is a new architecture for Large Atomic Models (LAMs),\n"
            "backed by a complete pipeline: pre-training, fine-tuning, distillation, deployment.",
            font_size=24,
            line_spacing=1.3,
            color=WHITE
        ).to_edge(ORIGIN)
        self.play(Write(summary))
        self.wait(4)
        self.play(FadeOut(summary))

        # Page 2: Key Findings
        findings = Text(
            "Key findings:\n"
            "• Multi-task pretraining enables generalization across 73 elements\n"
            "• Reduces zero-shot RMSEs by up to 62% vs baselines\n"
            "• Needs 10–100× less data on downstream tasks with similar accuracy",
            font_size=24,
            line_spacing=1.3,
            color=WHITE
        )
        findings.next_to(title, DOWN, buff=0.5)
        self.play(Write(findings))
        self.wait(5)
        self.play(FadeOut(findings))

        # Page 3: Limitation and Outlook
        outlook = Text(
            "Limitation:\n"
            "• Current datasets lack 2D material coverage, limiting generalization.\n\n"
            "Future outlook:\n"
            "• Need broader datasets, automation, and open collaboration.\n"
            "• OpenLAM Initiative launched to support long-term development.",
            font_size=24,
            line_spacing=1.2,
            color=WHITE
        )
        outlook.next_to(title, DOWN, buff=0.5)
        self.play(Write(outlook))
        self.wait(6)
        self.play(FadeOut(outlook), FadeOut(title))
