# 🔍 Embodied_AI Papers · 2025-09-15

[![Total Papers](https://img.shields.io/badge/Papers-1-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations](https://arxiv.org/abs/2509.11417)**  `arXiv:2509.11417`  `cs.RO` `cs.AI` `cs.CV` `cs.LG`  
  _Shresth Grover, Akshay Gopalkrishnan, Bo Ai, Henrik I. Christensen, Hao Su, Xuanlin Li_
  <details open><summary>Abstract</summary>
  Vision-language-action (VLA) models finetuned from vision-language models (VLMs) hold the promise of leveraging rich pretrained representations to build generalist robots across diverse tasks and environments. However, direct fine-tuning on robot data often disrupts these representations and limits generalization. We present a framework that better preserves pretrained features while adapting them for robot manipulation. Our approach introduces three components: (i) a dual-encoder design with one frozen vision encoder to retain pretrained features and another trainable for task adaptation, (ii) a string-based action tokenizer that casts continuous actions into character sequences aligned with the model's pretraining domain, and (iii) a co-training strategy that combines robot demonstrations with vision-language datasets emphasizing spatial reasoning and affordances. Evaluations in simulation and on real robots show that our method improves robustness to visual perturbations, generalization to novel instructions and environments, and overall task success compared to baselines.
  </details>
