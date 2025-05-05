# 🔍 3D_Generation Papers · 2025-05-04

[![Total Papers](https://img.shields.io/badge/Papers-1-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[FreePCA: Integrating Consistency Information across Long-short Frames in Training-free Long Video Generation via Principal Component Analysis](https://arxiv.org/abs/2505.01172)**  `arXiv:2505.01172`  `cs.CV`  
  _Jiangtong Tan, Hu Yu, Jie Huang, Jie Xiao, Feng Zhao_
  <details open><summary>Abstract</summary>
  Long video generation involves generating extended videos using models trained on short videos, suffering from distribution shifts due to varying frame counts. It necessitates the use of local information from the original short frames to enhance visual and motion quality, and global information from the entire long frames to ensure appearance consistency. Existing training-free methods struggle to effectively integrate the benefits of both, as appearance and motion in videos are closely coupled, leading to motion inconsistency and visual quality. In this paper, we reveal that global and local information can be precisely decoupled into consistent appearance and motion intensity information by applying Principal Component Analysis (PCA), allowing for refined complementary integration of global consistency and local quality. With this insight, we propose FreePCA, a training-free long video generation paradigm based on PCA that simultaneously achieves high consistency and quality. Concretely, we decouple consistent appearance and motion intensity features by measuring cosine similarity in the principal component space. Critically, we progressively integrate these features to preserve original quality and ensure smooth transitions, while further enhancing consistency by reusing the mean statistics of the initial noise. Experiments demonstrate that FreePCA can be applied to various video diffusion models without requiring training, leading to substantial improvements. Code is available atthis https URL.
  </details>
