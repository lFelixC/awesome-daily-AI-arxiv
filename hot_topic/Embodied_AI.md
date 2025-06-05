# 🔍 Embodied_AI Papers · 2025-06-04

[![Total Papers](https://img.shields.io/badge/Papers-3-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning](https://arxiv.org/abs/2412.03293)**  `arXiv:2412.03293`  `cs.RO` `cs.CV`  
  _Junjie Wen, Minjie Zhu, Yichen Zhu, Zhibin Tang, Jinming Li, Zhongyi Zhou, et al._
  <details open><summary>Abstract</summary>
  In this paper, we present DiffusionVLA, a novel framework that seamlessly combines the autoregression model with the diffusion model for learning visuomotor policy. Central to our approach is a next-token prediction objective, enabling the model to reason effectively over the user's query in the context of current observations. Subsequently, a diffusion model is attached to generate robust action outputs. To enhance policy learning through self-reasoning, we introduce a novel reasoning injection module that integrates reasoning phrases directly into the policy learning process. The whole framework is simple and flexible, making it easy to deploy and upgrade. We conduct extensive experiments using multiple real robots to validate the effectiveness of DiffusionVLA. Our tests include a challenging factory sorting task, where DiffusionVLA successfully categorizes objects, including those not seen during training. We observe that the reasoning module makes the model interpretable. It allows observers to understand the model thought process and identify potential causes of policy failures. Additionally, we test DiffusionVLA on a zero-shot bin-picking task, achieving 63.7\% accuracy on 102 previously unseen objects. Our method demonstrates robustness to visual changes, such as distractors and new backgrounds, and easily adapts to new embodiments. Furthermore, DiffusionVLA can follow novel instructions and retain conversational ability. Notably, DiffusionVLA is data-efficient and fast at inference; our smallest DiffusionVLA-2B runs 82Hz on a single A6000 GPU and can train from scratch on less than 50 demonstrations for a complex task. Finally, we scale the model from 2B to 72B parameters, showcasing improved generalization capabilities with increased model size.
  </details>

- **[Adversarial Attacks on Robotic Vision Language Action Models](https://arxiv.org/abs/2506.03350)**  `arXiv:2506.03350`  `cs.RO` `cs.AI`  
  _Eliot Krzysztof Jones, Alexander Robey, Andy Zou, Zachary Ravichandran, George J. Pappas, Hamed Hassani, et al._
  <details open><summary>Abstract</summary>
  The emergence of vision-language-action models (VLAs) for end-to-end control is reshaping the field of robotics by enabling the fusion of multimodal sensory inputs at the billion-parameter scale. The capabilities of VLAs stem primarily from their architectures, which are often based on frontier large language models (LLMs). However, LLMs are known to be susceptible to adversarial misuse, and given the significant physical risks inherent to robotics, questions remain regarding the extent to which VLAs inherit these vulnerabilities. Motivated by these concerns, in this work we initiate the study of adversarial attacks on VLA-controlled robots. Our main algorithmic contribution is the adaptation and application of LLM jailbreaking attacks to obtain complete control authority over VLAs. We find that textual attacks, which are applied once at the beginning of a rollout, facilitate full reachability of the action space of commonly used VLAs and often persist over longer horizons. This differs significantly from LLM jailbreaking literature, as attacks in the real world do not have to be semantically linked to notions of harm. We make all code available atthis https URL.
  </details>

- **[SwitchVLA: Execution-Aware Task Switching for Vision-Language-Action Models](https://arxiv.org/abs/2506.03574)**  `arXiv:2506.03574`  `cs.RO`  
  _Meng Li, Zhen Zhao, Zhengping Che, Fei Liao, Kun Wu, Zhiyuan Xu, et al._
  <details open><summary>Abstract</summary>
  Robots deployed in dynamic environments must be able to not only follow diverse language instructions but flexibly adapt when user intent changes mid-execution. While recent Vision-Language-Action (VLA) models have advanced multi-task learning and instruction following, they typically assume static task intent, failing to respond when new instructions arrive during ongoing execution. This limitation hinders natural and robust interaction in dynamic settings, such as retail or household environments, where real-time intent changes are common. We propose SwitchVLA, a unified, execution-aware framework that enables smooth and reactive task switching without external planners or additional switch-specific data. We model task switching as a behavior modulation problem conditioned on execution state and instruction context. Expert demonstrations are segmented into temporally grounded contact phases, allowing the policy to infer task progress and adjust its behavior accordingly. A multi-behavior conditional policy is then trained to generate flexible action chunks under varying behavior modes through conditioned trajectory modeling. Experiments in both simulation and real-world robotic manipulation demonstrate that SwitchVLA enables robust instruction adherence, fluid task switching, and strong generalization-outperforming prior VLA baselines in both task success rate and interaction naturalness.
  </details>
