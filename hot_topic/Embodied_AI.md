# 🔍 Embodied_AI Papers · 2025-09-10

[![Total Papers](https://img.shields.io/badge/Papers-2-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[LLaDA-VLA: Vision Language Diffusion Action Models](https://arxiv.org/abs/2509.06932)**  `arXiv:2509.06932`  `cs.RO` `cs.CV`  
  _Yuqing Wen, Hebei Li, Kefan Gu, Yucheng Zhao, Tiancai Wang, Xiaoyan Sun_
  <details open><summary>Abstract</summary>
  The rapid progress of auto-regressive vision-language models (VLMs) has inspired growing interest in vision-language-action models (VLA) for robotic manipulation. Recently, masked diffusion models, a paradigm distinct from autoregressive models, have begun to demonstrate competitive performance in text generation and multimodal applications, leading to the development of a series of diffusion-based VLMs (d-VLMs). However, leveraging such models for robot policy learning remains largely unexplored. In this work, we present LLaDA-VLA, the first Vision-Language-Diffusion-Action model built upon pretrained d-VLMs for robotic manipulation. To effectively adapt d-VLMs to robotic domain, we introduce two key designs: (1) a localized special-token classification strategy that replaces full-vocabulary classification with special action token classification, reducing adaptation difficulty; (2) a hierarchical action-structured decoding strategy that decodes action sequences hierarchically considering the dependencies within and across actions. Extensive experiments demonstrate that LLaDA-VLA significantly outperforms state-of-the-art VLAs on both simulation and real-world robots.
  </details>

- **[RoboChemist: Long-Horizon and Safety-Compliant Robotic Chemical Experimentation](https://arxiv.org/abs/2509.08820)**  `arXiv:2509.08820`  `cs.RO`  
  _Zongzheng Zhang, Chenghao Yue, Haobo Xu, Minwen Liao, Xianglin Qi, Huan-ang Gao, et al._
  <details open><summary>Abstract</summary>
  Robotic chemists promise to both liberate human experts from repetitive tasks and accelerate scientific discovery, yet remain in their infancy. Chemical experiments involve long-horizon procedures over hazardous and deformable substances, where success requires not only task completion but also strict compliance with experimental norms. To address these challenges, we propose \textit{RoboChemist}, a dual-loop framework that integrates Vision-Language Models (VLMs) with Vision-Language-Action (VLA) models. Unlike prior VLM-based systems (e.g., VoxPoser, ReKep) that rely on depth perception and struggle with transparent labware, and existing VLA systems (e.g., RDT, pi0) that lack semantic-level feedback for complex tasks, our method leverages a VLM to serve as (1) a planner to decompose tasks into primitive actions, (2) a visual prompt generator to guide VLA models, and (3) a monitor to assess task success and regulatory compliance. Notably, we introduce a VLA interface that accepts image-based visual targets from the VLM, enabling precise, goal-conditioned control. Our system successfully executes both primitive actions and complete multi-step chemistry protocols. Results show 23.57% higher average success rate and a 0.298 average increase in compliance rate over state-of-the-art VLA baselines, while also demonstrating strong generalization to objects and tasks.
  </details>
