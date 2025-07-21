# 🔍 Embodied_AI Papers · 2025-07-20

[![Total Papers](https://img.shields.io/badge/Papers-3-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[EdgeVLA: Efficient Vision-Language-Action Models](https://arxiv.org/abs/2507.14049)**  `arXiv:2507.14049`  `cs.RO` `cs.CL`  
  _Paweł Budzianowski, Wesley Maa, Matthew Freed, Jingxiang Mo, Winston Hsiao, Aaron Xie, et al._
  <details open><summary>Abstract</summary>
  Vision-Language Models (VLMs) have emerged as a promising approach to address the data scarcity challenge in robotics, enabling the development of generalizable visuomotor control policies. While models like OpenVLA showcase the potential of this paradigm, deploying large-scale VLMs on resource-constrained mobile manipulation systems remains a significant hurdle. This paper introduces Edge VLA (EVLA), a novel approach designed to significantly enhance the inference speed of Vision-Language-Action (VLA) models. EVLA maintains the representational power of these models while enabling real-time performance on edge devices. We achieve this through two key innovations: 1) Eliminating the autoregressive requirement for end-effector position prediction, leading to a 7x speedup in inference, and 2) Leveraging the efficiency of Small Language Models (SLMs), demonstrating comparable training performance to larger models with significantly reduced computational demands. Our early results demonstrate that EVLA achieves comparable training characteristics to OpenVLA while offering substantial gains in inference speed and memory efficiency. We release our model checkpoints and training \href{this https URL}{codebase} to foster further research.
  </details>

- **[EgoVLA: Learning Vision-Language-Action Models from Egocentric Human Videos](https://arxiv.org/abs/2507.12440)**  `arXiv:2507.12440`  `cs.RO` `cs.AI` `cs.CV` `cs.LG`  
  _Ruihan Yang, Qinxi Yu, Yecheng Wu, Rui Yan, Borui Li, An-Chieh Cheng, et al._
  <details open><summary>Abstract</summary>
  Real robot data collection for imitation learning has led to significant advancements in robotic manipulation. However, the requirement for robot hardware in the process fundamentally constrains the scale of the data. In this paper, we explore training Vision-Language-Action (VLA) models using egocentric human videos. The benefit of using human videos is not only for their scale but more importantly for the richness of scenes and tasks. With a VLA trained on human video that predicts human wrist and hand actions, we can perform Inverse Kinematics and retargeting to convert the human actions to robot actions. We fine-tune the model using a few robot manipulation demonstrations to obtain the robot policy, namely EgoVLA. We propose a simulation benchmark called Ego Humanoid Manipulation Benchmark, where we design diverse bimanual manipulation tasks with demonstrations. We fine-tune and evaluate EgoVLA with Ego Humanoid Manipulation Benchmark and show significant improvements over baselines and ablate the importance of human data. Videos can be found on our website:this https URL
  </details>

- **[VLA-Mark: A cross modal watermark for large vision-language alignment model](https://arxiv.org/abs/2507.14067)**  `arXiv:2507.14067`  `cs.CV` `cs.AI`  
  _Shuliang Liu, Qi Zheng, Jesse Jiaxi Xu, Yibo Yan, He Geng, Aiwei Liu, et al._
  <details open><summary>Abstract</summary>
  Vision-language models demand watermarking solutions that protect intellectual property without compromising multimodal coherence. Existing text watermarking methods disrupt visual-textual alignment through biased token selection and static strategies, leaving semantic-critical concepts vulnerable. We propose VLA-Mark, a vision-aligned framework that embeds detectable watermarks while preserving semantic fidelity through cross-modal coordination. Our approach integrates multiscale visual-textual alignment metrics, combining localized patch affinity, global semantic coherence, and contextual attention patterns, to guide watermark injection without model retraining. An entropy-sensitive mechanism dynamically balances watermark strength and semantic preservation, prioritizing visual grounding during low-uncertainty generation phases. Experiments show 7.4% lower PPL and 26.6% higher BLEU than conventional methods, with near-perfect detection (98.8% AUC). The framework demonstrates 96.1\% attack resilience against attacks such as paraphrasing and synonym substitution, while maintaining text-visual consistency, establishing new standards for quality-preserving multimodal watermarking
  </details>
