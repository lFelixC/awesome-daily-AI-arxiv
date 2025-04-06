# 🔍 3D_Generation Papers · 2025-04-05

[![Total Papers](https://img.shields.io/badge/Papers-4-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[Scene Splatter: Momentum 3D Scene Generation from Single Image with Video Diffusion Model](https://arxiv.org/abs/2504.02764)**  `arXiv:2504.02764`  `cs.CV` `cs.AI`  
  _Shengjun Zhang, Jinzhao Li, Xin Fei, Hao Liu, Yueqi Duan_
  <details open><summary>Abstract</summary>
  In this paper, we propose Scene Splatter, a momentum-based paradigm for video diffusion to generate generic scenes from single image. Existing methods, which employ video generation models to synthesize novel views, suffer from limited video length and scene inconsistency, leading to artifacts and distortions during further reconstruction. To address this issue, we construct noisy samples from original features as momentum to enhance video details and maintain scene consistency. However, for latent features with the perception field that spans both known and unknown regions, such latent-level momentum restricts the generative ability of video diffusion in unknown regions. Therefore, we further introduce the aforementioned consistent video as a pixel-level momentum to a directly generated video without momentum for better recovery of unseen regions. Our cascaded momentum enables video diffusion models to generate both high-fidelity and consistent novel views. We further finetune the global Gaussian representations with enhanced frames and render new frames for momentum update in the next step. In this manner, we can iteratively recover a 3D scene, avoiding the limitation of video length. Extensive experiments demonstrate the generalization capability and superior performance of our method in high-fidelity and consistent scene generation.
  </details>

- **[OmniCam: Unified Multimodal Video Generation via Camera Control](https://arxiv.org/abs/2504.02312)**  `arXiv:2504.02312`  `cs.CV` `cs.AI`  
  _Xiaoda Yang, Jiayang Xu, Kaixuan Luan, Xinyu Zhan, Hongshun Qiu, Shijun Shi, et al._
  <details open><summary>Abstract</summary>
  Camera control, which achieves diverse visual effects by changing camera position and pose, has attracted widespread attention. However, existing methods face challenges such as complex interaction and limited control capabilities. To address these issues, we present OmniCam, a unified multimodal camera control framework. Leveraging large language models and video diffusion models, OmniCam generates spatio-temporally consistent videos. It supports various combinations of input modalities: the user can provide text or video with expected trajectory as camera path guidance, and image or video as content reference, enabling precise control over camera motion. To facilitate the training of OmniCam, we introduce the OmniTr dataset, which contains a large collection of high-quality long-sequence trajectories, videos, and corresponding descriptions. Experimental results demonstrate that our model achieves state-of-the-art performance in high-quality camera-controlled video generation across various metrics.
  </details>

- **[LPA3D: 3D Room-Level Scene Generation from In-the-Wild Images](https://arxiv.org/abs/2504.02337)**  `arXiv:2504.02337`  `cs.CV`  
  _Ming-Jia Yang, Yu-Xiao Guo, Yang Liu, Bin Zhou, Xin Tong_
  <details open><summary>Abstract</summary>
  Generating realistic, room-level indoor scenes with semantically plausible and detailed appearances from in-the-wild images is crucial for various applications in VR, AR, and robotics. The success of NeRF-based generative methods indicates a promising direction to address this challenge. However, unlike their success at the object level, existing scene-level generative methods require additional information, such as multiple views, depth images, or semantic guidance, rather than relying solely on RGB images. This is because NeRF-based methods necessitate prior knowledge of camera poses, which is challenging to approximate for indoor scenes due to the complexity of defining alignment and the difficulty of globally estimating poses from a single image, given the unseen parts behind the camera. To address this challenge, we redefine global poses within the framework of Local-Pose-Alignment (LPA) -- an anchor-based multi-local-coordinate system that uses a selected number of anchors as the roots of these coordinates. Building on this foundation, we introduce LPA-GAN, a novel NeRF-based generative approach that incorporates specific modifications to estimate the priors of camera poses under LPA. It also co-optimizes the pose predictor and scene generation processes. Our ablation study and comparisons with straightforward extensions of NeRF-based object generative methods demonstrate the effectiveness of our approach. Furthermore, visual comparisons with other techniques reveal that our method achieves superior view-to-view consistency and semantic normality.
  </details>

- **[OSV: One Step is Enough for High-Quality Image to Video Generation](https://arxiv.org/abs/2409.11367)**  `arXiv:2409.11367`  `cs.CV`  
  _Xiaofeng Mao, Zhengkai Jiang, Fu-Yun Wang, Jiangning Zhang, Hao Chen, Mingmin Chi, et al._
  <details open><summary>Abstract</summary>
  Video diffusion models have shown great potential in generating high-quality videos, making them an increasingly popular focus. However, their inherent iterative nature leads to substantial computational and time costs. While efforts have been made to accelerate video diffusion by reducing inference steps (through techniques like consistency distillation) and GAN training (these approaches often fall short in either performance or training stability). In this work, we introduce a two-stage training framework that effectively combines consistency distillation with GAN training to address these challenges. Additionally, we propose a novel video discriminator design, which eliminates the need for decoding the video latents and improves the final performance. Our model is capable of producing high-quality videos in merely one-step, with the flexibility to perform multi-step refinement for further performance enhancement. Our quantitative evaluation on the OpenWebVid-1M benchmark shows that our model significantly outperforms existing methods. Notably, our 1-step performance(FVD 171.15) exceeds the 8-step performance of the consistency distillation based method, AnimateLCM (FVD 184.79), and approaches the 25-step performance of advanced Stable Video Diffusion (FVD 156.94).
  </details>
