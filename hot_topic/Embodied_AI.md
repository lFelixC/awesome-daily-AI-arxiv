# 🔍 Embodied_AI Papers · 2025-06-17

[![Total Papers](https://img.shields.io/badge/Papers-5-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[ClutterDexGrasp: A Sim-to-Real System for General Dexterous Grasping in Cluttered Scenes](https://arxiv.org/abs/2506.14317)**  `arXiv:2506.14317`  `cs.RO`  
  _Zeyuan Chen, Qiyang Yan, Yuanpei Chen, Tianhao Wu, Jiyao Zhang, Zihan Ding, et al._
  <details open><summary>Abstract</summary>
  Dexterous grasping in cluttered scenes presents significant challenges due to diverse object geometries, occlusions, and potential collisions. Existing methods primarily focus on single-object grasping or grasp-pose prediction without interaction, which are insufficient for complex, cluttered scenes. Recent vision-language-action models offer a potential solution but require extensive real-world demonstrations, making them costly and difficult to scale. To address these limitations, we revisit the sim-to-real transfer pipeline and develop key techniques that enable zero-shot deployment in reality while maintaining robust generalization. We propose ClutterDexGrasp, a two-stage teacher-student framework for closed-loop target-oriented dexterous grasping in cluttered scenes. The framework features a teacher policy trained in simulation using clutter density curriculum learning, incorporating both a novel geometry and spatially-embedded scene representation and a comprehensive safety curriculum, enabling general, dynamic, and safe grasping behaviors. Through imitation learning, we distill the teacher's knowledge into a student 3D diffusion policy (DP3) that operates on partial point cloud observations. To the best of our knowledge, this represents the first zero-shot sim-to-real closed-loop system for target-oriented dexterous grasping in cluttered scenes, demonstrating robust performance across diverse objects and layouts. More details and videos are available atthis https URL.
  </details>

- **[GRaD-Nav++: Vision-Language Model Enabled Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics](https://arxiv.org/abs/2506.14009)**  `arXiv:2506.14009`  `cs.RO`  
  _Qianzhong Chen, Naixiang Gao, Suning Huang, JunEn Low, Timothy Chen, Jiankai Sun, et al._
  <details open><summary>Abstract</summary>
  Autonomous drones capable of interpreting and executing high-level language instructions in unstructured environments remain a long-standing goal. Yet existing approaches are constrained by their dependence on hand-crafted skills, extensive parameter tuning, or computationally intensive models unsuitable for onboard use. We introduce GRaD-Nav++, a lightweight Vision-Language-Action (VLA) framework that runs fully onboard and follows natural-language commands in real time. Our policy is trained in a photorealistic 3D Gaussian Splatting (3DGS) simulator via Differentiable Reinforcement Learning (DiffRL), enabling efficient learning of low-level control from visual and linguistic inputs. At its core is a Mixture-of-Experts (MoE) action head, which adaptively routes computation to improve generalization while mitigating forgetting. In multi-task generalization experiments, GRaD-Nav++ achieves a success rate of 83% on trained tasks and 75% on unseen tasks in simulation. When deployed on real hardware, it attains 67% success on trained tasks and 50% on unseen ones. In multi-environment adaptation experiments, GRaD-Nav++ achieves an average success rate of 81% across diverse simulated environments and 67% across varied real-world settings. These results establish a new benchmark for fully onboard Vision-Language-Action (VLA) flight and demonstrate that compact, efficient models can enable reliable, language-guided navigation without relying on external infrastructure.
  </details>

- **[An Open-Source Software Toolkit & Benchmark Suite for the Evaluation and Adaptation of Multimodal Action Models](https://arxiv.org/abs/2506.09172)**  `arXiv:2506.09172`  `cs.LG` `cs.CV`  
  _Pranav Guruprasad, Yangyue Wang, Sudipta Chowdhury, Jaewoo Song, Harshvardhan Sikka_
  <details open><summary>Abstract</summary>
  Recent innovations in multimodal action models represent a promising direction for developing general-purpose agentic systems, combining visual understanding, language comprehension, and action generation. We introduce MultiNet - a novel, fully open-source benchmark and surrounding software ecosystem designed to rigorously evaluate and adapt models across vision, language, and action domains. We establish standardized evaluation protocols for assessing vision-language models (VLMs) and vision-language-action models (VLAs), and provide open source software to download relevant data, models, and evaluations. Additionally, we provide a composite dataset with over 1.3 trillion tokens of image captioning, visual question answering, commonsense reasoning, robotic control, digital game-play, simulated locomotion/manipulation, and many more tasks. The MultiNet benchmark, framework, toolkit, and evaluation harness have been used in downstream research on the limitations of VLA generalization.
  </details>

- **[Benchmarking Vision, Language, & Action Models in Procedurally Generated, Open Ended Action Environments](https://arxiv.org/abs/2505.05540)**  `arXiv:2505.05540`  `cs.CV` `cs.LG`  
  _Pranav Guruprasad, Yangyue Wang, Sudipta Chowdhury, Harshvardhan Sikka, Paul Pu Liang_
  <details open><summary>Abstract</summary>
  Vision-language-action (VLA) models represent an important step toward general-purpose robotic systems by integrating visual perception, language understanding, and action execution. However, systematic evaluation of these models, particularly their zero-shot generalization capabilities in procedurally out-of-distribution (OOD) environments, remains limited. In this paper, we introduce MultiNet v0.2, a comprehensive benchmark designed to evaluate and analyze the generalization performance of state-of-the-art VLMs and VLAs - including GPT-4o, GPT-4.1, OpenVLA, Pi0 Base, and Pi0 FAST - on diverse procedural tasks from the Procgen benchmark. Our analysis reveals several critical insights: (1) all evaluated models exhibit significant limitations in zero-shot generalization to OOD tasks, with performance heavily influenced by factors such as action representation and task complexity; (2) VLAs generally outperforms other models due to their robust architectural design; and (3) VLM variants demonstrate substantial improvements when constrained appropriately, highlighting the sensitivity of model performance to precise prompt engineering. We release our benchmark, evaluation framework, and findings to enable the assessment of future VLA models and identify critical areas for improvement in their application to out-of-distribution digital tasks.
  </details>

- **[FormGym: Doing Paperwork with Agents](https://arxiv.org/abs/2506.14079)**  `arXiv:2506.14079`  `cs.AI`  
  _Matthew Toles, Rattandeep Singh, Isaac Song Zhou Yu_
  <details open><summary>Abstract</summary>
  Completing paperwork is a challenging and time-consuming problem. Form filling is especially challenging in the pure-image domain without access to OCR, typeset PDF text, or a DOM. For computer agents, it requires multiple abilities, including multi-modal understanding, information retrieval, and tool-use. We present a novel form-filling benchmark consisting of 432 fields spread across 55 documents and 3 tasks, requiring knowledge of 236 features per user. We find that baseline VLAs achieve less than 1% accuracy in most cases, primarily due to poor localization ability. GUI agents also struggle, scoring between 10.6-68.0% despite high cost and latency. Therefore, we also contribute FieldFinder, a tool to assist LLMs in identifying where to place text on a form. With FieldFinder, all models achieve equal or better performance in all six study conditions, with a maximum increase from 2% to 56%.
  </details>
