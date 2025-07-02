# 🔍 Embodied_AI Papers · 2025-07-01

[![Total Papers](https://img.shields.io/badge/Papers-2-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers](https://arxiv.org/abs/2507.01016)**  `arXiv:2507.01016`  `cs.RO` `cs.CV`  
  _Yating Wang, Haoyi Zhu, Mingyu Liu, Jiange Yang, Hao-Shu Fang, Tong He_
  <details open><summary>Abstract</summary>
  In this paper, we introduce an innovative vector quantization based action tokenizer built upon the largest-scale action trajectory dataset to date, leveraging over 100 times more data than previous approaches. This extensive dataset enables our tokenizer to capture rich spatiotemporal dynamics, resulting in a model that not only accelerates inference but also generates smoother and more coherent action outputs. Once trained, the tokenizer can be seamlessly adapted to a wide range of downstream tasks in a zero-shot manner, from short-horizon reactive behaviors to long-horizon planning. A key finding of our work is that the domain gap between synthetic and real action trajectories is marginal, allowing us to effectively utilize a vast amount of synthetic data during training without compromising real-world performance. To validate our approach, we conducted extensive experiments in both simulated environments and on real robotic platforms. The results demonstrate that as the volume of synthetic trajectory data increases, the performance of our tokenizer on downstream tasks improves significantly-most notably, achieving up to a 30% higher success rate on two real-world tasks in long-horizon scenarios. These findings highlight the potential of our action tokenizer as a robust and scalable solution for real-time embodied intelligence systems, paving the way for more efficient and reliable robotic control in diverse applicationthis http URLwebsite:this https URL
  </details>

- **[Evo-0: Vision-Language-Action Model with Implicit Spatial Understanding](https://arxiv.org/abs/2507.00416)**  `arXiv:2507.00416`  `cs.RO` `cs.CV`  
  _Tao Lin, Gen Li, Yilei Zhong, Yanwen Zou, Bo Zhao_
  <details open><summary>Abstract</summary>
  Vision-Language-Action (VLA) models have emerged as a promising framework for enabling generalist robots capable of perceiving, reasoning, and acting in the real world. These models usually build upon pretrained Vision-Language Models (VLMs), which excel at semantic understanding due to large-scale text pretraining. However, VLMs typically lack precise spatial understanding capabilities, as they are primarily tuned on 2D image-text pairs without 3D supervision. To address this limitation, recent approaches have incorporated explicit 3D inputs such as point clouds or depth maps, but this necessitates additional depth sensors or defective estimation. In contrast, our work introduces a plug-and-play module that implicitly injects 3D geometry features into VLA models by leveraging an off-the-shelf visual geometry foundation models. We design five spatially challenging tasks that require precise spatial understanding ability to validate effectiveness of our method. Extensive evaluations show that our method significantly improves the performance of state-of-the-art VLA models across diverse scenarios.
  </details>
