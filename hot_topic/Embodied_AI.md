# 🔍 Embodied_AI Papers · 2025-09-09

[![Total Papers](https://img.shields.io/badge/Papers-4-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[F1: A Vision-Language-Action Model Bridging Understanding and Generation to Actions](https://arxiv.org/abs/2509.06951)**  `arXiv:2509.06951`  `cs.RO` `cs.CV`  
  _Qi Lv, Weijie Kong, Hao Li, Jia Zeng, Zherui Qiu, Delin Qu, et al._
  <details open><summary>Abstract</summary>
  Executing language-conditioned tasks in dynamic visual environments remains a central challenge in embodied AI. Existing Vision-Language-Action (VLA) models predominantly adopt reactive state-to-action mappings, often leading to short-sighted behaviors and poor robustness in dynamic scenes. In this paper, we introduce F1, a pretrained VLA framework which integrates the visual foresight generation into decision-making pipeline. F1 adopts a Mixture-of-Transformer architecture with dedicated modules for perception, foresight generation, and control, thereby bridging understanding, generation, and actions. At its core, F1 employs a next-scale prediction mechanism to synthesize goal-conditioned visual foresight as explicit planning targets. By forecasting plausible future visual states, F1 reformulates action generation as a foresight-guided inverse dynamics problem, enabling actions that implicitly achieve visual goals. To endow F1 with robust and generalizable capabilities, we propose a three-stage training recipe on an extensive dataset comprising over 330k trajectories across 136 diverse tasks. This training scheme enhances modular reasoning and equips the model with transferable visual foresight, which is critical for complex and dynamic environments. Extensive evaluations on real-world tasks and simulation benchmarks demonstrate F1 consistently outperforms existing approaches, achieving substantial gains in both task success rate and generalization ability.
  </details>

- **[EmbodiedOneVision: Interleaved Vision-Text-Action Pretraining for General Robot Control](https://arxiv.org/abs/2508.21112)**  `arXiv:2508.21112`  `cs.RO` `cs.AI`  
  _Delin Qu, Haoming Song, Qizhi Chen, Zhaoqing Chen, Xianqiang Gao, Xinyi Ye, et al._
  <details open><summary>Abstract</summary>
  The human ability to seamlessly perform multimodal reasoning and physical interaction in the open world is a core goal for general-purpose embodied intelligent systems. Recent vision-language-action (VLA) models, which are co-trained on large-scale robot and visual-text data, have demonstrated notable progress in general robot control. However, they still fail to achieve human-level flexibility in interleaved reasoning and interaction. In this work, introduce EO-Robotics, consists of EO-1 model and EO-Data1.5M dataset. EO-1 is a unified embodied foundation model that achieves superior performance in multimodal embodied reasoning and robot control through interleaved vision-text-action pre-training. The development of EO-1 is based on two key pillars: (i) a unified architecture that processes multimodal inputs indiscriminately (image, text, video, and action), and (ii) a massive, high-quality multimodal embodied reasoning dataset, EO-Data1.5M, which contains over 1.5 million samples with emphasis on interleaved vision-text-action comprehension. EO-1 is trained through synergies between auto-regressive decoding and flow matching denoising on EO-Data1.5M, enabling seamless robot action generation and multimodal embodied reasoning. Extensive experiments demonstrate the effectiveness of interleaved vision-text-action learning for open-world understanding and generalization, validated through a variety of long-horizon, dexterous manipulation tasks across multiple embodiments. This paper details the architecture of EO-1, the data construction strategy of EO-Data1.5M, and the training methodology, offering valuable insights for developing advanced embodied foundation models.
  </details>

- **[TA-VLA: Elucidating the Design Space of Torque-aware Vision-Language-Action Models](https://arxiv.org/abs/2509.07962)**  `arXiv:2509.07962`  `cs.RO`  
  _Zongzheng Zhang, Haobo Xu, Zhuo Yang, Chenghao Yue, Zehao Lin, Huan-ang Gao, et al._
  <details open><summary>Abstract</summary>
  Many robotic manipulation tasks require sensing and responding to force signals such as torque to assess whether the task has been successfully completed and to enable closed-loop control. However, current Vision-Language-Action (VLA) models lack the ability to integrate such subtle physical feedback. In this work, we explore Torque-aware VLA models, aiming to bridge this gap by systematically studying the design space for incorporating torque signals into existing VLA architectures. We identify and evaluate several strategies, leading to three key findings. First, introducing torque adapters into the decoder consistently outperforms inserting them into thethis http URL, inspired by joint prediction and planning paradigms in autonomous driving, we propose predicting torque as an auxiliary output, which further improves performance. This strategy encourages the model to build a physically grounded internal representation of interaction dynamics. Extensive quantitative and qualitative experiments across contact-rich manipulation benchmarks validate our findings.
  </details>

- **[Graph-Fused Vision-Language-Action for Policy Reasoning in Multi-Arm Robotic Manipulation](https://arxiv.org/abs/2509.07957)**  `arXiv:2509.07957`  `cs.RO`  
  _Shunlei Li, Longsen Gao, Jiuwen Cao, Yingbai Hu_
  <details open><summary>Abstract</summary>
  Acquiring dexterous robotic skills from human video demonstrations remains a significant challenge, largely due to conventional reliance on low-level trajectory replication, which often fails to generalize across varying objects, spatial layouts, and manipulator configurations. To address this limitation, we introduce Graph-Fused Vision-Language-Action (GF-VLA), a unified framework that enables dual-arm robotic systems to perform task-level reasoning and execution directly from RGB-D human demonstrations. GF-VLA employs an information-theoretic approach to extract task-relevant cues, selectively highlighting critical hand-object and object-object interactions. These cues are structured into temporally ordered scene graphs, which are subsequently integrated with a language-conditioned transformer to produce hierarchical behavior trees and interpretable Cartesian motion primitives. To enhance efficiency in bimanual execution, we propose a cross-arm allocation strategy that autonomously determines gripper assignment without requiring explicit geometric modeling. We validate GF-VLA on four dual-arm block assembly benchmarks involving symbolic structure construction and spatial generalization. Empirical results demonstrate that the proposed representation achieves over 95% graph accuracy and 93% subtask segmentation, enabling the language-action planner to generate robust, interpretable task policies. When deployed on a dual-arm robot, these policies attain 94% grasp reliability, 89% placement accuracy, and 90% overall task success across stacking, letter-formation, and geometric reconfiguration tasks, evidencing strong generalization and robustness under diverse spatial and semantic variations.
  </details>
