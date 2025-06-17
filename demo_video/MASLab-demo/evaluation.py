from manim import *

class MASLabEvaluation(Scene):
    def construct(self):

        title = Text("Evaluation", font_size=50)
        self.play(FadeIn(title))
        self.wait(2)
        self.play(FadeOut(title))
        
        # Helper function to create bullet lists without LaTeX
        def bullet_list(items, font_size=48, line_spacing=0.8):
            texts = VGroup(*[
                Text("• " + item, font_size=font_size) for item in items
            ])
            texts.arrange(DOWN, aligned_edge=LEFT, buff=line_spacing)
            return texts

        # 1. Title
        title = Text("MASLab Evaluation Protocols", font_size=45)
        self.play(Write(title))
        self.wait(1.5)
        self.play(FadeOut(title))

        # 2. Importance of Evaluation
        ev_desc = Text(
            "Accurate, automated, and scalable evaluation is essential for AI research.",
            font_size=30
        ).move_to(ORIGIN)
        self.play(Write(ev_desc))
        self.wait(3)
        self.play(FadeOut(ev_desc))

        # 3. Problems in existing MAS evaluation
        issue_title = Text("Problems in Current MAS Evaluation", font_size=45).to_edge(UP)
        issue_items = [
            "Inconsistent procedures introduce confounding variables",
            "Evaluation can be gamed via format-specific prompts",
            "Rule-based matching lacks semantic understanding"
        ]
        issue_points = bullet_list(issue_items, font_size=35, line_spacing=0.8)
        issue_points.next_to(issue_title, DOWN, buff=0.5)
        self.play(Write(issue_title), FadeIn(issue_points, shift=DOWN))
        self.wait(4)
        self.play(FadeOut(issue_title), FadeOut(issue_points))

        # 4. MASLab Unified Framework
        sol_title = Text("MASLab's Unified Evaluation Framework", font_size=45).to_edge(UP)
        sol_items = [
            "LLM-based semantic evaluation using ground-truth answers",
            "Two-step pipeline: extract and compare",
            "Task-specific evaluators like xVerify",
            "Includes rule-based strategies"
        ]
        sol_points = bullet_list(sol_items, font_size=35, line_spacing=0.8)
        sol_points.next_to(sol_title, DOWN, buff=0.5)
        self.play(Write(sol_title), FadeIn(sol_points, shift=DOWN))
        self.wait(4)
        self.play(FadeOut(sol_title), FadeOut(sol_points))

        # 5. Figure 3: Evaluation results on MATH benchmark

        # 6. Protocol effects on rankings
        effect_title = Text("Evaluation Protocols Affect Rankings", font_size=45).to_edge(UP)
        effect_items = [
            "MAV: 1st (LLM-based) → 10th (rule-based)",
            "AgentVerse: 79.0 → 25.6 accuracy drop",
            "DyLAN: 5th → 3rd under rule-based"
        ]
        fig3 = ImageMobject("images/d93671e9de6b3404f6fa9f3b2889d6985422eda27337752cfe2e47e0dfcbfbc6.jpg")
        fig3.scale(1.1)
        effect_points = bullet_list(effect_items, font_size=35, line_spacing=0.8)
        effect_points.next_to(effect_title, DOWN, buff=0.5)
        self.play(Write(effect_title))
        self.play(FadeIn(fig3))
        self.wait(4)
        self.play(FadeOut(fig3))
        self.play(FadeIn(effect_points, shift=DOWN))
        self.wait(4)
        self.play(FadeOut(effect_title), FadeOut(effect_points))

        # 7. LLM Evaluation Reliability
        rel_title = Text("LLM Evaluation Reliability", font_size=45).to_edge(UP)
        rel_items = [
            ">98% agreement with humans (2-step & xVerify)",
            "Best rule-based method: 65% agreement",
            "MASLab defaults to xVerify for balance"
        ]
        fig4 = ImageMobject("images/6d78097237fa8ecfdb2dec0677e8e1b35ea196970197497774c74f3ff4211ee3.jpg")
        fig4.scale(0.9)

        rel_points = bullet_list(rel_items, font_size=35, line_spacing=0.8)
        rel_points.next_to(rel_title, DOWN, buff=0.5)
        self.play(Write(rel_title))
        self.play(FadeIn(fig4))
        self.wait(4)
        self.play(FadeOut(fig4))
        self.play(FadeIn(rel_points, shift=DOWN))
        self.wait(4)
        self.play(FadeOut(rel_title), FadeOut(rel_points))

        # 8. Evaluating Coding Tasks
        code_title = Text("Evaluating Coding Tasks", font_size=45).to_edge(UP)
        code_items = [
            "No ground-truth → LLM-assisted evaluation",
            "Extract code from MAS output",
            "Execute against sandboxed test cases",
            "Focus on functional correctness"
        ]
        code_points = bullet_list(code_items, font_size=35, line_spacing=0.8)
        code_points.next_to(code_title, DOWN, buff=0.5)
        self.play(Write(code_title), FadeIn(code_points, shift=DOWN))
        self.wait(4)
        self.play(FadeOut(code_title), FadeOut(code_points))
