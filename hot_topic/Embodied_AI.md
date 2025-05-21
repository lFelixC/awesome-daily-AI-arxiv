# 🔍 Embodied_AI Papers · 2025-05-20

[![Total Papers](https://img.shields.io/badge/Papers-4-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[RoboFAC: A Comprehensive Framework for Robotic Failure Analysis and Correction](https://arxiv.org/abs/2505.12224)**  `arXiv:2505.12224`  `cs.RO` `cs.AI`  
  _Weifeng Lu, Minghao Ye, Zewei Ye, Ruihan Tao, Shuo Yang, Bo Zhao_
  <details open><summary>Abstract</summary>
  Vision-Language-Action (VLA) models have recently advanced robotic manipulation by translating natural-language instructions and image information into sequential control actions. However, these models often underperform in open-world scenarios, as they are predominantly trained on successful expert demonstrations and exhibit a limited capacity for failure recovery. In this work, we present a Robotic Failure Analysis and Correction (RoboFAC) framework to address this issue. Firstly, we construct RoboFAC dataset comprising 9,440 erroneous manipulation trajectories and 78,623 QA pairs across 16 diverse tasks and 53 scenes in both simulation and real-world environments. Leveraging our dataset, we develop RoboFAC model, which is capable of Task Understanding, Failure Analysis and Failure Correction. Experimental results demonstrate that the RoboFAC model outperforms GPT-4o by 34.1% on our evaluation benchmark. Furthermore, we integrate the RoboFAC model into a real-world VLA control pipeline as an external supervision providing correction instructions, yielding a 29.1% relative improvement on average on four real-world tasks. The results show that our RoboFAC framework effectively handles robotic failures and assists the VLA model in recovering from failures.
  </details>

- **[AutoBio: A Simulation and Benchmark for Robotic Automation in Digital Biology Laboratory](https://arxiv.org/abs/2505.14030)**  `arXiv:2505.14030`  `cs.RO`  
  _Zhiqian Lan, Yuxuan Jiang, Ruiqi Wang, Xuanbing Xie, Rongkui Zhang, Yicheng Zhu, et al._
  <details open><summary>Abstract</summary>
  Vision-language-action (VLA) models have shown promise as generalist robotic policies by jointly leveraging visual, linguistic, and proprioceptive modalities to generate action trajectories. While recent benchmarks have advanced VLA research in domestic tasks, professional science-oriented domains remain underexplored. We introduce AutoBio, a simulation framework and benchmark designed to evaluate robotic automation in biology laboratory environments--an application domain that combines structured protocols with demanding precision and multimodal interaction. AutoBio extends existing simulation capabilities through a pipeline for digitizing real-world laboratory instruments, specialized physics plugins for mechanisms ubiquitous in laboratory workflows, and a rendering stack that support dynamic instrument interfaces and transparent materials through physically based rendering. Our benchmark comprises biologically grounded tasks spanning three difficulty levels, enabling standardized evaluation of language-guided robotic manipulation in experimental protocols. We provide infrastructure for demonstration generation and seamless integration with VLA models. Baseline evaluations with two SOTA VLA models reveal significant gaps in precision manipulation, visual reasoning, and instruction following in scientific workflows. By releasing AutoBio, we aim to catalyze research on generalist robotic systems for complex, high-precision, and multimodal professional environments. The simulator and benchmark are publicly available to facilitate reproducible research.
  </details>

- **[InSpire: Vision-Language-Action Models with Intrinsic Spatial Reasoning](https://arxiv.org/abs/2505.13888)**  `arXiv:2505.13888`  `cs.RO`  
  _Ji Zhang, Shihan Wu, Xu Luo, Hao Wu, Lianli Gao, Heng Tao Shen, et al._
  <details open><summary>Abstract</summary>
  Leveraging pretrained Vision-Language Models (VLMs) to map language instruction and visual observations to raw low-level actions, Vision-Language-Action models (VLAs) hold great promise for achieving general-purpose robotic systems. Despite their advancements, existing VLAs tend to spuriously correlate task-irrelevant visual features with actions, limiting their generalization capacity beyond the training data. To tackle this challenge, we propose Intrinsic Spatial Reasoning (InSpire), a simple yet effective approach that mitigates the adverse effects of spurious correlations by boosting the spatial reasoning ability of VLAs. Specifically, InSpire redirects the VLA's attention to task-relevant factors by prepending the question "In which direction is the [object] relative to the robot?" to the language instruction and aligning the answer "right/left/up/down/front/back/grasped" and predicted actions with the ground-truth. Notably, InSpire can be used as a plugin to enhance existing autoregressive VLAs, requiring no extra training data or interaction with other large models. Extensive experimental results in both simulation and real-world environments demonstrate the effectiveness and flexibility of our approach. Our code, pretrained models and demos are publicly available at:this https URL.
  </details>

- **[ReVLA: Reverting Visual Domain Limitation of Robotic Foundation Models](https://arxiv.org/abs/2409.15250)**  `arXiv:2409.15250`  `cs.CV` `cs.RO`  
  _Sombit Dey, Jan-Nico Zaech, Nikolay Nikolov, Luc Van Gool, Danda Pani Paudel_
  <details open><summary>Abstract</summary>
  Recent progress in large language models and access to large-scale robotic datasets has sparked a paradigm shift in robotics models transforming them into generalists able to adapt to various tasks, scenes, and robot modalities. A large step for the community are open Vision Language Action models which showcase strong performance in a wide variety of tasks. In this work, we study the visual generalization capabilities of three existing robotic foundation models, and propose a corresponding evaluation framework. Our study shows that the existing models do not exhibit robustness to visual out-of-domain scenarios. This is potentially caused by limited variations in the training data and/or catastrophic forgetting, leading to domain limitations in the vision foundation models. We further explore OpenVLA, which uses two pre-trained vision foundation models and is, therefore, expected to generalize to out-of-domain experiments. However, we showcase catastrophic forgetting by DINO-v2 in OpenVLA through its failure to fulfill the task of depth regression. To overcome the aforementioned issue of visual catastrophic forgetting, we propose a gradual backbone reversal approach founded on model merging. This enables OpenVLA -- which requires the adaptation of the visual backbones during initial training -- to regain its visual generalization ability. Regaining this capability enables our ReVLA model to improve over OpenVLA by a factor of 77\% and 66\% for grasping and lifting in visual OOD tasks. Comprehensive evaluations, episode rollouts and model weights are available on the ReVLA Page
  </details>
