# 🔍 3D_Generation Papers · 2025-07-01

[![Total Papers](https://img.shields.io/badge/Papers-3-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[Populate-A-Scene: Affordance-Aware Human Video Generation](https://arxiv.org/abs/2507.00334)**  `arXiv:2507.00334`  `cs.CV`  
  _Mengyi Shan, Zecheng He, Haoyu Ma, Felix Juefei-Xu, Peizhao Zhang, Tingbo Hou, et al._
  <details open><summary>Abstract</summary>
  Can a video generation model be repurposed as an interactive world simulator? We explore the affordance perception potential of text-to-video models by teaching them to predict human-environment interaction. Given a scene image and a prompt describing human actions, we fine-tune the model to insert a person into the scene, while ensuring coherent behavior, appearance, harmonization, and scene affordance. Unlike prior work, we infer human affordance for video generation (i.e., where to insert a person and how they should behave) from a single scene image, without explicit conditions like bounding boxes or body poses. An in-depth study of cross-attention heatmaps demonstrates that we can uncover the inherent affordance perception of a pre-trained video model without labeled affordance datasets.
  </details>

- **[FreeLong++: Training-Free Long Video Generation via Multi-band SpectralFusion](https://arxiv.org/abs/2507.00162)**  `arXiv:2507.00162`  `cs.CV`  
  _Yu Lu, Yi Yang_
  <details open><summary>Abstract</summary>
  Recent advances in video generation models have enabled high-quality short video generation from text prompts. However, extending these models to longer videos remains a significant challenge, primarily due to degraded temporal consistency and visual fidelity. Our preliminary observations show that naively applying short-video generation models to longer sequences leads to noticeable quality degradation. Further analysis identifies a systematic trend where high-frequency components become increasingly distorted as video length grows, an issue we term high-frequency distortion. To address this, we propose FreeLong, a training-free framework designed to balance the frequency distribution of long video features during the denoising process. FreeLong achieves this by blending global low-frequency features, which capture holistic semantics across the full video, with local high-frequency features extracted from short temporal windows to preserve fine details. Building on this, FreeLong++ extends FreeLong dual-branch design into a multi-branch architecture with multiple attention branches, each operating at a distinct temporal scale. By arranging multiple window sizes from global to local, FreeLong++ enables multi-band frequency fusion from low to high frequencies, ensuring both semantic continuity and fine-grained motion dynamics across longer video sequences. Without any additional training, FreeLong++ can be plugged into existing video generation models (e.g. Wan2.1 and LTX-Video) to produce longer videos with substantially improved temporal consistency and visual fidelity. We demonstrate that our approach outperforms previous methods on longer video generation tasks (e.g. 4x and 8x of native length). It also supports coherent multi-prompt video generation with smooth scene transitions and enables controllable video generation using long depth or pose sequences.
  </details>

- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007)**  `arXiv:2502.07007`  `cs.CV`  
  _Siwei Meng, Yawei Luo, Ping Liu_
  <details open><summary>Abstract</summary>
  Recent advancements in AI-generated content have significantly improved the realism of 3D and 4D generation. However, most existing methods prioritize appearance consistency while neglecting underlying physical principles, leading to artifacts such as unrealistic deformations, unstable dynamics, and implausible objects interactions. Incorporating physics priors into generative models has become a crucial research direction to enhance structural integrity and motion realism. This survey provides a review of physics-aware generative methods, systematically analyzing how physical constraints are integrated into 3D and 4D generation. First, we examine recent works in incorporating physical priors into static and dynamic 3D generation, categorizing methods based on representation types, including vision-based, NeRF-based, and Gaussian Splatting-based approaches. Second, we explore emerging techniques in 4D generation, focusing on methods that model temporal dynamics with physical simulations. Finally, we conduct a comparative analysis of major methods, highlighting their strengths, limitations, and suitability for different materials and motion dynamics. By presenting an in-depth analysis of physics-grounded AIGC, this survey aims to bridge the gap between generative models and physical realism, providing insights that inspire future research in physically consistent content generation.
  </details>
