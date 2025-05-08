# 🔍 Embodied_AI Papers · 2025-05-07

[![Total Papers](https://img.shields.io/badge/Papers-2-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[OpenHelix: A Short Survey, Empirical Analysis, and Open-Source Dual-System VLA Model for Robotic Manipulation](https://arxiv.org/abs/2505.03912)**  `arXiv:2505.03912`  `cs.RO` `cs.CV`  
  _Can Cui, Pengxiang Ding, Wenxuan Song, Shuanghao Bai, Xinyang Tong, Zirui Ge, et al._
  <details open><summary>Abstract</summary>
  Dual-system VLA (Vision-Language-Action) architectures have become a hot topic in embodied intelligence research, but there is a lack of sufficient open-source work for further performance analysis and optimization. To address this problem, this paper will summarize and compare the structural designs of existing dual-system architectures, and conduct systematic empirical evaluations on the core design elements of existing dual-system architectures. Ultimately, it will provide a low-cost open-source model for further exploration. Of course, this project will continue to update with more experimental conclusions and open-source models with improved performance for everyone to choose from. Project page:this https URL.
  </details>

- **[Hamiltonian Normalizing Flows as kinetic PDE solvers: application to the 1D Vlasov-Poisson Equations](https://arxiv.org/abs/2505.04471)**  `arXiv:2505.04471`  `cs.LG`  
  _Vincent Souveton, Sébastien Terrana_
  <details open><summary>Abstract</summary>
  Many conservative physical systems can be described using the Hamiltonian formalism. A notable example is the Vlasov-Poisson equations, a set of partial differential equations that govern the time evolution of a phase-space density function representing collisionless particles under a self-consistent potential. These equations play a central role in both plasma physics and cosmology. Due to the complexity of the potential involved, analytical solutions are rarely available, necessitating the use of numerical methods such as Particle-In-Cell. In this work, we introduce a novel approach based on Hamiltonian-informed Normalizing Flows, specifically a variant of Fixed-Kinetic Neural Hamiltonian Flows. Our method transforms an initial Gaussian distribution in phase space into the final distribution using a sequence of invertible, volume-preserving transformations derived from Hamiltonian dynamics. The model is trained on a dataset comprising initial and final states at a fixed time T, generated via numerical simulations. After training, the model enables fast sampling of the final distribution from any given initial state. Moreover, by automatically learning an interpretable physical potential, it can generalize to intermediate states not seen during training, offering insights into the system's evolution across time.
  </details>
