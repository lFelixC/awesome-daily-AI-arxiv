# 🔍 3D_Generation Papers · 2025-07-06

[![Total Papers](https://img.shields.io/badge/Papers-4-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[RefTok: Reference-Based Tokenization for Video Generation](https://arxiv.org/abs/2507.02862)**  `arXiv:2507.02862`  `cs.CV`  
  _Xiang Fan, Xiaohang Sun, Kushan Thakkar, Zhu Liu, Vimal Bhat, Ranjay Krishna, et al._
  <details open><summary>Abstract</summary>
  Effectively handling temporal redundancy remains a key challenge in learning video models. Prevailing approaches often treat each set of frames independently, failing to effectively capture the temporal dependencies and redundancies inherent in videos. To address this limitation, we introduce RefTok, a novel reference-based tokenization method capable of capturing complex temporal dynamics and contextual information. Our method encodes and decodes sets of frames conditioned on an unquantized reference frame. When decoded, RefTok preserves the continuity of motion and the appearance of objects across frames. For example, RefTok retains facial details despite head motion, reconstructs text correctly, preserves small patterns, and maintains the legibility of handwriting from the context. Across 4 video datasets (K600, UCF-101, BAIR Robot Pushing, and DAVIS), RefTok significantly outperforms current state-of-the-art tokenizers (Cosmos and MAGVIT) and improves all evaluated metrics (PSNR, SSIM, LPIPS) by an average of 36.7% at the same or higher compression ratios. When a video generation model is trained using RefTok's latents on the BAIR Robot Pushing task, the generations not only outperform MAGVIT-B but the larger MAGVIT-L, which has 4x more parameters, across all generation metrics by an average of 27.9%.
  </details>

- **[Less is Enough: Training-Free Video Diffusion Acceleration via Runtime-Adaptive Caching](https://arxiv.org/abs/2507.02860)**  `arXiv:2507.02860`  `cs.CV`  
  _Xin Zhou, Dingkang Liang, Kaijin Chen, Tianrui Feng, Xiwu Chen, Hongkai Lin, et al._
  <details open><summary>Abstract</summary>
  Video generation models have demonstrated remarkable performance, yet their broader adoption remains constrained by slow inference speeds and substantial computational costs, primarily due to the iterative nature of the denoising process. Addressing this bottleneck is essential for democratizing advanced video synthesis technologies and enabling their integration into real-world applications. This work proposes EasyCache, a training-free acceleration framework for video diffusion models. EasyCache introduces a lightweight, runtime-adaptive caching mechanism that dynamically reuses previously computed transformation vectors, avoiding redundant computations during inference. Unlike prior approaches, EasyCache requires no offline profiling, pre-computation, or extensive parameter tuning. We conduct comprehensive studies on various large-scale video generation models, including OpenSora, Wan2.1, and HunyuanVideo. Our method achieves leading acceleration performance, reducing inference time by up to 2.1-3.3$\times$ compared to the original baselines while maintaining high visual fidelity with a significant up to 36% PSNR improvement compared to the previous SOTA method. This improvement makes our EasyCache a efficient and highly accessible solution for high-quality video generation in both research and practical applications. The code is available atthis https URL.
  </details>

- **[AnyI2V: Animating Any Conditional Image with Motion Control](https://arxiv.org/abs/2507.02857)**  `arXiv:2507.02857`  `cs.CV`  
  _Ziye Li, Hao Luo, Xincheng Shuai, Henghui Ding_
  <details open><summary>Abstract</summary>
  Recent advancements in video generation, particularly in diffusion models, have driven notable progress in text-to-video (T2V) and image-to-video (I2V) synthesis. However, challenges remain in effectively integrating dynamic motion signals and flexible spatial constraints. Existing T2V methods typically rely on text prompts, which inherently lack precise control over the spatial layout of generated content. In contrast, I2V methods are limited by their dependence on real images, which restricts the editability of the synthesized content. Although some methods incorporate ControlNet to introduce image-based conditioning, they often lack explicit motion control and require computationally expensive training. To address these limitations, we propose AnyI2V, a training-free framework that animates any conditional images with user-defined motion trajectories. AnyI2V supports a broader range of modalities as the conditional image, including data types such as meshes and point clouds that are not supported by ControlNet, enabling more flexible and versatile video generation. Additionally, it supports mixed conditional inputs and enables style transfer and editing via LoRA and text prompts. Extensive experiments demonstrate that the proposed AnyI2V achieves superior performance and provides a new perspective in spatial- and motion-controlled video generation. Code is available atthis https URL.
  </details>

- **[Self-Guidance: Boosting Flow and Diffusion Generation on Their Own](https://arxiv.org/abs/2412.05827)**  `arXiv:2412.05827`  `cs.CV`  
  _Tiancheng Li, Weijian Luo, Zhiyang Chen, Liyuan Ma, Guo-Jun Qi_
  <details open><summary>Abstract</summary>
  Proper guidance strategies are essential to achieve high-quality generation results without retraining diffusion and flow-based text-to-image models. Existing guidance either requires specific training or strong inductive biases of diffusion model networks, potentially limiting their applications. Motivated by the observation that artifact outliers can be detected by a significant decline in the density from a noisier to a cleaner noise level, we propose Self-Guidance (SG), which improves the image quality by suppressing the generation of low-quality samples. SG only relies on the sampling probabilities of its own diffusion model at different noise levels with no need of any guidance-specific training. This makes it flexible to be used in a plug-and-play manner with other sampling algorithms. We also introduce a more efficient approximation of SG, named SG-prev, which reuses the output from the immediately previous diffusion step to avoid doubling sampling time. We conduct experiments on text-to-image and text-to-video generation with different architectures, including UNet and transformer models. With open-sourced diffusion models such as Stable Diffusion 3.5 and FLUX, SG exceeds existing algorithms on multiple metrics, including both FID and Human Preference Score. SG-prev also achieves strong results over both the baseline and the SG with only one forward pass. Moreover, we find that SG and SG-prev both have a surprisingly positive effect on the generation of physiologically correct human body structures such as hands, faces, and arms, showing their ability of eliminating human body artifacts with minimal efforts. We will release our code along with this paper.
  </details>
