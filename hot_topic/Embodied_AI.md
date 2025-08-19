# 🔍 Embodied_AI Papers · 2025-08-18

[![Total Papers](https://img.shields.io/badge/Papers-4-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy](https://arxiv.org/abs/2508.13103)**  `arXiv:2508.13103`  `cs.RO` `cs.CV`  
  _Tianyi Zhang, Haonan Duan, Haoran Hao, Yu Qiao, Jifeng Dai, Zhi Hou_
  <details open><summary>Abstract</summary>
  Vision-Language-Action (VLA) models frequently encounter challenges in generalizing to real-world environments due to inherent discrepancies between observation and action spaces. Although training data are collected from diverse camera perspectives, the models typically predict end-effector poses within the robot base coordinate frame, resulting in spatial inconsistencies. To mitigate this limitation, we introduce the Observation-Centric VLA (OC-VLA) framework, which grounds action predictions directly in the camera observation space. Leveraging the camera's extrinsic calibration matrix, OC-VLA transforms end-effector poses from the robot base coordinate system into the camera coordinate system, thereby unifying prediction targets across heterogeneous viewpoints. This lightweight, plug-and-play strategy ensures robust alignment between perception and action, substantially improving model resilience to camera viewpoint variations. The proposed approach is readily compatible with existing VLA architectures, requiring no substantial modifications. Comprehensive evaluations on both simulated and real-world robotic manipulation tasks demonstrate that OC-VLA accelerates convergence, enhances task success rates, and improves cross-view generalization. The code will be publicly available.
  </details>

- **[Improving Pre-Trained Vision-Language-Action Policies with Model-Based Search](https://arxiv.org/abs/2508.12211)**  `arXiv:2508.12211`  `cs.RO` `cs.AI`  
  _Cyrus Neary, Omar G. Younis, Artur Kuramshin, Ozgur Aslan, Glen Berseth_
  <details open><summary>Abstract</summary>
  Pre-trained vision-language-action (VLA) models offer a promising foundation for generalist robot policies, but often produce brittle behaviours or unsafe failures when deployed zero-shot in out-of-distribution scenarios. We present Vision-Language-Action Planning & Search (VLAPS) -- a novel framework and accompanying algorithms that embed model-based search into the inference procedure of pre-trained VLA policies to improve their performance on robotic tasks. Specifically, our method biases a modified Monte Carlo Tree Search (MCTS) algorithm -- run using a model of the target environment -- using action priors defined by the VLA policy. By using VLA-derived abstractions and priors in model-based search, VLAPS efficiently explores language-conditioned robotics tasks whose search spaces would otherwise be intractably large. Conversely, by integrating model-based search with the VLA policy's inference procedure, VLAPS yields behaviours that are more performant than those obtained by directly following the VLA policy's action predictions. VLAPS offers a principled framework to: i) control test-time compute in VLA models, ii) leverage a priori knowledge of the robotic environment, and iii) integrate established planning and reinforcement learning techniques into the VLA inference process. Across all experiments, VLAPS significantly outperforms VLA-only baselines on language-specified tasks that would otherwise be intractable for uninformed search algorithms, increasing success rates by as much as 67 percentage points.
  </details>

- **[Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey](https://arxiv.org/abs/2508.13073)**  `arXiv:2508.13073`  `cs.RO`  
  _Rui Shao, Wei Li, Lingsen Zhang, Renshan Zhang, Zhiyang Liu, Ran Chen, et al._
  <details open><summary>Abstract</summary>
  Robotic manipulation, a key frontier in robotics and embodied AI, requires precise motor control and multimodal understanding, yet traditional rule-based methods fail to scale or generalize in unstructured, novel environments. In recent years, Vision-Language-Action (VLA) models, built upon Large Vision-Language Models (VLMs) pretrained on vast image-text datasets, have emerged as a transformative paradigm. This survey provides the first systematic, taxonomy-oriented review of large VLM-based VLA models for robotic manipulation. We begin by clearly defining large VLM-based VLA models and delineating two principal architectural paradigms: (1) monolithic models, encompassing single-system and dual-system designs with differing levels of integration; and (2) hierarchical models, which explicitly decouple planning from execution via interpretable intermediate representations. Building on this foundation, we present an in-depth examination of large VLM-based VLA models: (1) integration with advanced domains, including reinforcement learning, training-free optimization, learning from human videos, and world model integration; (2) synthesis of distinctive characteristics, consolidating architectural traits, operational strengths, and the datasets and benchmarks that support their development; (3) identification of promising directions, including memory mechanisms, 4D perception, efficient adaptation, multi-agent cooperation, and other emerging capabilities. This survey consolidates recent advances to resolve inconsistencies in existing taxonomies, mitigate research fragmentation, and fill a critical gap through the systematic integration of studies at the intersection of large VLMs and robotic manipulation. We provide a regularly updated project page to document ongoing progress:this https URL.
  </details>

- **[Toward General Physical Intelligence for Resilient Agile Manufacturing Automation](https://arxiv.org/abs/2508.11960)**  `arXiv:2508.11960`  `cs.RO`  
  _Sandeep Kanta, Mehrdad Tavassoli, Varun Teja Chirkuri, Venkata Akhil Kumar, Santhi Bharath Punati, Praveen Damacharla, et al._
  <details open><summary>Abstract</summary>
  Agile and human-centric manufacturing stipulates resilient robotic solutions capable of contextual reasoning and safe interaction in unstructured environments. Foundation models particularly the Vision Language Action (VLA) models have emerged to fuse multimodal perception, reasoning and physically grounded action across varied embodiments into unified representation, termed as General Physical Intelligence (GPI). While GPI has already been described in the literature but its practical application and evolving role in contemporary agile manufacturing processes have yet to be duly explored. To bridge this gap, this practical review systematically surveys recent advancements in VLA models within GPI context, performs comprehensive comparative analysis of leading implementations and evaluates their readiness for industrial deployment through structured ablation study. Our analysis has organized state-of-the-art into five thematic pillars including multisensory representation learning, sim2real transfer, planning and control, uncertainty and safety measures and benchmarking. Finally, we articulate open research challenges and propose directions to better integrate GPI into next-generation industrial ecosystems in line with Industry 5.0.
  </details>
