# 🔍 Embodied_AI Papers · 2025-07-29

[![Total Papers](https://img.shields.io/badge/Papers-3-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[VLA-Touch: Enhancing Vision-Language-Action Models with Dual-Level Tactile Feedback](https://arxiv.org/abs/2507.17294)**  `arXiv:2507.17294`  `cs.RO` `cs.LG`  
  _Jianxin Bi, Kevin Yuchen Ma, Ce Hao, Mike Zheng Shou, Harold Soh_
  <details open><summary>Abstract</summary>
  Tactile feedback is generally recognized to be crucial for effective interaction with the physical world. However, state-of-the-art Vision-Language-Action (VLA) models lack the ability to interpret and use tactile signals, limiting their effectiveness in contact-rich tasks. Incorporating tactile feedback into these systems is challenging due to the absence of large multi-modal datasets. We present VLA-Touch, an approach that enhances generalist robot policies with tactile sensing \emph{without fine-tuning} the base VLA. Our method introduces two key innovations: (1) a pipeline that leverages a pretrained tactile-language model that provides semantic tactile feedback for high-level task planning, and (2) a diffusion-based controller that refines VLA-generated actions with tactile signals for contact-rich manipulation. Through real-world experiments, we demonstrate that our dual-level integration of tactile feedback improves task planning efficiency while enhancing execution precision. Code is open-sourced at \href{this https URL}{this URL}.
  </details>

- **[OPAL: Encoding Causal Understanding of Physical Systems for Robot Learning](https://arxiv.org/abs/2504.06538)**  `arXiv:2504.06538`  `cs.RO` `cs.AI`  
  _Daniel Tcheurekdjian, Joshua Klasmeier, Tom Cooney, Christopher McCann, Tyler Fenstermaker_
  <details open><summary>Abstract</summary>
  We present OPAL (Operant Physical Agent with Language), a novel vision-language-action architecture that introduces topological constraints to flow matching for robotic control. To do so, we further introduce topological attention. Our approach models action sequences as topologically-structured representations with non-trivial constraints. Experimental results across 10 complex manipulation tasks demonstrate OPAL's superior performance compared to previous approaches, including Octo, OpenVLA, and ${\pi}$0.Our architecture achieves significant improvements in zero-shot performance without requiring task-specific fine-tuning, while reducing inference computational requirements by 42%. The theoretical guarantees provided by our topological approach result in more coherent long-horizon action sequences. Our results highlight the potential of constraining the search space of learning problems in robotics by deriving from fundamental physical laws, and the possibility of using topological attention to embed causal understanding into transformer architectures.
  </details>

- **[Improving Visual Place Recognition with Sequence-Matching Receptiveness Prediction](https://arxiv.org/abs/2503.06840)**  `arXiv:2503.06840`  `cs.CV`  
  _Somayeh Hussaini, Tobias Fischer, Michael Milford_
  <details open><summary>Abstract</summary>
  In visual place recognition (VPR), filtering and sequence-based matching approaches can improve performance by integrating temporal information across image sequences, especially in challenging conditions. While these methods are commonly applied, their effects on system behavior can be unpredictable and can actually make performance worse in certain situations. In this work, we present a new supervised learning approach that learns to predict the per-frame sequence matching receptiveness (SMR) of VPR techniques, enabling the system to selectively decide when to trust the output of a sequence matching system. Our approach is agnostic to the underlying VPR technique and effectively predicts SMR, and hence significantly improves VPR performance across a large range of state-of-the-art and classical VPR techniques (namely CosPlace, MixVPR, EigenPlaces, SALAD, AP-GeM, NetVLAD and SAD), and across three benchmark VPR datasets (Nordland, Oxford RobotCar, and SFU-Mountain). We also provide insights into a complementary approach that uses the predictor to replace discarded matches, and present ablation studies including an analysis of the interactions between our SMR predictor and the selected sequence length.
  </details>
