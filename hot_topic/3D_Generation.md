# 🔍 3D_Generation Papers · 2025-07-30

[![Total Papers](https://img.shields.io/badge/Papers-6-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[LoReUn: Data Itself Implicitly Provides Cues to Improve Machine Unlearning](https://arxiv.org/abs/2507.22499)**  `arXiv:2507.22499`  `cs.LG` `cs.AI`  
  _Xiang Li, Qianli Shen, Haonan Wang, Kenji Kawaguchi_
  <details open><summary>Abstract</summary>
  Recent generative models face significant risks of producing harmful content, which has underscored the importance of machine unlearning (MU) as a critical technique for eliminating the influence of undesired data. However, existing MU methods typically assign the same weight to all data to be forgotten, which makes it difficult to effectively forget certain data that is harder to unlearn than others. In this paper, we empirically demonstrate that the loss of data itself can implicitly reflect its varying difficulty. Building on this insight, we introduce Loss-based Reweighting Unlearning (LoReUn), a simple yet effective plug-and-play strategy that dynamically reweights data during the unlearning process with minimal additional computational overhead. Our approach significantly reduces the gap between existing MU methods and exact unlearning in both image classification and generation tasks, effectively enhancing the prevention of harmful content generation in text-to-image diffusion models.
  </details>

- **[Scaling RL to Long Videos](https://arxiv.org/abs/2507.07966)**  `arXiv:2507.07966`  `cs.CV` `cs.AI` `cs.CL`  
  _Yukang Chen, Wei Huang, Baifeng Shi, Qinghao Hu, Hanrong Ye, Ligeng Zhu, et al._
  <details open><summary>Abstract</summary>
  We introduce a full-stack framework that scales up reasoning in vision-language models (VLMs) to long videos, leveraging reinforcement learning. We address the unique challenges of long video reasoning by integrating three critical components: (1) a large-scale dataset, LongVideo-Reason, comprising 104K long video QA pairs with high-quality reasoning annotations across diverse domains such as sports, games, and vlogs; (2) a two-stage training pipeline that extends VLMs with chain-of-thought supervised fine-tuning (CoT-SFT) and reinforcement learning (RL); and (3) a training infrastructure for long video RL, named Multi-modal Reinforcement Sequence Parallelism (MR-SP), which incorporates sequence parallelism and a vLLM-based engine tailored for long video, using cached video embeddings for efficient rollout and prefilling. In our experiments, LongVILA-R1-7B achieves strong performance on video benchmarks, reaching 65.1% and 71.1% accuracy on VideoMME without and with subtitles, respectively, and consistently outperforming LongVILA-7B across multiple benchmarks. Moreover, LongVILA-R1-7B supports processing up to 8,192 video frames per video, and configurable FPS settings. Notably, our MR-SP system achieves up to 2.1x speedup on long video RL training. In addition, we release our training system for public availability that supports RL training on various modalities (video, text, and audio), various models (VILA and Qwen series), and even image and video generation models. On a single A100 node (8 GPUs), it supports RL training on hour-long videos (e.g., 3,600 frames).
  </details>

- **[GVD: Guiding Video Diffusion Model for Scalable Video Distillation](https://arxiv.org/abs/2507.22360)**  `arXiv:2507.22360`  `cs.CV` `cs.AI`  
  _Kunyang Li, Jeffrey A Chan Santiago, Sarinda Dhanesh Samarasinghe, Gaowen Liu, Mubarak Shah_
  <details open><summary>Abstract</summary>
  To address the larger computation and storage requirements associated with large video datasets, video dataset distillation aims to capture spatial and temporal information in a significantly smaller dataset, such that training on the distilled data has comparable performance to training on all of the data. We propose GVD: Guiding Video Diffusion, the first diffusion-based video distillation method. GVD jointly distills spatial and temporal features, ensuring high-fidelity video generation across diverse actions while capturing essential motion information. Our method's diverse yet representative distillations significantly outperform previous state-of-the-art approaches on the MiniUCF and HMDB51 datasets across 5, 10, and 20 Instances Per Class (IPC). Specifically, our method achieves 78.29 percent of the original dataset's performance using only 1.98 percent of the total number of frames in MiniUCF. Additionally, it reaches 73.83 percent of the performance with just 3.30 percent of the frames in HMDB51. Experimental results across benchmark video datasets demonstrate that GVD not only achieves state-of-the-art performance but can also generate higher resolution videos and higher IPC without significantly increasing computational cost.
  </details>

- **[Ultra3D: Efficient and High-Fidelity 3D Generation with Part Attention](https://arxiv.org/abs/2507.17745)**  `arXiv:2507.17745`  `cs.CV` `cs.AI`  
  _Yiwen Chen, Zhihao Li, Yikai Wang, Hu Zhang, Qin Li, Chi Zhang, et al._
  <details open><summary>Abstract</summary>
  Recent advances in sparse voxel representations have significantly improved the quality of 3D content generation, enabling high-resolution modeling with fine-grained geometry. However, existing frameworks suffer from severe computational inefficiencies due to the quadratic complexity of attention mechanisms in their two-stage diffusion pipelines. In this work, we propose Ultra3D, an efficient 3D generation framework that significantly accelerates sparse voxel modeling without compromising quality. Our method leverages the compact VecSet representation to efficiently generate a coarse object layout in the first stage, reducing token count and accelerating voxel coordinate prediction. To refine per-voxel latent features in the second stage, we introduce Part Attention, a geometry-aware localized attention mechanism that restricts attention computation within semantically consistent part regions. This design preserves structural continuity while avoiding unnecessary global attention, achieving up to 6.7x speed-up in latent generation. To support this mechanism, we construct a scalable part annotation pipeline that converts raw meshes into part-labeled sparse voxels. Extensive experiments demonstrate that Ultra3D supports high-resolution 3D generation at 1024 resolution and achieves state-of-the-art performance in both visual fidelity and user preference.
  </details>

- **[Graph-Guided Dual-Level Augmentation for 3D Scene Segmentation](https://arxiv.org/abs/2507.22668)**  `arXiv:2507.22668`  `cs.CV`  
  _Hongbin Lin, Yifan Jiang, Juangui Xu, Jesse Jiaxi Xu, Yi Lu, Zhengyu Hu, et al._
  <details open><summary>Abstract</summary>
  3D point cloud segmentation aims to assign semantic labels to individual points in a scene for fine-grained spatial understanding. Existing methods typically adopt data augmentation to alleviate the burden of large-scale annotation. However, most augmentation strategies only focus on local transformations or semantic recomposition, lacking the consideration of global structural dependencies within scenes. To address this limitation, we propose a graph-guided data augmentation framework with dual-level constraints for realistic 3D scene synthesis. Our method learns object relationship statistics from real-world data to construct guiding graphs for scene generation. Local-level constraints enforce geometric plausibility and semantic consistency between objects, while global-level constraints maintain the topological structure of the scene by aligning the generated layout with the guiding graph. Extensive experiments on indoor and outdoor datasets demonstrate that our framework generates diverse and high-quality augmented scenes, leading to consistent improvements in point cloud segmentation performance across various models.
  </details>

- **[SteerX: Creating Any Camera-Free 3D and 4D Scenes with Geometric Steering](https://arxiv.org/abs/2503.12024)**  `arXiv:2503.12024`  `cs.CV`  
  _Byeongjun Park, Hyojun Go, Hyelin Nam, Byung-Hoon Kim, Hyungjin Chung, Changick Kim_
  <details open><summary>Abstract</summary>
  Recent progress in 3D/4D scene generation emphasizes the importance of physical alignment throughout video generation and scene reconstruction. However, existing methods improve the alignment separately at each stage, making it difficult to manage subtle misalignments arising from another stage. Here, we present SteerX, a zero-shot inference-time steering method that unifies scene reconstruction into the generation process, tilting data distributions toward better geometric alignment. To this end, we introduce two geometric reward functions for 3D/4D scene generation by using pose-free feed-forward scene reconstruction models. Through extensive experiments, we demonstrate the effectiveness of SteerX in improving 3D/4D scene generation.
  </details>
