# 6 Limitations  

Our study explores the potential of cooperative autonomous agents in software development, but certain limitations and risks must be considered by researchers and practitioners. Firstly, the capabilities of autonomous agents in software production might be overestimated. While they enhance development quality, agents often implement simple logic, resulting in low information density. Without clear, detailed requirements, agents struggle to grasp task ideas. For instance, vague guidelines in developing a Snake game lead to basic representations; in information management systems, agents might retrieve static key-value placeholders instead of external databases. Therefore, it is crucial to clearly define detailed software requirements. Currently, these technologies are more suitable for prototype systems rather than complex real-world applications. Secondly, unlike traditional functionlevel code generation, automating the evaluation of general-purpose software is highly complex. While some efforts have focused on Human Revision Cost (Hong et al., 2023), manual verification for large datasets is impractical. Our paper emphasizes completeness, executability, consistency, and overall quality, but future research should consider additional factors such as functionalities, robustness, safety, and user-friendliness. Thirdly, compared to single-agent approaches, multiple agents require more tokens and time, increasing computational demands and environmental impact. Future research should aim to enhance agent capabilities with fewer interactions. Despite these limitations, we believe that engaging a broader, technically proficient audience can unlock additional potential directions in LLM-powered multi-agent collaboration.  

# Acknowledgments  

The work was supported by the National Key R&D Program of China (No.2022ZD0116312), the Postdoctoral Fellowship Program of CPSF under Grant Number GZB20230348, and Tencent Rhino-Bird Focused Research Program.  

# References  

Silvia T Acuna, Natalia Juristo, and Ana M Moreno. 2006. Emphasizing Human Capabilities in Software Development. In IEEE Software, volume 23, pages 94–101.  

Mansi Agnihotri and Anuradha Chug. 2020. A Systematic Literature Survey of Software Metrics, Code Smells and Refactoring Techniques. In booktitle of Information Processing Systems, volume 16, pages 915–934.  

Rajiv D Banker, Gordon B Davis, and Sandra A Slaughter. 1998. Software Development Practices, Software Complexity, and Software Maintenance Performance: A Field Study. In Management science, volume 44, pages 433–450.  

Victor R Basili. 1989. Software Development: A Paradigm for The Future. In Proceedings of the Annual International Computer Software and Applications Conference, pages 471–485. IEEE.  

Thorsten Brants, Ashok C Popat, Peng Xu, Franz J Och, and Jeffrey Dean. 2007. Large Language Models in Machine Translation. In Proceedings of the 2007 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL), pages 858– 867.  

Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens Winter, Chris Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. 2020. Language Models are Few-Shot Learners. In Advances in Neural Information Processing Systems (NeurIPS), volume 33, pages 1877–1901.  

Sébastien Bubeck, Varun Chandrasekaran, Ronen Eldan, Johannes Gehrke, Eric Horvitz, Ece Kamar, Peter Lee, Yin Tat Lee, Yuanzhi Li, Scott Lundberg, Harsha Nori, Hamid Palangi, Marco Tulio Ribeiro, and Yi Zhang. 2023. Sparks of artificial general intelligence: Early experiments with gpt-4. In arXiv preprint arXiv:2303.12712.  

Tianle Cai, Xuezhi Wang, Tengyu Ma, Xinyun Chen, and Denny Zhou. 2023. Large Language Models as Tool Makers. In arXiv preprint arXiv:2305.17126.  

Chi-Min Chan, Weize Chen, Yusheng Su, Jianxuan Yu, Wei Xue, Shanghang Zhang, Jie Fu, and Zhiyuan Liu. 2023. ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate. In arXiv preprint arXiv:2308.07201.  

Dake Chen, Hanbin Wang, Yunhao Huo, Yuzhao Li, and Haoyang Zhang. 2023a. GameGPT: Multi-agent  

