# 🔍 3D_Generation Papers · 2025-09-09

[![Total Papers](https://img.shields.io/badge/Papers-3-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[Conditional Video Generation for High-Efficiency Video Compression](https://arxiv.org/abs/2507.15269)**  `arXiv:2507.15269`  `cs.CV` `cs.AI`  
  _Fangqiu Yi, Jingyu Xu, Jiawei Shao, Chi Zhang, Xuelong Li_
  <details open><summary>Abstract</summary>
  Perceptual studies demonstrate that conditional diffusion models excel at reconstructing video content aligned with human visual perception. Building on this insight, we propose a video compression framework that leverages conditional diffusion models for perceptually optimized reconstruction. Specifically, we reframe video compression as a conditional generation task, where a generative model synthesizes video from sparse, yet informative signals. Our approach introduces three key modules: (1) Multi-granular conditioning that captures both static scene structure and dynamic spatio-temporal cues; (2) Compact representations designed for efficient transmission without sacrificing semantic richness; (3) Multi-condition training with modality dropout and role-aware embeddings, which prevent over-reliance on any single modality and enhance robustness. Extensive experiments show that our method significantly outperforms both traditional and neural codecs on perceptual quality metrics such as Fréchet Video Distance (FVD) and LPIPS, especially under high compression ratios.
  </details>

- **[ANYPORTAL: Zero-Shot Consistent Video Background Replacement](https://arxiv.org/abs/2509.07472)**  `arXiv:2509.07472`  `cs.CV`  
  _Wenshuo Gao, Xicheng Lan, Shuai Yang_
  <details open><summary>Abstract</summary>
  Despite the rapid advancements in video generation technology, creating high-quality videos that precisely align with user intentions remains a significant challenge. Existing methods often fail to achieve fine-grained control over video details, limiting their practical applicability. We introduce ANYPORTAL, a novel zero-shot framework for video background replacement that leverages pre-trained diffusion models. Our framework collaboratively integrates the temporal prior of video diffusion models with the relighting capabilities of image diffusion models in a zero-shot setting. To address the critical challenge of foreground consistency, we propose a Refinement Projection Algorithm, which enables pixel-level detail manipulation to ensure precise foreground preservation. ANYPORTAL is training-free and overcomes the challenges of achieving foreground consistency and temporally coherent relighting. Experimental results demonstrate that ANYPORTAL achieves high-quality results on consumer-grade GPUs, offering a practical and efficient solution for video content creation and editing.
  </details>

- **[Coefficients-Preserving Sampling for Reinforcement Learning with Flow Matching](https://arxiv.org/abs/2509.05952)**  `arXiv:2509.05952`  `cs.CV`  
  _Feng Wang, Zihao Yu_
  <details open><summary>Abstract</summary>
  Reinforcement Learning (RL) has recently emerged as a powerful technique for improving image and video generation in Diffusion and Flow Matching models, specifically for enhancing output quality and alignment with prompts. A critical step for applying online RL methods on Flow Matching is the introduction of stochasticity into the deterministic framework, commonly realized by Stochastic Differential Equation (SDE). Our investigation reveals a significant drawback to this approach: SDE-based sampling introduces pronounced noise artifacts in the generated images, which we found to be detrimental to the reward learning process. A rigorous theoretical analysis traces the origin of this noise to an excess of stochasticity injected during inference. To address this, we draw inspiration from Denoising Diffusion Implicit Models (DDIM) to reformulate the sampling process. Our proposed method, Coefficients-Preserving Sampling (CPS), eliminates these noise artifacts. This leads to more accurate reward modeling, ultimately enabling faster and more stable convergence for reinforcement learning-based optimizers like Flow-GRPO and Dance-GRPO. Code will be released atthis https URL
  </details>
