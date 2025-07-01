# 页 13
To perceive dialogues through previous phases, the chat chain only transmits the solutions from previous phases as long-term memories $\tilde { \mathcal { M } }$ , integrating them at the start of the next phase and enabling the cross-phase transmission of long dialogues:  
$$
\mathcal { I } _ { 1 } ^ { i + 1 } = \tilde { \mathcal { M } } ^ { i } \cup \mathsf { P } _ { \mathcal { Z } } ^ { i + 1 } , ~ \tilde { \mathcal { M } } ^ { i } = \bigcup _ { j = 1 } ^ { i } \tau ( \mathcal { M } _ { | \mathcal { M } ^ { j } | } ^ { j } )
$$  
where $\mathsf { P }$ symbolizes a predetermined prompt that appears exclusively at the start of each phase.