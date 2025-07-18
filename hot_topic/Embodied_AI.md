# 🔍 Embodied_AI Papers · 2025-07-17

[![Total Papers](https://img.shields.io/badge/Papers-4-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[LaViPlan : Language-Guided Visual Path Planning with RLVR](https://arxiv.org/abs/2507.12911)**  `arXiv:2507.12911`  `cs.RO` `cs.LG`  
  _Hayeon Oh_
  <details open><summary>Abstract</summary>
  Out-of-distribution (OOD) scenarios in autonomous driving refer to situations that deviate from the training domain, often leading to unexpected and potentially hazardous behavior from planners that lack prior exposure to such cases. Recently, Vision-Language Models (VLMs) have been introduced into autonomous driving research for their promising generalization capabilities in OOD settings. Early studies demonstrated that VLMs could recognize OOD scenarios and generate user-level decisions such as "go straight" or "turn right." However, a new challenge has emerged due to the misalignment between the VLM's high-level decisions or visual reasoning expressed in language, and the low-level predicted trajectories interpreted as actions. In this paper, we propose LaViPlan, a framework that leverages Reinforcement Learning with Verifiable Rewards (RLVR) to optimize VLMs using planning-oriented metrics. This approach addresses the vision-language-action misalignment observed in existing VLMs fine-tuned via supervised learning, which can recognize driving scenarios but often produce context-unaware decisions. Experimental results demonstrate that our method improves situational awareness and decision-making under OOD conditions, highlighting its potential to mitigate the misalignment issue. This work introduces a promising post-training paradigm for VLM agents in the context of autonomous driving.
  </details>

- **[EgoVLA: Learning Vision-Language-Action Models from Egocentric Human Videos](https://arxiv.org/abs/2507.12440)**  `arXiv:2507.12440`  `cs.RO` `cs.AI` `cs.CV` `cs.LG`  
  _Ruihan Yang, Qinxi Yu, Yecheng Wu, Rui Yan, Borui Li, An-Chieh Cheng, et al._
  <details open><summary>Abstract</summary>
  Real robot data collection for imitation learning has led to significant advancements in robotic manipulation. However, the requirement for robot hardware in the process fundamentally constrains the scale of the data. In this paper, we explore training Vision-Language-Action (VLA) models using egocentric human videos. The benefit of using human videos is not only for their scale but more importantly for the richness of scenes and tasks. With a VLA trained on human video that predicts human wrist and hand actions, we can perform Inverse Kinematics and retargeting to convert the human actions to robot actions. We fine-tune the model using a few robot manipulation demonstrations to obtain the robot policy, namely EgoVLA. We propose a simulation benchmark called Ego Humanoid Manipulation Benchmark, where we design diverse bimanual manipulation tasks with demonstrations. We fine-tune and evaluate EgoVLA with Ego Humanoid Manipulation Benchmark and show significant improvements over baselines and ablate the importance of human data. Videos can be found on our website:this https URL
  </details>

- **[DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge](https://arxiv.org/abs/2507.04447)**  `arXiv:2507.04447`  `cs.CV` `cs.RO`  
  _Wenyao Zhang, Hongsi Liu, Zekun Qi, Yunnan Wang, Xinqiang Yu, Jiazhao Zhang, et al._
  <details open><summary>Abstract</summary>
  Recent advances in vision-language-action (VLA) models have shown promise in integrating image generation with action prediction to improve generalization and reasoning in robot manipulation. However, existing methods are limited to challenging image-based forecasting, which suffers from redundant information and lacks comprehensive and critical world knowledge, including dynamic, spatial and semantic information. To address these limitations, we propose DreamVLA, a novel VLA framework that integrates comprehensive world knowledge forecasting to enable inverse dynamics modeling, thereby establishing a perception-prediction-action loop for manipulation tasks. Specifically, DreamVLA introduces a dynamic-region-guided world knowledge prediction, integrated with the spatial and semantic cues, which provide compact yet comprehensive representations for action planning. This design aligns with how humans interact with the world by first forming abstract multimodal reasoning chains before acting. To mitigate interference among the dynamic, spatial and semantic information during training, we adopt a block-wise structured attention mechanism that masks their mutual attention, preventing information leakage and keeping each representation clean and disentangled. Moreover, to model the conditional distribution over future actions, we employ a diffusion-based transformer that disentangles action representations from shared latent features. Extensive experiments on both real-world and simulation environments demonstrate that DreamVLA achieves 76.7% success rate on real robot tasks and 4.44 average length on the CALVIN ABC-D benchmarks.
  </details>

- **[AnyPos: Automated Task-Agnostic Actions for Bimanual Manipulation](https://arxiv.org/abs/2507.12768)**  `arXiv:2507.12768`  `cs.CV` `cs.LG` `cs.RO`  
  _Hengkai Tan, Yao Feng, Xinyi Mao, Shuhe Huang, Guodong Liu, Zhongkai Hao, et al._
  <details open><summary>Abstract</summary>
  Vision-language-action (VLA) models have shown promise on task-conditioned control in complex settings such as bimanual manipulation. However, the heavy reliance on task-specific human demonstrations limits their generalization and incurs high data acquisition costs. In this work, we present a new notion of task-agnostic action paradigm that decouples action execution from task-specific conditioning, enhancing scalability, efficiency, and cost-effectiveness. To address the data collection challenges posed by this paradigm -- such as low coverage density, behavioral redundancy, and safety risks -- we introduce ATARA (Automated Task-Agnostic Random Actions), a scalable self-supervised framework that accelerates collection by over $ 30\times $ compared to human teleoperation. To further enable effective learning from task-agnostic data, which often suffers from distribution mismatch and irrelevant trajectories, we propose AnyPos, an inverse dynamics model equipped with Arm-Decoupled Estimation and a Direction-Aware Decoder (DAD). We additionally integrate a video-conditioned action validation module to verify the feasibility of learned policies across diverse manipulation tasks. Extensive experiments show that the AnyPos-ATARA pipeline yields a 51% improvement in test accuracy and achieves 30-40% higher success rates in downstream tasks such as lifting, pick-and-place, and clicking, using replay-based video validation. Project Page:this https URL
  </details>
