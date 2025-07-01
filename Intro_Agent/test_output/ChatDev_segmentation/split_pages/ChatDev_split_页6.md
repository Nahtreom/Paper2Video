# 页 6
ChatDev thus employs inception prompting mechanism (Li et al., 2023a) for initiating, sustaining, and concluding agents’ communication to guarantee a robust and efficient workflow. This mechanism is composed of the instructor system prompt ${ \sf P } _ { I }$ and the assistant system prompt $\mathsf { P } _ { A }$ . The system prompts for both roles are mostly symmetrical, covering the overview and objectives of the current subtask, specialized roles, accessible external tools, communication protocols, termination conditions, and constraints or requirements to avoid undesirable behaviors. Then, an instructor $\mathcal { T }$ and an assistant $\mathcal { A }$ are instantiated by hypnotizing LLMs via ${ \sf P } _ { I }$ and $\mathsf { P } _ { A }$ :

$$
\mathcal { T } = \rho ( L L M , \mathsf { P } _ { I } ) , \mathcal { A } = \rho ( L L M , \mathsf { P } _ { A } )
$$

where $\rho$ is the role customization operation, implemented via system message assignment.