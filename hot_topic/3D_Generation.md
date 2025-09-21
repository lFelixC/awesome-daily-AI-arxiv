# 🔍 3D_Generation Papers · 2025-09-20

[![Total Papers](https://img.shields.io/badge/Papers-3-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[BWCache: Accelerating Video Diffusion Transformers through Block-Wise Caching](https://arxiv.org/abs/2509.13789)**  `arXiv:2509.13789`  `cs.CV` `cs.AI`  
  _Hanshuai Cui, Zhiqing Tang, Zhifei Xu, Zhi Yao, Wenyi Zeng, Weijia Jia_
  <details open><summary>Abstract</summary>
  Recent advancements in Diffusion Transformers (DiTs) have established them as the state-of-the-art method for video generation. However, their inherently sequential denoising process results in inevitable latency, limiting real-world applicability. Existing acceleration methods either compromise visual quality due to architectural modifications or fail to reuse intermediate features at proper granularity. Our analysis reveals that DiT blocks are the primary contributors to inference latency. Across diffusion timesteps, the feature variations of DiT blocks exhibit a U-shaped pattern with high similarity during intermediate timesteps, which suggests substantial computational redundancy. In this paper, we propose Block-Wise Caching (BWCache), a training-free method to accelerate DiT-based video generation. BWCache dynamically caches and reuses features from DiT blocks across diffusion timesteps. Furthermore, we introduce a similarity indicator that triggers feature reuse only when the differences between block features at adjacent timesteps fall below a threshold, thereby minimizing redundant computations while maintaining visual fidelity. Extensive experiments on several video diffusion models demonstrate that BWCache achieves up to 2.24$\times$ speedup with comparable visual quality.
  </details>

- **[DACoN: DINO for Anime Paint Bucket Colorization with Any Number of Reference Images](https://arxiv.org/abs/2509.14685)**  `arXiv:2509.14685`  `cs.CV`  
  _Kazuma Nagata, Naoshi Kaneko_
  <details open><summary>Abstract</summary>
  Automatic colorization of line drawings has been widely studied to reduce the labor cost of hand-drawn anime production. Deep learning approaches, including image/video generation and feature-based correspondence, have improved accuracy but struggle with occlusions, pose variations, and viewpoint changes. To address these challenges, we propose DACoN, a framework that leverages foundation models to capture part-level semantics, even in line drawings. Our method fuses low-resolution semantic features from foundation models with high-resolution spatial features from CNNs for fine-grained yet robust feature extraction. In contrast to previous methods that rely on the Multiplex Transformer and support only one or two reference images, DACoN removes this constraint, allowing any number of references. Quantitative and qualitative evaluations demonstrate the benefits of using multiple reference images, achieving superior colorization performance. Our code and model are available atthis https URL.
  </details>

- **[The Art of Storytelling: Multi-Agent Generative AI for Dynamic Multimodal Narratives](https://arxiv.org/abs/2409.11261)**  `arXiv:2409.11261`  `cs.CL`  
  _Samee Arif, Taimoor Arif, Muhammad Saad Haroon, Aamina Jamal Khan, Agha Ali Raza, Awais Athar_
  <details open><summary>Abstract</summary>
  This paper introduces the concept of an education tool that utilizes Generative Artificial Intelligence (GenAI) to enhance storytelling. We evaluate GenAI-driven narrative co-creation, text-to-speech conversion, text-to-music and text-to-video generation to produce an engaging experience for learners. We describe the co-creation process, the adaptation of narratives into spoken words using text-to-speech models, and the transformation of these narratives into contextually relevant visuals through text-to-video technology. Our evaluation covers the linguistics of the generated stories, the text-to-speech conversion quality, and the accuracy of the generated visuals.
  </details>
