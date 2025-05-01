# 🔍 3D_Generation Papers · 2025-04-30

[![Total Papers](https://img.shields.io/badge/Papers-3-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[BEVWorld: A Multimodal World Simulator for Autonomous Driving via Scene-Level BEV Latents](https://arxiv.org/abs/2407.05679)**  `arXiv:2407.05679`  `cs.CV` `cs.AI`  
  _Yumeng Zhang, Shi Gong, Kaixin Xiong, Xiaoqing Ye, Xiaofan Li, Xiao Tan, et al._
  <details open><summary>Abstract</summary>
  World models have attracted increasing attention in autonomous driving for their ability to forecast potential future scenarios. In this paper, we propose BEVWorld, a novel framework that transforms multimodal sensor inputs into a unified and compact Bird's Eye View (BEV) latent space for holistic environment modeling. The proposed world model consists of two main components: a multi-modal tokenizer and a latent BEV sequence diffusion model. The multi-modal tokenizer first encodes heterogeneous sensory data, and its decoder reconstructs the latent BEV tokens into LiDAR and surround-view image observations via ray-casting rendering in a self-supervised manner. This enables joint modeling and bidirectional encoding-decoding of panoramic imagery and point cloud data within a shared spatial representation. On top of this, the latent BEV sequence diffusion model performs temporally consistent forecasting of future scenes, conditioned on high-level action tokens, enabling scene-level reasoning over time. Extensive experiments demonstrate the effectiveness of BEVWorld on autonomous driving benchmarks, showcasing its capability in realistic future scene generation and its benefits for downstream tasks such as perception and motion prediction.
  </details>

- **[HoloTime: Taming Video Diffusion Models for Panoramic 4D Scene Generation](https://arxiv.org/abs/2504.21650)**  `arXiv:2504.21650`  `cs.CV`  
  _Haiyang Zhou, Wangbo Yu, Jiawen Guan, Xinhua Cheng, Yonghong Tian, Li Yuan_
  <details open><summary>Abstract</summary>
  The rapid advancement of diffusion models holds the promise of revolutionizing the application of VR and AR technologies, which typically require scene-level 4D assets for user experience. Nonetheless, existing diffusion models predominantly concentrate on modeling static 3D scenes or object-level dynamics, constraining their capacity to provide truly immersive experiences. To address this issue, we propose HoloTime, a framework that integrates video diffusion models to generate panoramic videos from a single prompt or reference image, along with a 360-degree 4D scene reconstruction method that seamlessly transforms the generated panoramic video into 4D assets, enabling a fully immersive 4D experience for users. Specifically, to tame video diffusion models for generating high-fidelity panoramic videos, we introduce the 360World dataset, the first comprehensive collection of panoramic videos suitable for downstream 4D scene reconstruction tasks. With this curated dataset, we propose Panoramic Animator, a two-stage image-to-video diffusion model that can convert panoramic images into high-quality panoramic videos. Following this, we present Panoramic Space-Time Reconstruction, which leverages a space-time depth estimation method to transform the generated panoramic videos into 4D point clouds, enabling the optimization of a holistic 4D Gaussian Splatting representation to reconstruct spatially and temporally consistent 4D scenes. To validate the efficacy of our method, we conducted a comparative analysis with existing approaches, revealing its superiority in both panoramic video generation and 4D scene reconstruction. This demonstrates our method's capability to create more engaging and realistic immersive environments, thereby enhancing user experiences in VR and AR applications.
  </details>

- **[DyST-XL: Dynamic Layout Planning and Content Control for Compositional Text-to-Video Generation](https://arxiv.org/abs/2504.15032)**  `arXiv:2504.15032`  `cs.CV`  
  _Weijie He, Mushui Liu, Yunlong Yu, Zhao Wang, Chao Wu_
  <details open><summary>Abstract</summary>
  Compositional text-to-video generation, which requires synthesizing dynamic scenes with multiple interacting entities and precise spatial-temporal relationships, remains a critical challenge for diffusion-based models. Existing methods struggle with layout discontinuity, entity identity drift, and implausible interaction dynamics due to unconstrained cross-attention mechanisms and inadequate physics-aware reasoning. To address these limitations, we propose DyST-XL, a \textbf{training-free} framework that enhances off-the-shelf text-to-video models (e.g., CogVideoX-5B) through frame-aware control. DyST-XL integrates three key innovations: (1) A Dynamic Layout Planner that leverages large language models (LLMs) to parse input prompts into entity-attribute graphs and generates physics-aware keyframe layouts, with intermediate frames interpolated via trajectory optimization; (2) A Dual-Prompt Controlled Attention Mechanism that enforces localized text-video alignment through frame-aware attention masking, achieving precise control over individual entities; and (3) An Entity-Consistency Constraint strategy that propagates first-frame feature embeddings to subsequent frames during denoising, preserving object identity without manual annotation. Experiments demonstrate that DyST-XL excels in compositional text-to-video generation, significantly improving performance on complex prompts and bridging a crucial gap in training-free video synthesis. The code is released inthis https URL.
  </details>
