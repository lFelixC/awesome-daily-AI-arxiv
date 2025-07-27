# 🔍 Embodied_AI Papers · 2025-07-26

[![Total Papers](https://img.shields.io/badge/Papers-1-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[DSFormer: A Dual-Scale Cross-Learning Transformer for Visual Place Recognition](https://arxiv.org/abs/2507.18444)**  `arXiv:2507.18444`  `cs.CV` `cs.RO`  
  _Haiyang Jiang, Songhao Piao, Chao Gao, Lei Yu, Liguo Chen_
  <details open><summary>Abstract</summary>
  Visual Place Recognition (VPR) is crucial for robust mobile robot localization, yet it faces significant challenges in maintaining reliable performance under varying environmental conditions and viewpoints. To address this, we propose a novel framework that integrates Dual-Scale-Former (DSFormer), a Transformer-based cross-learning module, with an innovative block clustering strategy. DSFormer enhances feature representation by enabling bidirectional information transfer between dual-scale features extracted from the final two CNN layers, capturing both semantic richness and spatial details through self-attention for long-range dependencies within each scale and shared cross-attention for cross-scale learning. Complementing this, our block clustering strategy repartitions the widely used San Francisco eXtra Large (SF-XL) training dataset from multiple distinct perspectives, optimizing data organization to further bolster robustness against viewpoint variations. Together, these innovations not only yield a robust global embedding adaptable to environmental changes but also reduce the required training data volume by approximately 30\% compared to previous partitioning methods. Comprehensive experiments demonstrate that our approach achieves state-of-the-art performance across most benchmark datasets, surpassing advanced reranking methods like DELG, Patch-NetVLAD, TransVPR, and R2Former as a global retrieval solution using 512-dim global descriptors, while significantly improving computational efficiency.
  </details>
