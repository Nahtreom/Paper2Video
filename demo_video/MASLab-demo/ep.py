from manim import *

class EmpiricalStudy(Scene):
    def construct(self):
        # Helper for bullet lists
        def bullets(items, font_size=42, spacing=0.5):
            grp = VGroup(*[Text("• " + it, font_size=font_size) for it in items])
            grp.arrange(DOWN, aligned_edge=LEFT, buff=spacing)
            return grp

        # Section Title
        title = Text("Empirical Study", font_size=50)
        self.play(FadeIn(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Experimental setups
        setup = VGroup(
            Text("Experimental Setups:", font_size=50),
            bullets([
                "Backends: Llama-3.3-70B, Qwen-2.5, GPT-4o-mini, GPT-4.1",
                "Tokens: 2048, Temp: 0.5",
                "Math: MATH, GSM-Hard, AQUA-RAT, AIME-2024",
                "Sci: SciBench, GPQA; Knowledge: MMLU-Pro",
                "Med: MedMCQA; Code: HumanEval, MBPP; AI: GAIA"
            ], font_size=40)
        ).arrange(DOWN, buff=0.5).scale(0.8)
        self.play(FadeIn(setup)); self.wait(3); self.play(FadeOut(setup))

        # Table 2 and analysis
        table2 = ImageMobject("images/6d78097237fa8ecfdb2dec0677e8e1b35ea196970197497774c74f3ff4211ee3.jpg").scale(0.8).to_edge(LEFT)
        analysis2 = bullets([
            "No method dominates all five domains",
            "AgentVerse and DyLAN swap ranks across backends",
            "Llama shows stronger MAS uplift than Qwen"
        ], font_size=19).next_to(table2, RIGHT, buff=1)
        self.play(FadeIn(table2), Write(analysis2)); self.wait(4)
        self.play(FadeOut(table2), FadeOut(analysis2))

        # Figure 4 and insight
        fig4 = ImageMobject("images/4976cb6d6f67aea7f05d8cfda947ff8bceaf240626ae26890aa7f191ab91bb70.jpg").scale(0.7).to_edge(LEFT)
        insight4 = bullets([
            "Points above line: higher accuracy per token",
            "Highlights cost-effective MAS designs"
        ], font_size=20).next_to(fig4, RIGHT, buff=1)
        self.play(FadeIn(fig4), Write(insight4)); self.wait(4)
        self.play(FadeOut(fig4), FadeOut(insight4))

        # Current Landscape subheading
        sub = Text("Current Landscape", font_size=50).to_edge(UP)
        self.play(Write(sub)); 
 

        # Figure 5 with commentary
        fig5 = ImageMobject("images/a761f65690e8e37b0f264ecfde9292010f9c8cb7ec1faedb2a7687b6b1739052.jpg").scale(0.9)
        comment5 = Text("EvoMAC excels on GPT-4o-mini, MapCoder on Llama-3.3-70B.", font_size=25)
        self.play(FadeIn(fig5), Write(comment5.next_to(fig5, DOWN, buff=0.5))); self.wait(4)
        self.play(FadeOut(fig5), FadeOut(comment5))

        # Figure 6 with commentary
        fig6 = ImageMobject("images/18e0f4f1fab67ed61d06fd12e731430004902375f34c06c28a39a3b339af374c.jpg").scale(0.9)
        comment6 = Text("AFlow trades higher optimization cost for best MATH performance.", font_size=25)
        self.play(FadeIn(fig6), Write(comment6.next_to(fig6, DOWN, buff=0.5))); self.wait(4)
        self.play(FadeOut(fig6), FadeOut(comment6))

        # Figure 7 with bullet insights
        fig7 = ImageMobject("images/ca12e79d7776ec3a5a87b9e58cac47f38117afe5c85e32191c3011acab9ffef2.jpg").scale(0.7).to_edge(LEFT)
        insights7 = bullets([
            "Tool-enabled MAS > MAS without tools",
            "Stronger LLMs amplify tool benefits",
            "MASLab-ReAct achieves top performance"
        ], font_size=25).next_to(fig7, RIGHT, buff=1)
        self.play(FadeIn(fig7), Write(insights7)); self.wait(4)
        self.play(FadeOut(fig7), FadeOut(insights7))

        self.play(FadeOut(sub))
        # Scaling section
        scale_head = Text("Scaling Properties", font_size=50).to_edge(UP)
        self.play(Write(scale_head)); self.wait(1); 
        fig8 = ImageMobject("images/b5b211c503dad4205e368a5baa77076584adfe413498f70d38b8b9022d4b8083.jpg").scale(1.5)
        comment8 = Text("Self-Consistency & AgentVerse show best compute scaling.", font_size=30)
        self.play(FadeIn(fig8), Write(comment8.next_to(fig8, DOWN, buff=0.5))); self.wait(3)
        self.play(FadeOut(fig8), FadeOut(comment8))
        fig9 = ImageMobject("images/49fc68c3f9438e2bd4cad438c8a1edfc50dec082bc345dd70f4ed8ad01e27715.jpg").scale(1.5)
        comment9 = Text("LLM-Debate leads across model sizes; small models struggle.", font_size=30)
        self.play(FadeIn(fig9), Write(comment9.next_to(fig9, DOWN, buff=0.5))); self.wait(3)
        self.play(FadeOut(fig9), FadeOut(comment9))
        self.play(FadeOut(scale_head))

        # Failure Analysis section
        fail_head = Text("Failure Analysis", font_size=50).to_edge(UP)
        self.play(Write(fail_head)); self.wait(1); 
        table3 = ImageMobject("images/ad5b16ca68a7a9b00c9b72fb8e3af3f891fcac6152a0cacbb037b882deab5df1.jpg").scale(1.5)
        comment3 = Text("Format errors dominate AgentVerse failures.", font_size=30)
        self.play(FadeIn(table3), Write(comment3.next_to(table3, DOWN, buff=0.5))); self.wait(4)
        self.play(FadeOut(table3), FadeOut(comment3))
        fig10 = ImageMobject("images/1d08ad72182d1a349c0bbbc9ac959a9045efbbfadf3642596bee420c380d7bb1.jpg").scale(1.5)
        comment10 = Text("Tool usage errors highest in OWL-Roleplaying.", font_size=30)
        self.play(FadeIn(fig10), Write(comment10.next_to(fig10, DOWN, buff=0.5))); self.wait(4)
        self.play(FadeOut(fig10), FadeOut(comment10))
        self.play(FadeOut(fail_head))
