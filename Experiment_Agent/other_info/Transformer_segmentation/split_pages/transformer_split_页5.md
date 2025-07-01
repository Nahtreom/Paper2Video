# 页 5
We call our particular attention "Scaled Dot- Product Attention" (Figure 2). The input consists of queries and keys of dimension  $d_{k}$ , and values of dimension  $d_{v}$ . We compute the dot products of the query with all keys, divide each by  $\sqrt{d_{k}}$ , and apply a softmax function to obtain the weights on the values.

In practice, we compute the attention function on a set of queries simultaneously, packed together into a matrix  $Q$ . The keys and values are also packed together into matrices  $K$  and  $V$ . We compute the matrix of outputs as:

$$
\mathrm{Attention}(Q,K,V) = \mathrm{softmax}(\frac{QK^T}{\sqrt{d_k}})V \tag{1}
$$