# 🔍 Embodied_AI Papers · 2025-07-22

[![Total Papers](https://img.shields.io/badge/Papers-2-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[GR-3 Technical Report](https://arxiv.org/abs/2507.15493)**  `arXiv:2507.15493`  `cs.RO` `cs.AI` `cs.CV`  
  _Chilam Cheang, Sijin Chen, Zhongren Cui, Yingdong Hu, Liqun Huang, Tao Kong, et al._
  <details open><summary>Abstract</summary>
  We report our recent progress towards building generalist robot policies, the development of GR-3. GR-3 is a large-scale vision-language-action (VLA) model. It showcases exceptional capabilities in generalizing to novel objects, environments, and instructions involving abstract concepts. Furthermore, it can be efficiently fine-tuned with minimal human trajectory data, enabling rapid and cost-effective adaptation to new settings. GR-3 also excels in handling long-horizon and dexterous tasks, including those requiring bi-manual manipulation and mobile movement, showcasing robust and reliable performance. These capabilities are achieved through a multi-faceted training recipe that includes co-training with web-scale vision-language data, efficient fine-tuning from human trajectory data collected via VR devices, and effective imitation learning with robot trajectory data. In addition, we introduce ByteMini, a versatile bi-manual mobile robot designed with exceptional flexibility and reliability, capable of accomplishing a wide range of tasks when integrated with GR-3. Through extensive real-world experiments, we show GR-3 surpasses the state-of-the-art baseline method, $\pi_0$, on a wide variety of challenging tasks. We hope GR-3 can serve as a step towards building generalist robots capable of assisting humans in daily life.
  </details>

- **[ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning](https://arxiv.org/abs/2507.16815)**  `arXiv:2507.16815`  `cs.CV` `cs.AI` `cs.LG` `cs.RO`  
  _Chi-Pin Huang, Yueh-Hua Wu, Min-Hung Chen, Yu-Chiang Frank Wang, Fu-En Yang_
  <details open><summary>Abstract</summary>
  Vision-language-action (VLA) reasoning tasks require agents to interpret multimodal instructions, perform long-horizon planning, and act adaptively in dynamic environments. Existing approaches typically train VLA models in an end-to-end fashion, directly mapping inputs to actions without explicit reasoning, which hinders their ability to plan over multiple steps or adapt to complex task variations. In this paper, we propose ThinkAct, a dual-system framework that bridges high-level reasoning with low-level action execution via reinforced visual latent planning. ThinkAct trains a multimodal LLM to generate embodied reasoning plans guided by reinforcing action-aligned visual rewards based on goal completion and trajectory consistency. These reasoning plans are compressed into a visual plan latent that conditions a downstream action model for robust action execution on target environments. Extensive experiments on embodied reasoning and robot manipulation benchmarks demonstrate that ThinkAct enables few-shot adaptation, long-horizon planning, and self-correction behaviors in complex embodied AI tasks.
  </details>
