# 🔍 Embodied_AI Papers · 2025-08-20

[![Total Papers](https://img.shields.io/badge/Papers-1-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[MinD: Learning A Dual-System World Model for Real-Time Planning and Implicit Risk Analysis](https://arxiv.org/abs/2506.18897)**  `arXiv:2506.18897`  `cs.RO` `cs.AI`  
  _Xiaowei Chi, Kuangzhi Ge, Jiaming Liu, Siyuan Zhou, Peidong Jia, Zichen He, et al._
  <details open><summary>Abstract</summary>
  Video Generation Models (VGMs) have become powerful backbones for Vision-Language-Action (VLA) models, leveraging large-scale pretraining for robust dynamics modeling. However, current methods underutilize their distribution modeling capabilities for predicting future states. Two challenges hinder progress: integrating generative processes into feature learning is both technically and conceptually underdeveloped, and naive frame-by-frame video diffusion is computationally inefficient for real-time robotics. To address these, we propose Manipulate in Dream (MinD), a dual-system world model for real-time, risk-aware planning. MinD uses two asynchronous diffusion processes: a low-frequency visual generator (LoDiff) that predicts future scenes and a high-frequency diffusion policy (HiDiff) that outputs actions. Our key insight is that robotic policies do not require fully denoised frames but can rely on low-resolution latents generated in a single denoising step. To connect early predictions to actions, we introduce DiffMatcher, a video-action alignment module with a novel co-training strategy that synchronizes the two diffusion models. MinD achieves a 63% success rate on RL-Bench, 60% on real-world Franka tasks, and operates at 11.3 FPS, demonstrating the efficiency of single-step latent features for control signals. Furthermore, MinD identifies 74% of potential task failures in advance, providing real-time safety signals for monitoring and intervention. This work establishes a new paradigm for efficient and reliable robotic manipulation using generative world models.
  </details>
