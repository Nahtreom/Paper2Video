# 页 1
We introduce ChatDev, a chat-powered softwaredevelopment framework that integrates multiple "software agents" with various social roles (e.g., requirements analysts, professional programmers and test engineers) collaborating in the core phases of the software life cycle, see Figure 1. Technically, to facilitate cooperative communication, ChatDev introduces chat chain to further break down each phase into smaller and manageable subtasks, which guides multi-turn communications between different roles to propose and validate solutions for each subtask. In addition, to alleviate unexpected hallucinations, a communicative pattern named communicative dehallucination is devised, wherein agents request more detailed information before responding directly and then continue the next round of communication based on these details.

# 页 2
![](ChatDev_images/79021ce9de0bd97d75fc696a609821851154d2323b1123cd2b2b71870afbd198.jpg)  
Figure 1: ChatDev, a chat-powered software development framework, integrates LLM agents with various social roles, working autonomously to develop comprehensive solutions via multi-agent collaboration.

# 页 3
Although LLMs show a good understanding of natural and programming languages, efficiently transforming textual requirements into functional software in a single step remains a significant challenge. ChatDev thus adopts the core principles of the waterfall model, using a chat chain $( \mathcal { C } )$ with sequential phases $( \mathcal { P } )$ , each comprising sequential subtasks $( \mathcal { T } )$ . Specifically, ChatDev segments the software development process into three sequential phases: design, coding, and testing. The coding phase is further subdivided into subtasks of code writing and completion, and the testing phase is segmented into code review (static testing) and system testing (dynamic testing), as illustrated in Figure 2.

# 页 4
In every subtask, two agents, each with their own specialized roles (e.g., a reviewer skilled at identifying endless loops and a programmer adept in GUI design), perform the functions of an instructor $( { \mathcal { T } } )$ and an assistant $( \mathcal { A } )$ . The instructor agent initiates instructions, instructing $(  )$ the discourse toward the completion of the subtask, while the assistant agent adheres to these instructions and responds with $( \sim )$ appropriate solutions. They engage in a multi-turn dialogue (C), working cooperatively until they achieve consensus, extracting $( \tau )$ solutions that can range from the text (e.g., defining a software function point) to code (e.g., creating the initial version of source code), ultimately leading to the completion of the subtask. 

# 页 5
The entire tasksolving process along the agentic workflow can be formulated as:  
$$
\begin{array} { r l } & { \mathcal { C } = \langle \mathcal { P } ^ { 1 } , \mathcal { P } ^ { 2 } , \dotsc , \mathcal { P } ^ { | \mathcal { C } | } \rangle } \\ & { \mathcal { P } ^ { i } = \langle \mathcal { T } ^ { 1 } , \mathcal { T } ^ { 2 } , \dotsc , \mathcal { T } ^ { | \mathcal { P } ^ { i } | } \rangle } \\ & { \mathcal { T } ^ { j } = \tau \big ( \mathsf { C } ( \mathbb { Z } , \mathcal { A } ) \big ) } \\ & { \mathsf { C } ( \mathbb { Z } , \mathcal { A } ) = \langle \mathbb { Z }  \mathcal { A } , \mathcal { A }  \mathbb { Z } \rangle _ { \odot } } \end{array}
$$ 

# 页 6
The dual-agent communication design simplifies communications by avoiding complex multi-agent topologies, effectively streamlining the consensusreaching process (Yin et al., 2023; Chen et al., 2023b). Subsequently, the solutions from previous tasks serve as bridges to the next phase, allowing a smooth transition between subtasks. This approach continues until all subtasks are completed. It’s worth noting that the conceptually simple but empirically powerful chain-style structure guides agents on what to communicate, fostering cooperation and smoothly linking natural- and programming-language subtasks. It also offers a transparent view of the entire software development process, allowing for the examination of intermediate solutions and assisting in identifying possible problems.  

# 页 7
Agentization To enhance the quality and reduce human intervention, ChatDev implements prompt engineering that only takes place at the start of each subtask round. As soon as the communication phase begins, the instructor and the assistant will communicate with each other in an automated loop, continuing this exchange until the task concludes. However, simply exchanging responses cannot achieve effective multi-round task-oriented communication, since it inevitably faces significant challenges including role flipping, instruction repeating, and fake replies. As a result, there is a failure to advance the progression of productive communications and hinders the achievement of meaningful solutions. 

# 页 8
ChatDev thus employs inception prompting mechanism (Li et al., 2023a) for initiating, sustaining, and concluding agents’ communication to guarantee a robust and efficient workflow. This mechanism is composed of the instructor system prompt ${ \sf P } _ { I }$ and the assistant system prompt $\mathsf { P } _ { A }$ . The system prompts for both roles are mostly symmetrical, covering the overview and objectives of the current subtask, specialized roles, accessible external tools, communication protocols, termination conditions, and constraints or requirements to avoid undesirable behaviors. Then, an instructor $\mathcal { T }$ and an assistant $\mathcal { A }$ are instantiated by hypnotizing LLMs via ${ \sf P } _ { I }$ and $\mathsf { P } _ { A }$ :  

# 页 9
$$
\mathcal { T } = \rho ( L L M , \mathsf { P } _ { I } ) , \mathcal { A } = \rho ( L L M , \mathsf { P } _ { A } )
$$  
where $\rho$ is the role customization operation, implemented via system message assignment.  

