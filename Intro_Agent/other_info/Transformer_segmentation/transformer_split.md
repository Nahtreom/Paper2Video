# 页 1
Most competitive neural sequence transduction models have an encoder- decoder structure [5, 2, 35]. Here, the encoder maps an input sequence of symbol representations  $(x_{1},\ldots ,x_{n})$  to a sequence of continuous representations  $\mathbf{z} = (z_{1},\ldots ,z_{n})$ . Given  $\mathbf{z}$ , the decoder then generates an output sequence  $(y_{1},\ldots ,y_{m})$  of symbols one element at a time. At each step the model is auto- regressive [10], consuming the previously generated symbols as additional input when generating the next.

![alt text](transformer_images/image-1.png)  
Figure 1: The Transformer - model architecture.

The Transformer follows this overall architecture using stacked self- attention and point- wise, fully connected layers for both the encoder and decoder, shown in the left and right halves of Figure 1, respectively.

# 页 2
Encoder: The encoder is composed of a stack of  $N = 6$  identical layers. Each layer has two sub- layers. The first is a multi- head self- attention mechanism, and the second is a simple, positionwise fully connected feed- forward network. We employ a residual connection [11] around each of the two sub- layers, followed by layer normalization [1]. That is, the output of each sub- layer is  $\mathrm{LayerNorm}(x + \mathrm{Sublayer}(x))$ , where  $\mathrm{Sublayer}(x)$  is the function implemented by the sub- layer itself. To facilitate these residual connections, all sub- layers in the model, as well as the embedding layers, produce outputs of dimension  $d_{\mathrm{model}} = 512$ .

# 页 3
Decoder: The decoder is also composed of a stack of  $N = 6$  identical layers. In addition to the two sub- layers in each encoder layer, the decoder inserts a third sub- layer, which performs multi- head attention over the output of the encoder stack. Similar to the encoder, we employ residual connections around each of the sub- layers, followed by layer normalization. We also modify the self- attention sub- layer in the decoder stack to prevent positions from attending to subsequent positions. This masking, combined with fact that the output embeddings are offset by one position, ensures that the predictions for position  $i$  can depend only on the known outputs at positions less than  $i$ .

# 页 4
An attention function can be described as mapping a query and a set of key- value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum

![alt text](transformer_images/image.png)  
Figure 2: (left) Scaled Dot-Product Attention. (right) Multi-Head Attention consists of several attention layers running in parallel.

of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key.

# 页 5
We call our particular attention "Scaled Dot- Product Attention" (Figure 2). The input consists of queries and keys of dimension  $d_{k}$ , and values of dimension  $d_{v}$ . We compute the dot products of the query with all keys, divide each by  $\sqrt{d_{k}}$ , and apply a softmax function to obtain the weights on the values.

In practice, we compute the attention function on a set of queries simultaneously, packed together into a matrix  $Q$ . The keys and values are also packed together into matrices  $K$  and  $V$ . We compute the matrix of outputs as:

$$
\mathrm{Attention}(Q,K,V) = \mathrm{softmax}(\frac{QK^T}{\sqrt{d_k}})V \tag{1}
$$

# 页 6
The two most commonly used attention functions are additive attention [2], and dot- product (multiplicative) attention. Dot- product attention is identical to our algorithm, except for the scaling factor of  $\frac{1}{\sqrt{d_{k}}}$ . Additive attention computes the compatibility function using a feed- forward network with a single hidden layer. While the two are similar in theoretical complexity, dot- product attention is much faster and more space- efficient in practice, since it can be implemented using highly optimized matrix multiplication code.

While for small values of  $d_{k}$  the two mechanisms perform similarly, additive attention outperforms dot product attention without scaling for larger values of  $d_{k}$  [3]. We suspect that for large values of  $d_{k}$ , the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients<sup>4</sup>. To counteract this effect, we scale the dot products by  $\frac{1}{\sqrt{d_{k}}}$ .

# 页 7
Instead of performing a single attention function with  $d_{\mathrm{model}}$  - dimensional keys, values and queries, we found it beneficial to linearly project the queries, keys and values  $h$  times with different, learned linear projections to  $d_{k},d_{k}$  and  $d_{v}$  dimensions, respectively. On each of these projected versions of queries, keys and values we then perform the attention function in parallel, yielding  $d_{v}$  - dimensional output values. These are concatenated and once again projected, resulting in the final values, as depicted in Figure 2.

Multi- head attention allows the model to jointly attend to information from different representation subspaces at different positions. With a single attention head, averaging inhibits this.

# 页 8
$$
\begin{array}{rl} & {\mathrm{MultiHead}(Q,K,V) = \mathrm{Constant}(\mathrm{head}_1,\dots,\mathrm{head}_{\mathrm{h}})W^O}\\ & {\qquad \mathrm{where~head}_{\mathrm{i}} = \mathrm{Attention}(QW_i^Q,KW_i^K,VW_i^V)} \end{array}
$$

Where the projections are parameter matrices  $W_{i}^{Q}\in \mathbb{R}^{d_{\mathrm{model}}\times d_{k}}$ $W_{i}^{K}\in \mathbb{R}^{d_{\mathrm{model}}\times d_{k}}$ $W_{i}^{V}\in \mathbb{R}^{d_{\mathrm{model}}\times d_{v}}$  and  $W^{O}\in \mathbb{R}^{h d_{v}\times d_{\mathrm{model}}}$

In this work we employ  $h = 8$  parallel attention layers, or heads. For each of these we use  $d_{k} = d_{v} = d_{\mathrm{model}} / h = 64$ . Due to the reduced dimension of each head, the total computational cost is similar to that of single- head attention with full dimensionality.