# 页 8
$$
\begin{array}{rl} & {\mathrm{MultiHead}(Q,K,V) = \mathrm{Constant}(\mathrm{head}_1,\dots,\mathrm{head}_{\mathrm{h}})W^O}\\ & {\qquad \mathrm{where~head}_{\mathrm{i}} = \mathrm{Attention}(QW_i^Q,KW_i^K,VW_i^V)} \end{array}
$$

Where the projections are parameter matrices  $W_{i}^{Q}\in \mathbb{R}^{d_{\mathrm{model}}\times d_{k}}$ $W_{i}^{K}\in \mathbb{R}^{d_{\mathrm{model}}\times d_{k}}$ $W_{i}^{V}\in \mathbb{R}^{d_{\mathrm{model}}\times d_{v}}$  and  $W^{O}\in \mathbb{R}^{h d_{v}\times d_{\mathrm{model}}}$

In this work we employ  $h = 8$  parallel attention layers, or heads. For each of these we use  $d_{k} = d_{v} = d_{\mathrm{model}} / h = 64$ . Due to the reduced dimension of each head, the total computational cost is similar to that of single- head attention with full dimensionality.