Collaborative Framework for Game Development. In arXiv preprint arXiv:2310.08067.   
Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, et al. 2021. Evaluating Large Language Models Trained on Code. In arXiv preprint arXiv:2107.03374.   
Weize Chen, Yusheng Su, Jingwei Zuo, Cheng Yang, Chenfei Yuan, Chen Qian, Chi-Min Chan, Yujia Qin, Yaxi Lu, Ruobing Xie, et al. 2023b. AgentVerse: Facilitating Multi-agent Collaboration and Exploring Emergent Behaviors in Agents. In International Conference on Learning Representations (ICLR).   
Roi Cohen, May Hamri, Mor Geva, and Amir Globerson. 2023. LM vs LM: Detecting Factual Errors via Cross Examination. In ArXiv, volume abs/2305.13281.   
Shehzaad Dhuliawala, Mojtaba Komeili, Jing Xu, Roberta Raileanu, Xian Li, Asli Celikyilmaz, and Jason Weston. 2023. Chain-of-Verification Reduces Hallucination in Large Language Models. In arXiv preprint arXiv:2309.11495.   
Shiying Ding, Xinyi Chen, Yan Fang, Wenrui Liu, Yiwu Qiu, and Chunlei Chai. 2023. DesignGPT: MultiAgent Collaboration in Design. In arXiv preprint arXiv:2311.11591.   
Michael D. Ernst. 2017. Natural Language is a Programming Language: Applying Natural Language Processing to Software Development. In Advances in Programming Languages (SNAPL), volume 71, pages 4:1–4:14.   
Saad Ezzini, Sallam Abualhaija, Chetan Arora, and Mehrdad Sabetzadeh. 2022. Automated Handling of Anaphoric Ambiguity in Requirements: A Multisolution Study. In International Conference on Software Engineering (ICSE), pages 187–199.   
Robert France and Bernhard Rumpe. 2007. Modeldriven Development of Complex Software: A Research Roadmap. In Future of Software Engineering (FOSE), pages 37–54.   
Peter Freeman, Donald J. Bagert, Hossein Saiedian, Mary Shaw, Robert Dupuis, and J. Barrie Thompson. 2001. Software Engineering Body of Knowledge (SWEBOK). In Proceedings of the International Conference on Software Engineering (ICSE), pages 693–696.   
Sa Gao, Chunyang Chen, Zhenchang Xing, Yukun Ma, Wen Song, and Shang-Wei Lin. 2019. A Neural Model for Method Name Generation from Functional Description. In 26th IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER), pages 411–421.   
Sirui Hong, Mingchen Zhuge, Jonathan Chen, Xiawu Zheng, Yuheng Cheng, Ceyao Zhang, Jinlin Wang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu, and Jürgen Schmidhuber. 2023. MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework. In International Conference on Learning Representations (ICLR).   
Wenyue Hua, Lizhou Fan, Lingyao Li, Kai Mei, Jianchao Ji, Yingqiang Ge, Libby Hemphill, and Yongfeng Zhang. 2023. War and Peace (WarAgent): Large Language Model-based Multi-Agent Simulation of World Wars. In arXiv preprint arXiv:2311.17227.   
Ziwei Ji, Nayeon Lee, Rita Frieske, Tiezheng Yu, Dan Su, Yan Xu, Etsuko Ishii, Ye Jin Bang, Andrea Madotto, and Pascale Fung. 2023. Survey of Hallucination in Natural Language Generation. In ACM Computing Surveys, volume 55, pages 1–38.   
Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. 2020. Scaling Laws for Neural Language Models. In arXiv preprint arXiv:2001.08361.   
Guohao Li, Hasan Abed Al Kader Hammoud, Hani Itani, Dmitrii Khizbullin, and Bernard Ghanem. 2023a. CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society. In Thirty-seventh Conference on Neural Information Processing Systems (NeurIPS).   
Yuan Li, Yixuan Zhang, and Lichao Sun. 2023b. MetaAgents: Simulating Interactions of Human Behaviors for LLM-based Task-oriented Coordination via Collaborative Generative Agents. In arXiv preprint arXiv:2310.06500.   
Zhiwei Liu, Weiran Yao, Jianguo Zhang, Le Xue, Shelby Heinecke, Rithesh Murthy, Yihao Feng, Zeyuan Chen, Juan Carlos Niebles, Devansh Arpit, Ran Xu, Phil Mui, Huan Wang, Caiming Xiong, and Silvio Savarese. 2023. BOLAA: Benchmarking and Orchestrating LLM-augmented Autonomous Agents. In arXiv preprint arXiv:2308.05960.   
Kaixin Ma, Hongming Zhang, Hongwei Wang, Xiaoman Pan, and Dong Yu. 2023. LASER: LLM Agent with State-Space Exploration for Web Navigation. In arXiv preprint arXiv:2309.08172.   
Cuauhtémoc López Martín and Alain Abran. 2015. Neural networks for predicting the duration of new software projects. In J. Syst. Softw., volume 101, pages 127–135.   
Nadia Nahar, Shurui Zhou, Grace A. Lewis, and Christian Kästner. 2022. Collaboration Challenges in Building ML-Enabled Systems: Communication, Documentation, Engineering, and Process. In IEEE/ACM International Conference on Software Engineering (ICSE), pages 413–425.   
Erik Nijkamp, Bo Pang, Hiroaki Hayashi, Lifu Tu, Huan Wang, Yingbo Zhou, Silvio Savarese, and Caiming Xiong. 2023. CodeGen: An Open Large Language Model for Code with Multi-Turn Program Synthesis. In The International Conference on Learning Representations (ICLR).   
Anton Osika. 2023. GPT-Engineer. In https://github.com/AntonOsika/gpt-engineer.   
Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, and Ryan Lowe. 2022. Training Language Models to Follow Instructions with Human Feedback. In arXiv preprint arXiv:2203.02155.   
Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and Michael S. Bernstein. 2023. Generative Agents: Interactive Simulacra of Human Behavior. In Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology (UIST).   
Florian Pudlitz, Florian Brokhausen, and Andreas Vogelsang. 2019. Extraction of System States from Natural Language Requirements. In IEEE International Requirements Engineering Conference $( R E )$ , pages 211–222.   
Yujia Qin, Shihao Liang, Yining Ye, Kunlun Zhu, Lan Yan, Yaxi Lu, Yankai Lin, Xin Cong, Xiangru Tang, Bill Qian, et al. 2023a. ToolLLM: Facilitating Large Language Models to Master $1 6 0 0 0 +$ Real-World APIs. In arXiv preprint arXiv:2307.16789.   
Zhen Qin, Rolf Jagerman, Kai Hui, Honglei Zhuang, Junru Wu, Jiaming Shen, Tianqi Liu, Jialu Liu, Donald Metzler, Xuanhui Wang, and Michael Bendersky. 2023b. Large Language Models are Effective Text Rankers with Pairwise Ranking Prompting. In arXiv preprint arXiv:2306.17563.   
Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever, et al. Language Models are Unsupervised Multitask Learners. In OpenAI Blog, volume 1, page 9.   
Toran Bruce Richards. 2023. AutoGPT. In https://github.com/Significant-Gravitas/AutoGPT.   
Jingqing Ruan, Yihong Chen, Bin Zhang, Zhiwei Xu, Tianpeng Bao, Guoqing Du, Shiwei Shi, Hangyu Mao, Ziyue Li, Xingyu Zeng, and Rui Zhao. 2023. TPTU: Large Language Model-based AI Agents for Task Planning and Tool Usage. In arXiv preprint arXiv:2308.03427.   
Steve Sawyer and Patricia J. Guinan. 1998. Software development: Processes and Performance. In IBM  

