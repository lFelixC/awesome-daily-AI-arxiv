# 🔍 Embodied_AI Papers · 2025-07-04

[![Total Papers](https://img.shields.io/badge/Papers-3-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[cVLA: Towards Efficient Camera-Space VLAs](https://arxiv.org/abs/2507.02190)**  `arXiv:2507.02190`  `cs.RO` `cs.LG`  
  _Max Argus, Jelena Bratulic, Houman Masnavi, Maxim Velikanov, Nick Heppert, Abhinav Valada, et al._
  <details open><summary>Abstract</summary>
  Vision-Language-Action (VLA) models offer a compelling framework for tackling complex robotic manipulation tasks, but they are often expensive to train. In this paper, we propose a novel VLA approach that leverages the competitive performance of Vision Language Models (VLMs) on 2D images to directly infer robot end-effector poses in image frame coordinates. Unlike prior VLA models that output low-level controls, our model predicts trajectory waypoints, making it both more efficient to train and robot embodiment agnostic. Despite its lightweight design, our next-token prediction architecture effectively learns meaningful and executable robot trajectories. We further explore the underutilized potential of incorporating depth images, inference-time techniques such as decoding strategies, and demonstration-conditioned action generation. Our model is trained on a simulated dataset and exhibits strong sim-to-real transfer capabilities. We evaluate our approach using a combination of simulated and real data, demonstrating its effectiveness on a real robotic system.
  </details>

- **[TriVLA: A Triple-System-Based Unified Vision-Language-Action Model for General Robot Control](https://arxiv.org/abs/2507.01424)**  `arXiv:2507.01424`  `cs.RO`  
  _Zhenyang Liu, Yongchong Gu, Sixiao Zheng, Xiangyang Xue, Yanwei Fu_
  <details open><summary>Abstract</summary>
  Recent advancements in vision-language models (VLMs) for common-sense reasoning have led to the development of vision-language-action (VLA) models, enabling robots to perform generalized manipulation. Although existing autoregressive VLA methods design a specific architecture like dual-system to leverage large-scale pretrained knowledge, they tend to capture static information, often neglecting the dynamic aspects vital for embodied tasks. To this end, we propose TriVLA, a unified Vision-Language-Action model with a triple-system architecture for general robot control. The vision-language module (System 2) interprets the environment through vision and language instructions. The dynamics perception module (System 3) inherently produces visual representations that encompass both current static information and predicted future dynamics, thereby providing valuable guidance for policy learning. TriVLA utilizes pre-trained VLM model and fine-tunes pre-trained video foundation model on robot datasets along with internet human manipulation data. The subsequent policy learning module (System 1) generates fluid motor actions in real time. Experimental evaluation demonstrates that TriVLA operates at approximately 36 Hz and surpasses state-of-the-art imitation learning baselines on standard simulation benchmarks as well as challenging real-world manipulation tasks.
  </details>

- **[DexVLG: Dexterous Vision-Language-Grasp Model at Scale](https://arxiv.org/abs/2507.02747)**  `arXiv:2507.02747`  `cs.CV` `cs.RO`  
  _Jiawei He, Danshi Li, Xinqiang Yu, Zekun Qi, Wenyao Zhang, Jiayi Chen, et al._
  <details open><summary>Abstract</summary>
  As large models gain traction, vision-language-action (VLA) systems are enabling robots to tackle increasingly complex tasks. However, limited by the difficulty of data collection, progress has mainly focused on controlling simple gripper end-effectors. There is little research on functional grasping with large models for human-like dexterous hands. In this paper, we introduce DexVLG, a large Vision-Language-Grasp model for Dexterous grasp pose prediction aligned with language instructions using single-view RGBD input. To accomplish this, we generate a dataset of 170 million dexterous grasp poses mapped to semantic parts across 174,000 objects in simulation, paired with detailed part-level captions. This large-scale dataset, named DexGraspNet 3.0, is used to train a VLM and flow-matching-based pose head capable of producing instruction-aligned grasp poses for tabletop objects. To assess DexVLG's performance, we create benchmarks in physics-based simulations and conduct real-world experiments. Extensive testing demonstrates DexVLG's strong zero-shot generalization capabilities-achieving over 76% zero-shot execution success rate and state-of-the-art part-grasp accuracy in simulation-and successful part-aligned grasps on physical objects in real-world scenarios.
  </details>
