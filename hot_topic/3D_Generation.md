# 🔍 3D_Generation Papers · 2025-08-31

[![Total Papers](https://img.shields.io/badge/Papers-1-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[ERTACache: Error Rectification and Timesteps Adjustment for Efficient Diffusion](https://arxiv.org/abs/2508.21091)**  `arXiv:2508.21091`  `cs.CV`  
  _Xurui Peng, Hong Liu, Chenqian Yan, Rui Ma, Fangmin Chen, Xing Wang, et al._
  <details open><summary>Abstract</summary>
  Diffusion models suffer from substantial computational overhead due to their inherently iterative inference process. While feature caching offers a promising acceleration strategy by reusing intermediate outputs across timesteps, naive reuse often incurs noticeable quality degradation. In this work, we formally analyze the cumulative error introduced by caching and decompose it into two principal components: feature shift error, caused by inaccuracies in cached outputs, and step amplification error, which arises from error propagation under fixed timestep schedules. To address these issues, we propose ERTACache, a principled caching framework that jointly rectifies both error types. Our method employs an offline residual profiling stage to identify reusable steps, dynamically adjusts integration intervals via a trajectory-aware correction coefficient, and analytically approximates cache-induced errors through a closed-form residual linearization model. Together, these components enable accurate and efficient sampling under aggressive cache reuse. Extensive experiments across standard image and video generation benchmarks show that ERTACache achieves up to 2x inference speedup while consistently preserving or even improving visual quality. Notably, on the state-of-the-art Wan2.1 video diffusion model, ERTACache delivers 2x acceleration with minimal VBench degradation, effectively maintaining baseline fidelity while significantly improving efficiency. The code is available atthis https URL.
  </details>
