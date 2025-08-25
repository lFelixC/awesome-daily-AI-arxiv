# 🔍 3D_Generation Papers · 2025-08-24

[![Total Papers](https://img.shields.io/badge/Papers-6-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[Spatial Policy: Guiding Visuomotor Robotic Manipulation with Spatial-Aware Modeling and Reasoning](https://arxiv.org/abs/2508.15874)**  `arXiv:2508.15874`  `cs.RO` `cs.AI`  
  _Yijun Liu, Yuwei Liu, Yuan Meng, Jieheng Zhang, Yuwei Zhou, Ye Li, et al._
  <details open><summary>Abstract</summary>
  Vision-centric hierarchical embodied models have demonstrated strong potential for long-horizon robotic control. However, existing methods lack spatial awareness capabilities, limiting their effectiveness in bridging visual plans to actionable control in complex environments. To address this problem, we propose Spatial Policy (SP), a unified spatial-aware visuomotor robotic manipulation framework via explicit spatial modeling and reasoning. Specifically, we first design a spatial-conditioned embodied video generation module to model spatially guided predictions through a spatial plan table. Then, we propose a spatial-based action prediction module to infer executable actions with coordination. Finally, we propose a spatial reasoning feedback policy to refine the spatial plan table via dual-stage replanning. Extensive experiments show that SP significantly outperforms state-of-the-art baselines, achieving a 33.0% average improvement over the best baseline. With an 86.7% average success rate across 11 diverse tasks, SP substantially enhances the practicality of embodied models for robotic control applications. Code and checkpoints are maintained atthis https URL.
  </details>

- **[OmniCache: A Trajectory-Oriented Global Perspective on Training-Free Cache Reuse for Diffusion Transformer Models](https://arxiv.org/abs/2508.16212)**  `arXiv:2508.16212`  `cs.CV` `cs.AI` `cs.LG`  
  _Huanpeng Chu, Wei Wu, Guanyu Fen, Yutao Zhang_
  <details open><summary>Abstract</summary>
  Diffusion models have emerged as a powerful paradigm for generative tasks such as image synthesis and video generation, with Transformer architectures further enhancing performance. However, the high computational cost of diffusion Transformers-stemming from a large number of sampling steps and complex per-step computations-presents significant challenges for real-time deployment. In this paper, we introduce OmniCache, a training-free acceleration method that exploits the global redundancy inherent in the denoising process. Unlike existing methods that determine caching strategies based on inter-step similarities and tend to prioritize reusing later sampling steps, our approach originates from the sampling perspective of DIT models. We systematically analyze the model's sampling trajectories and strategically distribute cache reuse across the entire sampling process. This global perspective enables more effective utilization of cached computations throughout the diffusion trajectory, rather than concentrating reuse within limited segments of the samplingthis http URLaddition, during cache reuse, we dynamically estimate the corresponding noise and filter it out to reduce its impact on the samplingthis http URLexperiments demonstrate that our approach accelerates the sampling process while maintaining competitive generative quality, offering a promising and practical solution for efficient deployment of diffusion-based generative models.
  </details>

- **[Seeing Clearly, Forgetting Deeply: Revisiting Fine-Tuned Video Generators for Driving Simulation](https://arxiv.org/abs/2508.16512)**  `arXiv:2508.16512`  `cs.CV`  
  _Chun-Peng Chang, Chen-Yu Wang, Julian Schmidt, Holger Caesar, Alain Pagani_
  <details open><summary>Abstract</summary>
  Recent advancements in video generation have substantially improved visual quality and temporal coherence, making these models increasingly appealing for applications such as autonomous driving, particularly in the context of driving simulation and so-called "world models". In this work, we investigate the effects of existing fine-tuning video generation approaches on structured driving datasets and uncover a potential trade-off: although visual fidelity improves, spatial accuracy in modeling dynamic elements may degrade. We attribute this degradation to a shift in the alignment between visual quality and dynamic understanding objectives. In datasets with diverse scene structures within temporal space, where objects or perspective shift in varied ways, these objectives tend to highly correlated. However, the very regular and repetitive nature of driving scenes allows visual quality to improve by modeling dominant scene motion patterns, without necessarily preserving fine-grained dynamic behavior. As a result, fine-tuning encourages the model to prioritize surface-level realism over dynamic accuracy. To further examine this phenomenon, we show that simple continual learning strategies, such as replay from diverse domains, can offer a balanced alternative by preserving spatial accuracy while maintaining strong visual quality.
  </details>

- **[Forecast then Calibrate: Feature Caching as ODE for Efficient Diffusion Transformers](https://arxiv.org/abs/2508.16211)**  `arXiv:2508.16211`  `cs.CV`  
  _Shikang Zheng, Liang Feng, Xinyu Wang, Qinming Zhou, Peiliang Cai, Chang Zou, et al._
  <details open><summary>Abstract</summary>
  Diffusion Transformers (DiTs) have demonstrated exceptional performance in high-fidelity image and video generation. To reduce their substantial computational costs, feature caching techniques have been proposed to accelerate inference by reusing hidden representations from previous timesteps. However, current methods often struggle to maintain generation quality at high acceleration ratios, where prediction errors increase sharply due to the inherent instability of long-step forecasting. In this work, we adopt an ordinary differential equation (ODE) perspective on the hidden-feature sequence, modeling layer representations along the trajectory as a feature-ODE. We attribute the degradation of existing caching strategies to their inability to robustly integrate historical features under large skipping intervals. To address this, we propose FoCa (Forecast-then-Calibrate), which treats feature caching as a feature-ODE solving problem. Extensive experiments on image synthesis, video generation, and super-resolution tasks demonstrate the effectiveness of FoCa, especially under aggressive acceleration. Without additional training, FoCa achieves near-lossless speedups of 5.50 times on FLUX, 6.45 times on HunyuanVideo, 3.17 times on Inf-DiT, and maintains high quality with a 4.53 times speedup on DiT.
  </details>

- **[OccScene: Semantic Occupancy-based Cross-task Mutual Learning for 3D Scene Generation](https://arxiv.org/abs/2412.11183)**  `arXiv:2412.11183`  `cs.CV`  
  _Bohan Li, Xin Jin, Jianan Wang, Yukai Shi, Yasheng Sun, Xiaofeng Wang, et al._
  <details open><summary>Abstract</summary>
  Recent diffusion models have demonstrated remarkable performance in both 3D scene generation and perception tasks. Nevertheless, existing methods typically separate these two processes, acting as a data augmenter to generate synthetic data for downstream perception tasks. In this work, we propose OccScene, a novel mutual learning paradigm that integrates fine-grained 3D perception and high-quality generation in a unified framework, achieving a cross-task win-win effect. OccScene generates new and consistent 3D realistic scenes only depending on text prompts, guided with semantic occupancy in a joint-training diffusion framework. To align the occupancy with the diffusion latent, a Mamba-based Dual Alignment module is introduced to incorporate fine-grained semantics and geometry as perception priors. Within OccScene, the perception module can be effectively improved with customized and diverse generated scenes, while the perception priors in return enhance the generation performance for mutual benefits. Extensive experiments show that OccScene achieves realistic 3D scene generation in broad indoor and outdoor scenarios, while concurrently boosting the perception models to achieve substantial performance improvements in the 3D perception task of semantic occupancy prediction.
  </details>

- **[Soteria: Language-Specific Functional Parameter Steering for Multilingual Safety Alignment](https://arxiv.org/abs/2502.11244)**  `arXiv:2502.11244`  `cs.CL` `cs.AI`  
  _Somnath Banerjee, Sayan Layek, Pratyush Chatterjee, Animesh Mukherjee, Rima Hazra_
  <details open><summary>Abstract</summary>
  Ensuring consistent safety across multiple languages remains a significant challenge for large language models (LLMs). We introduce Soteria, a lightweight yet powerful strategy that locates and minimally adjusts the "functional heads" most responsible for harmful content generation in each language. By altering only a fraction of parameters, Soteria drastically reduces policy violations without sacrificing overall model performance, even in low-resource settings. To rigorously evaluate our approach, we also present XThreatBench, a specialized multilingual dataset capturing fine-grained harmful behaviors drawn from real policy guidelines. Experiments with leading open-source LLMs (e.g., Llama, Qwen, Mistral) show that Soteria consistently improves safety metrics across high-, mid-, and low-resource languages. These findings highlight a promising path toward scalable, linguistically attuned, and ethically aligned LLMs worldwide.
  </details>
