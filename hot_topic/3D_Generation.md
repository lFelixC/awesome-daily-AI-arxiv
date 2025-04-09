# 🔍 3D_Generation Papers · 2025-04-08

[![Total Papers](https://img.shields.io/badge/Papers-2-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[EP-Diffuser: An Efficient Diffusion Model for Traffic Scene Generation and Prediction via Polynomial Representations](https://arxiv.org/abs/2504.05422)**  `arXiv:2504.05422`  `cs.CV` `cs.LG` `cs.RO`  
  _Yue Yao, Mohamed-Khalil Bouzidi, Daniel Goehring, Joerg Reichardt_
  <details open><summary>Abstract</summary>
  As the prediction horizon increases, predicting the future evolution of traffic scenes becomes increasingly difficult due to the multi-modal nature of agent motion. Most state-of-the-art (SotA) prediction models primarily focus on forecasting the most likely future. However, for the safe operation of autonomous vehicles, it is equally important to cover the distribution for plausible motion alternatives. To address this, we introduce EP-Diffuser, a novel parameter-efficient diffusion-based generative model designed to capture the distribution of possible traffic scene evolutions. Conditioned on road layout and agent history, our model acts as a predictor and generates diverse, plausible scene continuations. We benchmark EP-Diffuser against two SotA models in terms of accuracy and plausibility of predictions on the Argoverse 2 dataset. Despite its significantly smaller model size, our approach achieves both highly accurate and plausible traffic scene predictions. We further evaluate model generalization ability in an out-of-distribution (OoD) test setting using Waymo Open dataset and show superior robustness of our approach. The code and model checkpoints can be found here:this https URL.
  </details>

- **[CamContextI2V: Context-aware Controllable Video Generation](https://arxiv.org/abs/2504.06022)**  `arXiv:2504.06022`  `cs.CV`  
  _Luis Denninger, Sina Mokhtarzadeh Azar, Juergen Gall_
  <details open><summary>Abstract</summary>
  Recently, image-to-video (I2V) diffusion models have demonstrated impressive scene understanding and generative quality, incorporating image conditions to guide generation. However, these models primarily animate static images without extending beyond their provided context. Introducing additional constraints, such as camera trajectories, can enhance diversity but often degrades visual quality, limiting their applicability for tasks requiring faithful scene representation. We propose CamContextI2V, an I2V model that integrates multiple image conditions with 3D constraints alongside camera control to enrich both global semantics and fine-grained visual details. This enables more coherent and context-aware video generation. Moreover, we motivate the necessity of temporal awareness for an effective context representation. Our comprehensive study on the RealEstate10K dataset demonstrates improvements in visual quality and camera controllability. We make our code and models publicly available at:this https URL.
  </details>
