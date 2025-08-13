# 🔍 Embodied_AI Papers · 2025-08-12

[![Total Papers](https://img.shields.io/badge/Papers-4-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[GeoVLA: Empowering 3D Representations in Vision-Language-Action Models](https://arxiv.org/abs/2508.09071)**  `arXiv:2508.09071`  `cs.RO`  
  _Lin Sun, Bin Xie, Yingfei Liu, Hao Shi, Tiancai Wang, Jiale Cao_
  <details open><summary>Abstract</summary>
  Vision-Language-Action (VLA) models have emerged as a promising approach for enabling robots to follow language instructions and predict correspondingthis http URL, current VLA models mainly rely on 2D visual inputs, neglecting the rich geometric information in the 3D physical world, which limits their spatial awareness and adaptability. In this paper, we present GeoVLA, a novel VLA framework that effectively integrates 3D information to advance robotic manipulation. It uses a vision-language model (VLM) to process images and language instructions,extracting fused vision-language embeddings. In parallel, it converts depth maps into point clouds and employs a customized point encoder, called Point Embedding Network, to generate 3D geometric embeddings independently. These produced embeddings are then concatenated and processed by our proposed spatial-aware action expert, called 3D-enhanced Action Expert, which combines information from different sensor modalities to produce precise action sequences. Through extensive experiments in both simulation and real-world environments, GeoVLA demonstrates superior performance and robustness. It achieves state-of-the-art results in the LIBERO and ManiSkill2 simulation benchmarks and shows remarkable robustness in real-world tasks requiring height adaptability, scale awareness and viewpoint invariance.
  </details>

- **[OmniVTLA: Vision-Tactile-Language-Action Model with Semantic-Aligned Tactile Sensing](https://arxiv.org/abs/2508.08706)**  `arXiv:2508.08706`  `cs.RO`  
  _Zhengxue Cheng, Yiqian Zhang, Wenkang Zhang, Haoyu Li, Keyu Wang, Li Song, et al._
  <details open><summary>Abstract</summary>
  Recent vision-language-action (VLA) models build upon vision-language foundations, and have achieved promising results and exhibit the possibility of task generalization in robot manipulation. However, due to the heterogeneity of tactile sensors and the difficulty of acquiring tactile data, current VLA models significantly overlook the importance of tactile perception and fail in contact-rich tasks. To address this issue, this paper proposes OmniVTLA, a novel architecture involving tactile sensing. Specifically, our contributions are threefold. First, our OmniVTLA features a dual-path tactile encoder framework. This framework enhances tactile perception across diverse vision-based and force-based tactile sensors by using a pretrained vision transformer (ViT) and a semantically-aligned tactile ViT (SA-ViT). Second, we introduce ObjTac, a comprehensive force-based tactile dataset capturing textual, visual, and tactile information for 56 objects across 10 categories. With 135K tri-modal samples, ObjTac supplements existing visuo-tactile datasets. Third, leveraging this dataset, we train a semantically-aligned tactile encoder to learn a unified tactile representation, serving as a better initialization for OmniVTLA. Real-world experiments demonstrate substantial improvements over state-of-the-art VLA baselines, achieving 96.9% success rates with grippers, (21.9% higher over baseline) and 100% success rates with dexterous hands (6.2% higher over baseline) in pick-and-place tasks. Besides, OmniVTLA significantly reduces task completion time and generates smoother trajectories through tactile sensing compared to existing VLA.
  </details>

- **[Spatial Traces: Enhancing VLA Models with Spatial-Temporal Understanding](https://arxiv.org/abs/2508.09032)**  `arXiv:2508.09032`  `cs.CV` `cs.AI` `cs.RO`  
  _Maxim A. Patratskiy, Alexey K. Kovalev, Aleksandr I. Panov_
  <details open><summary>Abstract</summary>
  Vision-Language-Action models have demonstrated remarkable capabilities in predicting agent movements within virtual environments and real-world scenarios based on visual observations and textual instructions. Although recent research has focused on enhancing spatial and temporal understanding independently, this paper presents a novel approach that integrates both aspects through visual prompting. We introduce a method that projects visual traces of key points from observations onto depth maps, enabling models to capture both spatial and temporal information simultaneously. The experiments in SimplerEnv show that the mean number of tasks successfully solved increased for 4% compared to SpatialVLA and 19% compared to TraceVLA. Furthermore, we show that this enhancement can be achieved with minimal training data, making it particularly valuable for real-world applications where data collection is challenging. The project page is available atthis https URL.
  </details>

- **[IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model](https://arxiv.org/abs/2508.06571)**  `arXiv:2508.06571`  `cs.AI` `cs.CV` `cs.RO`  
  _Anqing Jiang, Yu Gao, Yiru Wang, Zhigang Sun, Shuo Wang, Yuwen Heng, et al._
  <details open><summary>Abstract</summary>
  Vision-Language-Action (VLA) models have demonstrated potential in autonomous driving. However, two critical challenges hinder their development: (1) Existing VLA architectures are typically based on imitation learning in open-loop setup which tends to capture the recorded behaviors in the dataset, leading to suboptimal and constrained performance, (2) Close-loop training relies heavily on high-fidelity sensor simulation, where domain gaps and computational inefficiencies pose significant barriers. In this paper, we introduce IRL-VLA, a novel close-loop Reinforcement Learning via \textbf{I}nverse \textbf{R}einforcement \textbf{L}earning reward world model with a self-built VLA approach. Our framework proceeds in a three-stage paradigm: In the first stage, we propose a VLA architecture and pretrain the VLA policy via imitation learning. In the second stage, we construct a lightweight reward world model via inverse reinforcement learning to enable efficient close-loop reward computation. To further enhance planning performance, finally, we design specialized reward world model guidence reinforcement learning via PPO(Proximal Policy Optimization) to effectively balance the safety incidents, comfortable driving, and traffic efficiency. Our approach achieves state-of-the-art performance in NAVSIM v2 end-to-end driving benchmark, 1st runner up in CVPR2025 Autonomous Grand Challenge. We hope that our framework will accelerate VLA research in close-loop autonomous driving.
  </details>
