# 🔍 3D_Generation Papers · 2025-07-15

[![Total Papers](https://img.shields.io/badge/Papers-3-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[Flows and Diffusions on the Neural Manifold](https://arxiv.org/abs/2507.10623)**  `arXiv:2507.10623`  `cs.LG` `cs.CV`  
  _Daniel Saragih, Deyu Cao, Tejas Balaji_
  <details open><summary>Abstract</summary>
  Diffusion and flow-based generative models have achieved remarkable success in domains such as image synthesis, video generation, and natural language modeling. In this work, we extend these advances to weight space learning by leveraging recent techniques to incorporate structural priors derived from optimization dynamics. Central to our approach is modeling the trajectory induced by gradient descent as a trajectory inference problem. We unify several trajectory inference techniques under the framework of gradient flow matching, providing a theoretical framework for treating optimization paths as inductive bias. We further explore architectural and algorithmic choices, including reward fine-tuning by adjoint matching, the use of autoencoders for latent weight representation, conditioning on task-specific context data, and adopting informative source distributions such as Kaiming uniform. Experiments demonstrate that our method matches or surpasses baselines in generating in-distribution weights, improves initialization for downstream training, and supports fine-tuning to enhance performance. Finally, we illustrate a practical application in safety-critical systems: detecting harmful covariate shifts, where our method outperforms the closest comparable baseline.
  </details>

- **[NarrLV: Towards a Comprehensive Narrative-Centric Evaluation for Long Video Generation Models](https://arxiv.org/abs/2507.11245)**  `arXiv:2507.11245`  `cs.CV`  
  _X. Feng, H. Yu, M. Wu, S. Hu, J. Chen, C. Zhu, et al._
  <details open><summary>Abstract</summary>
  With the rapid development of foundation video generation technologies, long video generation models have exhibited promising research potential thanks to expanded content creation space. Recent studies reveal that the goal of long video generation tasks is not only to extend video duration but also to accurately express richer narrative content within longer videos. However, due to the lack of evaluation benchmarks specifically designed for long video generation models, the current assessment of these models primarily relies on benchmarks with simple narrative prompts (e.g., VBench). To the best of our knowledge, our proposed NarrLV is the first benchmark to comprehensively evaluate the Narrative expression capabilities of Long Video generation models. Inspired by film narrative theory, (i) we first introduce the basic narrative unit maintaining continuous visual presentation in videos as Temporal Narrative Atom (TNA), and use its count to quantitatively measure narrative richness. Guided by three key film narrative elements influencing TNA changes, we construct an automatic prompt generation pipeline capable of producing evaluation prompts with a flexibly expandable number of TNAs. (ii) Then, based on the three progressive levels of narrative content expression, we design an effective evaluation metric using the MLLM-based question generation and answering framework. (iii) Finally, we conduct extensive evaluations on existing long video generation models and the foundation generation models. Experimental results demonstrate that our metric aligns closely with human judgments. The derived evaluation outcomes reveal the detailed capability boundaries of current video generation models in narrative content expression.
  </details>

- **[Acquiring and Adapting Priors for Novel Tasks via Neural Meta-Architectures](https://arxiv.org/abs/2507.10446)**  `arXiv:2507.10446`  `cs.AI`  
  _Sudarshan Babu_
  <details open><summary>Abstract</summary>
  The ability to transfer knowledge from prior experiences to novel tasks stands as a pivotal capability of intelligent agents, including both humans and computational models. This principle forms the basis of transfer learning, where large pre-trained neural networks are fine-tuned to adapt to downstream tasks. Transfer learning has demonstrated tremendous success, both in terms of task adaptation speed and performance. However there are several domains where, due to lack of data, training such large pre-trained models or foundational models is not a possibility - computational chemistry, computational immunology, and medical imaging are examples. To address these challenges, our work focuses on designing architectures to enable efficient acquisition of priors when large amounts of data are unavailable. In particular, we demonstrate that we can use neural memory to enable adaptation on non-stationary distributions with only a few samples. Then we demonstrate that our hypernetwork designs (a network that generates another network) can acquire more generalizable priors than standard networks when trained with Model Agnostic Meta-Learning (MAML). Subsequently, we apply hypernetworks to 3D scene generation, demonstrating that they can acquire priors efficiently on just a handful of training scenes, thereby leading to faster text-to-3D generation. We then extend our hypernetwork framework to perform 3D segmentation on novel scenes with limited data by efficiently transferring priors from earlier viewed scenes. Finally, we repurpose an existing molecular generative method as a pre-training framework that facilitates improved molecular property prediction, addressing critical challenges in computational immunology.
  </details>
