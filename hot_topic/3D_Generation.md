# 🔍 3D_Generation Papers · 2025-09-14

[![Total Papers](https://img.shields.io/badge/Papers-2-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[Compute Only 16 Tokens in One Timestep: Accelerating Diffusion Transformers with Cluster-Driven Feature Caching](https://arxiv.org/abs/2509.10312)**  `arXiv:2509.10312`  `cs.CV`  
  _Zhixin Zheng, Xinyu Wang, Chang Zou, Shaobo Wang, Linfeng Zhang_
  <details open><summary>Abstract</summary>
  Diffusion transformers have gained significant attention in recent years for their ability to generate high-quality images and videos, yet still suffer from a huge computational cost due to their iterative denoising process. Recently, feature caching has been introduced to accelerate diffusion transformers by caching the feature computation in previous timesteps and reusing it in the following timesteps, which leverage the temporal similarity of diffusion models while ignoring the similarity in the spatial dimension. In this paper, we introduce Cluster-Driven Feature Caching (ClusCa) as an orthogonal and complementary perspective for previous feature caching. Specifically, ClusCa performs spatial clustering on tokens in each timestep, computes only one token in each cluster and propagates their information to all the other tokens, which is able to reduce the number of tokens by over 90%. Extensive experiments on DiT, FLUX and HunyuanVideo demonstrate its effectiveness in both text-to-image and text-to-video generation. Besides, it can be directly applied to any diffusion transformer without requirements for training. For instance, ClusCa achieves 4.96x acceleration on FLUX with an ImageReward of 99.49%, surpassing the original model by 0.51%. The code is available atthis https URL.
  </details>

- **[A Markovian Framing of WaveFunctionCollapse for Procedurally Generating Aesthetically Complex Environments](https://arxiv.org/abs/2509.09919)**  `arXiv:2509.09919`  `cs.AI`  
  _Franklin Yiu, Mohan Lu, Nina Li, Kevin Joseph, Tianxu Zhang, Julian Togelius, et al._
  <details open><summary>Abstract</summary>
  Procedural content generation often requires satisfying both designer-specified objectives and adjacency constraints implicitly imposed by the underlying tile set. To address the challenges of jointly optimizing both constraints and objectives, we reformulate WaveFunctionCollapse (WFC) as a Markov Decision Process (MDP), enabling external optimization algorithms to focus exclusively on objective maximization while leveraging WFC's propagation mechanism to enforce constraint satisfaction. We empirically compare optimizing this MDP to traditional evolutionary approaches that jointly optimize global metrics and local tile placement. Across multiple domains with various difficulties, we find that joint optimization not only struggles as task complexity increases, but consistently underperforms relative to optimization over the WFC-MDP, underscoring the advantages of decoupling local constraint satisfaction from global objective optimization.
  </details>