Systems Journal, volume 37, pages 552–569.  

Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom. 2023. ToolFormer: Language Models Can Teach Themselves to Use Tools. In arXiv preprint arXiv:2302.04761.  

Murray Shanahan, Kyle McDonell, and Laria Reynolds. 2023. Role Play with Large Language Models. In Nature, volume 623, pages 493–498.   
Theodore R. Sumers, Shunyu Yao, Karthik Narasimhan, and Thomas L. Griffiths. 2023. Cognitive Architectures for Language Agents. In arXiv preprint arXiv:2309.02427.   
Hannes Thaller, Lukas Linsbauer, and Alexander Egyed. 2019. Feature Maps: A Comprehensible Software Representation for Design Pattern Detection. In IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER), pages 207–217.   
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al. 2023. LLaMA: Open and Efficient Foundation Language Models. In arXiv preprint arXiv:2302.13971.   
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. 2017. Attention is All You Need. In Advances in Neural Information Processing Systems (NeurIPS), volume 30.   
Chengcheng Wan, Shicheng Liu, Sophie Xie, Yifan Liu, Henry Hoffmann, Michael Maire, and Shan Lu. 2022. Automated Testing of Software that Uses Machine Learning APIs. In IEEE/ACM International Conference on Software Engineering (ICSE), pages 212–224.   
Yao Wan, Zhou Zhao, Min Yang, Guandong Xu, Haochao Ying, Jian Wu, and Philip S. Yu. 2018. Improving Automatic Source Code Summarization via Deep Reinforcement Learning. In Proceedings of the ACM/IEEE International Conference on Automated Software Engineering (ASE), pages 397–407.   
Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and Anima Anandkumar. 2023a. Voyager: An Open-ended Embodied Agent with Large Language Models. In arXiv preprint arXiv:2305.16291.   
Lei Wang, Jingsen Zhang, Hao Yang, Zhiyuan Chen, Jiakai Tang, Zeyu Zhang, Xu Chen, Yankai Lin, Ruihua Song, Wayne Xin Zhao, Jun Xu, Zhicheng Dou, Jun Wang, and Ji-Rong Wen. 2023b. When Large Language Model based Agent Meets User Behavior Analysis: A Novel User Simulation Paradigm. In arXiv preprint arXiv:2306.02552.   
Peiyi Wang, Lei Li, Liang Chen, Zefan Cai, Dawei Zhu, Binghuai Lin, Yunbo Cao, Qi Liu, Tianyu Liu, and Zhifang Sui. 2023c. Large Language Models are not Fair Evaluators. In arXiv preprint arXiv:2305.17926.   
Song Wang, Taiyue Liu, and Lin Tan. 2016. Automatically Learning Semantic Features for Defect Prediction. In Proceedings of the International Conference on Software Engineering (ICSE), pages 297–308.   
Song Wang, Nishtha Shrestha, Abarna Kucheri Subburaman, Junjie Wang, Moshi Wei, and Nachiappan Nagappan. 2021. Automatic Unit Test Generation for Machine Learning Libraries: How Far Are We? In IEEE/ACM International Conference on Software Engineering (ICSE), pages 1548–1560.   
Xinyuan Wang, Chenxi Li, Zhen Wang, Fan Bai, Haotian Luo, Jiayou Zhang, Nebojsa Jojic, Eric P. Xing, and Zhiting Hu. 2023d. PromptAgent: Strategic Planning with Language Models Enables Expertlevel Prompt Optimization. In arXiv preprint arXiv:2310.16427.   
Zhilin Wang, Yu Ying Chiu, and Yu Cheung Chiu. 2023e. Humanoid Agents: Platform for Simulating Human-like Generative Agents. In arXiv preprint arXiv:2310.05418.   
Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma, Denny Zhou, Donald Metzler, et al. 2022a. Emergent Abilities of Large Language Models. In arXiv preprint arXiv:2206.07682.   
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. 2022b. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. In Advances in Neural Information Processing Systems (NeurIPS), volume 35, pages 24824–24837.   
Lilian Weng. 2023. LLM-powered Autonomous Agents. In lilianweng.github.io.   
Jonas Winkler, Jannis Grönberg, and Andreas Vogelsang. 2020. Predicting How to Test Requirements: An Automated Approach. In Software Engineering, volume P-300 of LNI, pages 141–142.   
Chengrun Yang, Xuezhi Wang, Yifeng Lu, Hanxiao Liu, Quoc V. Le, Denny Zhou, and Xinyun Chen. 2023a. Large Language Models as Optimizers. In arXiv preprint arXiv:2309.03409.   
Rui Yang, Lin Song, Yanwei Li, Sijie Zhao, Yixiao Ge, Xiu Li, and Ying Shan. 2023b. GPT4Tools: Teaching Large Language Model to Use Tools via Self-instruction. In Advances in Neural Information Processing Systems (NeurIPS).   
Murat Yilmaz, Rory V O’Connor, and Paul Clarke. 2012. A Systematic Approach to the Comparison of Roles in the Software Development Processes. In International Conference on Software Process Improvement and Capability Determination, pages 198–209. Springer.   
Zhangyue Yin, Qiushi Sun, Cheng Chang, Qipeng Guo, Junqi Dai, Xuanjing Huang, and Xipeng Qiu. 2023. Exchange-of-Thought: Enhancing Large Language Model Capabilities through Cross-Model Communication. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP), pages 15135–15153.   
An Zhang, Leheng Sheng, Yuxin Chen, Hao Li, Yang Deng, Xiang Wang, and Tat-Seng Chua. 2023a. On Generative Agents in Recommendation. In arXiv preprint arXiv:2310.10108.   
Yue Zhang, Yafu Li, Leyang Cui, Deng Cai, Lemao Liu, Tingchen Fu, Xinting Huang, Enbo Zhao, Yu Zhang, Yulong Chen, et al. 2023b. Siren’s Song in the AI Ocean: A Survey on Hallucination in Large Language Models. In arXiv preprint arXiv:2309.01219.   
Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Yong-Jin Liu, and Gao Huang. 2023. ExpeL: LLM Agents Are Experiential Learners. In AAAI Conference on Artificial Intelligence (AAAI).   
Tianming Zhao, Chunyang Chen, Yuanning Liu, and Xiaodong Zhu. 2021. GUIGAN: Learning to Generate GUI Designs Using Generative Adversarial Networks. In IEEE/ACM International Conference on Software Engineering (ICSE), pages 748–760.   
Shuyan Zhou, Frank F Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Yonatan Bisk, Daniel Fried, Uri Alon, et al. 2023a. WebArena: A Realistic Web Environment for Building Autonomous Agents. In arXiv preprint arXiv:2307.13854.   
Wangchunshu Zhou, Yuchen Eleanor Jiang, Long Li, Jialong Wu, Tiannan Wang, Shi Qiu, Jintian Zhang, Jing Chen, Ruipu Wu, Shuai Wang, Shiding Zhu, Jiyu Chen, Wentao Zhang, Ningyu Zhang, Huajun Chen, Peng Cui, and Mrinmaya Sachan. 2023b. Agents: An Open-source Framework for Autonomous Language Agents. In arXiv preprint arXiv:2309.07870.  