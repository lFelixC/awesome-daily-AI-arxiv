# 🔍 3D_Generation Papers · 2025-09-03

[![Total Papers](https://img.shields.io/badge/Papers-1-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[CompSlider: Compositional Slider for Disentangled Multiple-Attribute Image Generation](https://arxiv.org/abs/2509.01028)**  `arXiv:2509.01028`  `cs.CV`  
  _Zixin Zhu, Kevin Duarte, Mamshad Nayeem Rizve, Chengyuan Xu, Ratheesh Kalarot, Junsong Yuan_
  <details open><summary>Abstract</summary>
  In text-to-image (T2I) generation, achieving fine-grained control over attributes - such as age or smile - remains challenging, even with detailed text prompts. Slider-based methods offer a solution for precise control of image attributes. Existing approaches typically train individual adapter for each attribute separately, overlooking the entanglement among multiple attributes. As a result, interference occurs among different attributes, preventing precise control of multiple attributes together. To address this challenge, we aim to disentangle multiple attributes in slider-based generation to enbale more reliable and independent attribute manipulation. Our approach, CompSlider, can generate a conditional prior for the T2I foundation model to control multiple attributes simultaneously. Furthermore, we introduce novel disentanglement and structure losses to compose multiple attribute changes while maintaining structural consistency within the image. Since CompSlider operates in the latent space of the conditional prior and does not require retraining the foundation model, it reduces the computational burden for both training and inference. We evaluate our approach on a variety of image attributes and highlight its generality by extending to video generation.
  </details>
