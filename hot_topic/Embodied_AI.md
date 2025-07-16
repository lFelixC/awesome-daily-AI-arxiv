# 🔍 Embodied_AI Papers · 2025-07-15

[![Total Papers](https://img.shields.io/badge/Papers-2-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models](https://arxiv.org/abs/2502.19417)**  `arXiv:2502.19417`  `cs.RO` `cs.AI` `cs.LG`  
  _Lucy Xiaoyang Shi, Brian Ichter, Michael Equi, Liyiming Ke, Karl Pertsch, Quan Vuong, et al._
  <details open><summary>Abstract</summary>
  Generalist robots that can perform a range of different tasks in open-world settings must be able to not only reason about the steps needed to accomplish their goals, but also process complex instructions, prompts, and even feedback during task execution. Intricate instructions (e.g., "Could you make me a vegetarian sandwich?" or "I don't like that one") require not just the ability to physically perform the individual steps, but the ability to situate complex commands and feedback in the physical world. In this work, we describe a system that uses vision-language models in a hierarchical structure, first reasoning over complex prompts and user feedback to deduce the most appropriate next step to fulfill the task, and then performing that step with low-level actions. In contrast to direct instruction following methods that can fulfill simple commands ("pick up the cup"), our system can reason through complex prompts and incorporate situated feedback during task execution ("that's not trash"). We evaluate our system across three robotic platforms, including single-arm, dual-arm, and dual-arm mobile robots, demonstrating its ability to handle tasks such as cleaning messy tables, making sandwiches, and grocery shopping. Videos are available atthis https URL
  </details>

- **[Vision Language Action Models in Robotic Manipulation: A Systematic Review](https://arxiv.org/abs/2507.10672)**  `arXiv:2507.10672`  `cs.RO`  
  _Muhayy Ud Din, Waseem Akram, Lyes Saad Saoud, Jan Rosell, Irfan Hussain_
  <details open><summary>Abstract</summary>
  Vision Language Action (VLA) models represent a transformative shift in robotics, with the aim of unifying visual perception, natural language understanding, and embodied control within a single learning framework. This review presents a comprehensive and forward-looking synthesis of the VLA paradigm, with a particular emphasis on robotic manipulation and instruction-driven autonomy. We comprehensively analyze 102 VLA models, 26 foundational datasets, and 12 simulation platforms that collectively shape the development and evaluation of VLAs models. These models are categorized into key architectural paradigms, each reflecting distinct strategies for integrating vision, language, and control in robotic systems. Foundational datasets are evaluated using a novel criterion based on task complexity, variety of modalities, and dataset scale, allowing a comparative analysis of their suitability for generalist policy learning. We introduce a two-dimensional characterization framework that organizes these datasets based on semantic richness and multimodal alignment, showing underexplored regions in the current data landscape. Simulation environments are evaluated for their effectiveness in generating large-scale data, as well as their ability to facilitate transfer from simulation to real-world settings and the variety of supported tasks. Using both academic and industrial contributions, we recognize ongoing challenges and outline strategic directions such as scalable pretraining protocols, modular architectural design, and robust multimodal alignment strategies. This review serves as both a technical reference and a conceptual roadmap for advancing embodiment and robotic control, providing insights that span from dataset generation to real world deployment of generalist robotic agents.
  </details>
