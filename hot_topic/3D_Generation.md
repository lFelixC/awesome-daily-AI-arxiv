# 🔍 3D_Generation Papers · 2025-07-27

[![Total Papers](https://img.shields.io/badge/Papers-3-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[MagicDrive3D: Controllable 3D Generation for Any-View Rendering in Street Scenes](https://arxiv.org/abs/2405.14475)**  `arXiv:2405.14475`  `cs.CV` `cs.AI`  
  _Ruiyuan Gao, Kai Chen, Zhihao Li, Lanqing Hong, Zhenguo Li, Qiang Xu_
  <details open><summary>Abstract</summary>
  Controllable generative models for images and videos have seen significant success, yet 3D scene generation, especially in unbounded scenarios like autonomous driving, remains underdeveloped. Existing methods lack flexible controllability and often rely on dense view data collection in controlled environments, limiting their generalizability across common datasets (e.g., nuScenes). In this paper, we introduce MagicDrive3D, a novel framework for controllable 3D street scene generation that combines video-based view synthesis with 3D representation (3DGS) generation. It supports multi-condition control, including road maps, 3D objects, and text descriptions. Unlike previous approaches that require 3D representation before training, MagicDrive3D first trains a multi-view video generation model to synthesize diverse street views. This method utilizes routinely collected autonomous driving data, reducing data acquisition challenges and enriching 3D scene generation. In the 3DGS generation step, we introduce Fault-Tolerant Gaussian Splatting to address minor errors and use monocular depth for better initialization, alongside appearance modeling to manage exposure discrepancies across viewpoints. Experiments show that MagicDrive3D generates diverse, high-quality 3D driving scenes, supports any-view rendering, and enhances downstream tasks like BEV segmentation, demonstrating its potential for autonomous driving simulation and beyond.
  </details>

- **[ScenePainter: Semantically Consistent Perpetual 3D Scene Generation with Concept Relation Alignment](https://arxiv.org/abs/2507.19058)**  `arXiv:2507.19058`  `cs.CV`  
  _Chong Xia, Shengjun Zhang, Fangfu Liu, Chang Liu, Khodchaphun Hirunyaratsameewong, Yueqi Duan_
  <details open><summary>Abstract</summary>
  Perpetual 3D scene generation aims to produce long-range and coherent 3D view sequences, which is applicable for long-term video synthesis and 3D scene reconstruction. Existing methods follow a "navigate-and-imagine" fashion and rely on outpainting for successive view expansion. However, the generated view sequences suffer from semantic drift issue derived from the accumulated deviation of the outpainting module. To tackle this challenge, we propose ScenePainter, a new framework for semantically consistent 3D scene generation, which aligns the outpainter's scene-specific prior with the comprehension of the current scene. To be specific, we introduce a hierarchical graph structure dubbed SceneConceptGraph to construct relations among multi-level scene concepts, which directs the outpainter for consistent novel views and can be dynamically refined to enhance diversity. Extensive experiments demonstrate that our framework overcomes the semantic drift issue and generates more consistent and immersive 3D view sequences. Project Page:this https URL.
  </details>

- **[MagicDrive-V2: High-Resolution Long Video Generation for Autonomous Driving with Adaptive Control](https://arxiv.org/abs/2411.13807)**  `arXiv:2411.13807`  `cs.CV`  
  _Ruiyuan Gao, Kai Chen, Bo Xiao, Lanqing Hong, Zhenguo Li, Qiang Xu_
  <details open><summary>Abstract</summary>
  The rapid advancement of diffusion models has greatly improved video synthesis, especially in controllable video generation, which is vital for applications like autonomous driving. Although DiT with 3D VAE has become a standard framework for video generation, it introduces challenges in controllable driving video generation, especially for geometry control, rendering existing control methods ineffective. To address these issues, we propose MagicDrive-V2, a novel approach that integrates the MVDiT block and spatial-temporal conditional encoding to enable multi-view video generation and precise geometric control. Additionally, we introduce an efficient method for obtaining contextual descriptions for videos to support diverse textual control, along with a progressive training strategy using mixed video data to enhance training efficiency and generalizability. Consequently, MagicDrive-V2 enables multi-view driving video synthesis with $3.3\times$ resolution and $4\times$ frame count (compared to current SOTA), rich contextual control, and geometric controls. Extensive experiments demonstrate MagicDrive-V2's ability, unlocking broader applications in autonomous driving.
  </details>
