# 页 1
We introduce ChatDev, a chat-powered softwaredevelopment framework that integrates multiple "software agents" with various social roles (e.g., requirements analysts, professional programmers and test engineers) collaborating in the core phases of the software life cycle, see Figure 1. Technically, to facilitate cooperative communication, ChatDev introduces chat chain to further break down each phase into smaller and manageable subtasks, which guides multi-turn communications between different roles to propose and validate solutions for each subtask. In addition, to alleviate unexpected hallucinations, a communicative pattern named communicative dehallucination is devised, wherein agents request more detailed information before responding directly and then continue the next round of communication based on these details.

![](ChatDev_images/79021ce9de0bd97d75fc696a609821851154d2323b1123cd2b2b71870afbd198.jpg)  
Figure 1: ChatDev, a chat-powered software development framework, integrates LLM agents with various social roles, working autonomously to develop comprehensive solutions via multi-agent collaboration.

# 页 2
Although LLMs show a good understanding of natural and programming languages, efficiently transforming textual requirements into functional software in a single step remains a significant challenge. ChatDev thus adopts the core principles of the waterfall model, using a chat chain $( \mathcal { C } )$ with sequential phases $( \mathcal { P } )$ , each comprising sequential subtasks $( \mathcal { T } )$ . Specifically, ChatDev segments the software development process into three sequential phases: design, coding, and testing. The coding phase is further subdivided into subtasks of code writing and completion, and the testing phase is segmented into code review (static testing) and system testing (dynamic testing), as illustrated in Figure 2.

![](ChatDev_images/748798460d843c6da70d8549109d2d1bc44bbfccba7ec7a66b1e0c7c118fe145.jpg)  
Figure 2: Upon receiving a preliminary task requirement (e.g., “develop a Gomoku game”), these software agents engage in multi-turn communication and perform instruction-following along a chain-structured workflow, collaborating to execute a series of subtasks autonomously to craft a comprehensive solution.

# 页 3
In every subtask, two agents, each with their own specialized roles (e.g., a reviewer skilled at identifying endless loops and a programmer adept in GUI design), perform the functions of an instructor $( { \mathcal { T } } )$ and an assistant $( \mathcal { A } )$ . The instructor agent initiates instructions, instructing $(  )$ the discourse toward the completion of the subtask, while the assistant agent adheres to these instructions and responds with $( \sim )$ appropriate solutions. They engage in a multi-turn dialogue (C), working cooperatively until they achieve consensus, extracting $( \tau )$ solutions that can range from the text (e.g., defining a software function point) to code (e.g., creating the initial version of source code), ultimately leading to the completion of the subtask. The entire tasksolving process along the agentic workflow can be formulated as:

$$
\begin{array} { r l } & { \mathcal { C } = \langle \mathcal { P } ^ { 1 } , \mathcal { P } ^ { 2 } , \dotsc , \mathcal { P } ^ { | \mathcal { C } | } \rangle } \\ & { \mathcal { P } ^ { i } = \langle \mathcal { T } ^ { 1 } , \mathcal { T } ^ { 2 } , \dotsc , \mathcal { T } ^ { | \mathcal { P } ^ { i } | } \rangle } \\ & { \mathcal { T } ^ { j } = \tau \big ( \mathsf { C } ( \mathbb { Z } , \mathcal { A } ) \big ) } \\ & { \mathsf { C } ( \mathbb { Z } , \mathcal { A } ) = \langle \mathbb { Z }  \mathcal { A } , \mathcal { A }  \mathbb { Z } \rangle _ { \odot } } \end{array}
$$

# 页 4
The dual-agent communication design simplifies communications by avoiding complex multi-agent topologies, effectively streamlining the consensusreaching process (Yin et al., 2023; Chen et al., 2023b). Subsequently, the solutions from previous tasks serve as bridges to the next phase, allowing a smooth transition between subtasks. This approach continues until all subtasks are completed. It’s worth noting that the conceptually simple but empirically powerful chain-style structure guides agents on what to communicate, fostering cooperation and smoothly linking natural- and programming-language subtasks. It also offers a transparent view of the entire software development process, allowing for the examination of intermediate solutions and assisting in identifying possible problems.

# 页 5
Agentization To enhance the quality and reduce human intervention, ChatDev implements prompt engineering that only takes place at the start of each subtask round. As soon as the communication phase begins, the instructor and the assistant will communicate with each other in an automated loop, continuing this exchange until the task concludes. However, simply exchanging responses cannot achieve effective multi-round task-oriented communication, since it inevitably faces significant challenges including role flipping, instruction repeating, and fake replies. As a result, there is a failure to advance the progression of productive communications and hinders the achievement of meaningful solutions.

# 页 6
ChatDev thus employs inception prompting mechanism (Li et al., 2023a) for initiating, sustaining, and concluding agents’ communication to guarantee a robust and efficient workflow. This mechanism is composed of the instructor system prompt ${ \sf P } _ { I }$ and the assistant system prompt $\mathsf { P } _ { A }$ . The system prompts for both roles are mostly symmetrical, covering the overview and objectives of the current subtask, specialized roles, accessible external tools, communication protocols, termination conditions, and constraints or requirements to avoid undesirable behaviors. Then, an instructor $\mathcal { T }$ and an assistant $\mathcal { A }$ are instantiated by hypnotizing LLMs via ${ \sf P } _ { I }$ and $\mathsf { P } _ { A }$ :

$$
\mathcal { T } = \rho ( L L M , \mathsf { P } _ { I } ) , \mathcal { A } = \rho ( L L M , \mathsf { P } _ { A } )
$$

where $\rho$ is the role customization operation, implemented via system message assignment.

# 页 7
Memory Note that the limited context length of common LLMs typically restricts the ability to maintain a complete communication history among all agents and phases. To tackle this issue, based on the nature of the chat chain, we accordingly segment the agents’ context memories based on their sequential phases, resulting in two functionally distinct types of memory: short-term memory and long-term memory. Short-term memory is utilized to sustain the continuity of the dialogue within a single phase, while long-term memory is leveraged to preserve contextual awareness across different phases.