# 🔍 3D_Generation Papers · 2025-09-05

[![Total Papers](https://img.shields.io/badge/Papers-3-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[Virtual Fitting Room: Generating Arbitrarily Long Videos of Virtual Try-On from a Single Image -- Technical Preview](https://arxiv.org/abs/2509.04450)**  `arXiv:2509.04450`  `cs.CV` `cs.LG`  
  _Jun-Kun Chen, Aayush Bansal, Minh Phuoc Vo, Yu-Xiong Wang_
  <details open><summary>Abstract</summary>
  We introduce the Virtual Fitting Room (VFR), a novel video generative model that produces arbitrarily long virtual try-on videos. Our VFR models long video generation tasks as an auto-regressive, segment-by-segment generation process, eliminating the need for resource-intensive generation and lengthy video data, while providing the flexibility to generate videos of arbitrary length. The key challenges of this task are twofold: ensuring local smoothness between adjacent segments and maintaining global temporal consistency across different segments. To address these challenges, we propose our VFR framework, which ensures smoothness through a prefix video condition and enforces consistency with the anchor video -- a 360-degree video that comprehensively captures the human's wholebody appearance. Our VFR generates minute-scale virtual try-on videos with both local smoothness and global temporal consistency under various motions, making it a pioneering work in long virtual try-on video generation.
  </details>

- **[Conditional Video Generation for High-Efficiency Video Compression](https://arxiv.org/abs/2507.15269)**  `arXiv:2507.15269`  `cs.CV` `cs.AI`  
  _Fangqiu Yi, Jingyu Xu, Jiawei Shao, Chi Zhang, Xuelong Li_
  <details open><summary>Abstract</summary>
  Perceptual studies demonstrate that conditional diffusion models excel at reconstructing video content aligned with human visual perception. Building on this insight, we propose a video compression framework that leverages conditional diffusion models for perceptually optimized reconstruction. Specifically, we reframe video compression as a conditional generation task, where a generative model synthesizes video from sparse, yet informative signals. Our approach introduces three key modules: (1) Multi-granular conditioning that captures both static scene structure and dynamic spatio-temporal cues; (2) Compact representations designed for efficient transmission without sacrificing semantic richness; (3) Multi-condition training with modality dropout and role-aware embeddings, which prevent over-reliance on any single modality and enhance robustness. Extensive experiments show that our method significantly outperforms both traditional and neural codecs on perceptual quality metrics such as Fréchet Video Distance (FVD) and LPIPS, especially under high compression ratios.
  </details>

- **[HLG: Comprehensive 3D Room Construction via Hierarchical Layout Generation](https://arxiv.org/abs/2508.17832)**  `arXiv:2508.17832`  `cs.CV`  
  _Xiping Wang, Yuxi Wang, Mengqi Zhou, Junsong Fan, Zhaoxiang Zhang_
  <details open><summary>Abstract</summary>
  Realistic 3D indoor scene generation is crucial for virtual reality, interior design, embodied intelligence, and scene understanding. While existing methods have made progress in coarse-scale furniture arrangement, they struggle to capture fine-grained object placements, limiting the realism and utility of generated environments. This gap hinders immersive virtual experiences and detailed scene comprehension for embodied AI applications. To address these issues, we propose Hierarchical Layout Generation (HLG), a novel method for fine-grained 3D scene generation. HLG is the first to adopt a coarse-to-fine hierarchical approach, refining scene layouts from large-scale furniture placement to intricate object arrangements. Specifically, our fine-grained layout alignment module constructs a hierarchical layout through vertical and horizontal decoupling, effectively decomposing complex 3D indoor scenes into multiple levels of granularity. Additionally, our trainable layout optimization network addresses placement issues, such as incorrect positioning, orientation errors, and object intersections, ensuring structurally coherent and physically plausible scene generation. We demonstrate the effectiveness of our approach through extensive experiments, showing superior performance in generating realistic indoor scenes compared to existing methods. This work advances the field of scene generation and opens new possibilities for applications requiring detailed 3D environments. We will release our code upon publication to encourage future research.
  </details>
