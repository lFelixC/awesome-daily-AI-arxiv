# 🔍 3D_Generation Papers · 2025-05-07

[![Total Papers](https://img.shields.io/badge/Papers-2-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[HunyuanCustom: A Multimodal-Driven Architecture for Customized Video Generation](https://arxiv.org/abs/2505.04512)**  `arXiv:2505.04512`  `cs.CV`  
  _Teng Hu, Zhentao Yu, Zhengguang Zhou, Sen Liang, Yuan Zhou, Qin Lin, et al._
  <details open><summary>Abstract</summary>
  Customized video generation aims to produce videos featuring specific subjects under flexible user-defined conditions, yet existing methods often struggle with identity consistency and limited input modalities. In this paper, we propose HunyuanCustom, a multi-modal customized video generation framework that emphasizes subject consistency while supporting image, audio, video, and text conditions. Built upon HunyuanVideo, our model first addresses the image-text conditioned generation task by introducing a text-image fusion module based on LLaVA for enhanced multi-modal understanding, along with an image ID enhancement module that leverages temporal concatenation to reinforce identity features across frames. To enable audio- and video-conditioned generation, we further propose modality-specific condition injection mechanisms: an AudioNet module that achieves hierarchical alignment via spatial cross-attention, and a video-driven injection module that integrates latent-compressed conditional video through a patchify-based feature-alignment network. Extensive experiments on single- and multi-subject scenarios demonstrate that HunyuanCustom significantly outperforms state-of-the-art open- and closed-source methods in terms of ID consistency, realism, and text-video alignment. Moreover, we validate its robustness across downstream tasks, including audio and video-driven customized video generation. Our results highlight the effectiveness of multi-modal conditioning and identity-preserving strategies in advancing controllable video generation. All the code and models are available atthis https URL.
  </details>

- **[Replace Anyone in Videos](https://arxiv.org/abs/2409.19911)**  `arXiv:2409.19911`  `cs.CV`  
  _Xiang Wang, Shiwei Zhang, Haonan Qiu, Ruihang Chu, Zekun Li, Yingya Zhang, et al._
  <details open><summary>Abstract</summary>
  The field of controllable human-centric video generation has witnessed remarkable progress, particularly with the advent of diffusion models. However, achieving precise and localized control over human motion in videos, such as replacing or inserting individuals while preserving desired motion patterns, still remains a formidable challenge. In this work, we present the ReplaceAnyone framework, which focuses on localized human replacement and insertion featuring intricate backgrounds. Specifically, we formulate this task as an image-conditioned video inpainting paradigm with pose guidance, utilizing a unified end-to-end video diffusion architecture that facilitates image-conditioned video inpainting within masked regions. To prevent shape leakage and enable granular local control, we introduce diverse mask forms involving both regular and irregular shapes. Furthermore, we implement an enriched visual guidance mechanism to enhance appearance alignment, a hybrid inpainting encoder to further preserve the detailed background information in the masked video, and a two-phase optimization methodology to simplify the training difficulty. ReplaceAnyone enables seamless replacement or insertion of characters while maintaining the desired pose motion and reference appearance within a single framework. Extensive experimental results demonstrate the effectiveness of our method in generating realistic and coherent video content. The proposed ReplaceAnyone can be seamlessly applied not only to traditional 3D-UNet base models but also to DiT-based video models such as Wan2.1. The code will be available atthis https URL.
  </details>
