# 页 1
Most competitive neural sequence transduction models have an encoder- decoder structure [5, 2, 35]. Here, the encoder maps an input sequence of symbol representations  $(x_{1},\ldots ,x_{n})$  to a sequence of continuous representations  $\mathbf{z} = (z_{1},\ldots ,z_{n})$ . Given  $\mathbf{z}$ , the decoder then generates an output sequence  $(y_{1},\ldots ,y_{m})$  of symbols one element at a time. At each step the model is auto- regressive [10], consuming the previously generated symbols as additional input when generating the next.

![alt text](transformer_images/image-1.png)  
Figure 1: The Transformer - model architecture.

The Transformer follows this overall architecture using stacked self- attention and point- wise, fully connected layers for both the encoder and decoder, shown in the left and right halves of Figure 1, respectively.