# 页 10
Memory Note that the limited context length of common LLMs typically restricts the ability to maintain a complete communication history among all agents and phases. To tackle this issue, based on the nature of the chat chain, we accordingly segment the agents’ context memories based on their sequential phases, resulting in two functionally distinct types of memory: short-term memory and long-term memory. Short-term memory is utilized to sustain the continuity of the dialogue within a single phase, while long-term memory is leveraged to preserve contextual awareness across different phases.  

# 页 11
Formally, short-term memory records an agent’s current phase utterances, aiding context-aware decision-making. At the time $t$ during phase ${ \mathcal { P } } ^ { i }$ , we use $\mathcal { T } _ { t } ^ { i }$ to represent the instructor’s instruction and $\mathcal { A } _ { t } ^ { i }$ for the assistant’s response. The short-term memory $\mathcal { M }$ collects utterances up to time $t$ as:  
$$
\mathcal { M } _ { t } ^ { i } = \langle ( \mathcal { T } _ { 1 } ^ { i } , \mathcal { A } _ { 1 } ^ { i } ) , ( \mathcal { T } _ { 2 } ^ { i } , \mathcal { A } _ { 2 } ^ { i } ) , \dots , ( \mathcal { T } _ { t } ^ { i } , \mathcal { A } _ { t } ^ { i } ) \rangle
$$  

# 页 12
In the next time step $t + 1$ , the instructor utilizes the current memory to generate a new instruction $\mathcal { T } _ { t + 1 } ^ { i }$ , which is then conveyed to the assistant to produce a new response $\mathcal { A } _ { t + 1 } ^ { i }$ . The short-term memory iteratively updates until the number of communications reaches the upper limit $| \mathcal { M } ^ { i } |$ :  
$$
\begin{array} { r } { \mathscr { T } _ { t + 1 } ^ { i } = \mathscr { T } ( \mathcal { M } _ { t } ^ { i } ) , \ \mathscr { A } _ { t + 1 } ^ { i } = \mathscr { A } ( \mathcal { M } _ { t } ^ { i } , \mathscr { T } _ { t + 1 } ^ { i } ) } \\ { \mathscr { M } _ { t + 1 } ^ { i } = \mathscr { M } _ { t } ^ { i } \cup ( \mathscr { T } _ { t + 1 } ^ { i } , \mathscr { A } _ { t + 1 } ^ { i } ) \quad } \end{array}
$$

# 页 13
To perceive dialogues through previous phases, the chat chain only transmits the solutions from previous phases as long-term memories $\tilde { \mathcal { M } }$ , integrating them at the start of the next phase and enabling the cross-phase transmission of long dialogues:  
$$
\mathcal { I } _ { 1 } ^ { i + 1 } = \tilde { \mathcal { M } } ^ { i } \cup \mathsf { P } _ { \mathcal { Z } } ^ { i + 1 } , ~ \tilde { \mathcal { M } } ^ { i } = \bigcup _ { j = 1 } ^ { i } \tau ( \mathcal { M } _ { | \mathcal { M } ^ { j } | } ^ { j } )
$$  
where $\mathsf { P }$ symbolizes a predetermined prompt that appears exclusively at the start of each phase. 

# 页 14
By sharing only the solutions of each subtask rather than the entire communication history, ChatDev minimizes the risk of being overwhelmed by too much information, enhancing concentration on each task and encouraging more targeted cooperation, while simultaneously facilitating cross-phase context continuity.

# 页 15
LLM hallucinations manifest when models generate outputs that are nonsensical, factually incorrect, or inaccurate (Dhuliawala et al., 2023; Zhang et al., 2023b). This issue is particularly concerning in software development, where programming languages demand precise syntax—the absence of even a single line can lead to system failure. We have observed that LLMs often produce coding hallucinations, which encompass potential issues like incomplete implementations, unexecutable code, and inconsistencies that don’t meet requirements.

# 页 16
Coding hallucinations frequently appear when the assistant struggles to precisely follow instructions, often due to the vagueness and generality of certain instructions that require multiple adjustments, making it challenging for agents to achieve full compliance. Inspired by this, we introduce communicative dehallucination, which encourages the assistant to actively seek more detailed suggestions from the instructor before delivering a formal response.

# 页 17
Specifically, a vanilla communication pattern between the assistant and the instructor follows a straightforward instruction-response format:  
$$
\langle \mathcal { T } \to \mathcal { A } , \mathcal { A } \sim \mathcal { T } \rangle _ { \mathcal { O } }
$$

# 页 18
In contrast, our communicative dehallucination mechanism features a deliberate "role reversal", where the assistant takes on an instructor-like role, proactively seeking more specific information (e.g., the precise name of an external dependency and its related class) before delivering a conclusive response. After the instructor provides a specific modification suggestion, the assistant proceeds to perform precise optimization:  
$$
\langle \mathcal { T } \to \mathcal { A } , \langle \mathcal { A } \to \mathcal { I } , \mathcal { I } \sim \mathcal { A } \rangle _ { \odot } , \mathcal { A } \sim \mathcal { I } \rangle _ { \odot }
$$  

# 页 19
Since this mechanism tackles one concrete issue at a time, it requires multiple rounds of communication to optimize various potential problems. The communication pattern instructs agents on how to communicate, enabling finer-grained information exchange for effective solution optimization, which practically aids in reducing coding hallucinations.