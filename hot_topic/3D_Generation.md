# 🔍 3D_Generation Papers · 2025-09-12

[![Total Papers](https://img.shields.io/badge/Papers-4-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[Improving Video Diffusion Transformer Training by Multi-Feature Fusion and Alignment from Self-Supervised Vision Encoders](https://arxiv.org/abs/2509.09547)**  `arXiv:2509.09547`  `cs.CV` `cs.AI`  
  _Dohun Lee, Hyeonho Jeong, Jiwook Kim, Duygu Ceylan, Jong Chul Ye_
  <details open><summary>Abstract</summary>
  Video diffusion models have advanced rapidly in the recent years as a result of series of architectural innovations (e.g., diffusion transformers) and use of novel training objectives (e.g., flow matching). In contrast, less attention has been paid to improving the feature representation power of such models. In this work, we show that training video diffusion models can benefit from aligning the intermediate features of the video generator with feature representations of pre-trained vision encoders. We propose a new metric and conduct an in-depth analysis of various vision encoders to evaluate their discriminability and temporal consistency, thereby assessing their suitability for video feature alignment. Based on the analysis, we present Align4Gen which provides a novel multi-feature fusion and alignment method integrated into video diffusion model training. We evaluate Align4Gen both for unconditional and class-conditional video generation tasks and show that it results in improved video generation as quantified by various metrics. Full video results are available on our project page:this https URL
  </details>

- **[Kling-Avatar: Grounding Multimodal Instructions for Cascaded Long-Duration Avatar Animation Synthesis](https://arxiv.org/abs/2509.09595)**  `arXiv:2509.09595`  `cs.CV`  
  _Yikang Ding, Jiwen Liu, Wenyuan Zhang, Zekun Wang, Wentao Hu, Liyuan Cui, et al._
  <details open><summary>Abstract</summary>
  Recent advances in audio-driven avatar video generation have significantly enhanced audio-visual realism. However, existing methods treat instruction conditioning merely as low-level tracking driven by acoustic or visual cues, without modeling the communicative purpose conveyed by the instructions. This limitation compromises their narrative coherence and character expressiveness. To bridge this gap, we introduce Kling-Avatar, a novel cascaded framework that unifies multimodal instruction understanding with photorealistic portrait generation. Our approach adopts a two-stage pipeline. In the first stage, we design a multimodal large language model (MLLM) director that produces a blueprint video conditioned on diverse instruction signals, thereby governing high-level semantics such as character motion and emotions. In the second stage, guided by blueprint keyframes, we generate multiple sub-clips in parallel using a first-last frame strategy. This global-to-local framework preserves fine-grained details while faithfully encoding the high-level intent behind multimodal instructions. Our parallel architecture also enables fast and stable generation of long-duration videos, making it suitable for real-world applications such as digital human livestreaming and vlogging. To comprehensively evaluate our method, we construct a benchmark of 375 curated samples covering diverse instructions and challenging scenarios. Extensive experiments demonstrate that Kling-Avatar is capable of generating vivid, fluent, long-duration videos at up to 1080p and 48 fps, achieving superior performance in lip synchronization accuracy, emotion and dynamic expressiveness, instruction controllability, identity preservation, and cross-domain generalization. These results establish Kling-Avatar as a new benchmark for semantically grounded, high-fidelity audio-driven avatar synthesis.
  </details>

- **[Zero-shot 3D-Aware Trajectory-Guided image-to-video generation via Test-Time Training](https://arxiv.org/abs/2509.06723)**  `arXiv:2509.06723`  `cs.CV`  
  _Ruicheng Zhang, Jun Zhou, Zunnan Xu, Zihao Liu, Jiehui Huang, Mingyang Zhang, et al._
  <details open><summary>Abstract</summary>
  Trajectory-Guided image-to-video (I2V) generation aims to synthesize videos that adhere to user-specified motion instructions. Existing methods typically rely on computationally expensive fine-tuning on scarce annotated datasets. Although some zero-shot methods attempt to trajectory control in the latent space, they may yield unrealistic motion by neglecting 3D perspective and creating a misalignment between the manipulated latents and the network's noise predictions. To address these challenges, we introduce Zo3T, a novel zero-shot test-time-training framework for trajectory-guided generation with three core innovations: First, we incorporate a 3D-Aware Kinematic Projection, leveraging inferring scene depth to derive perspective-correct affine transformations for target regions. Second, we introduce Trajectory-Guided Test-Time LoRA, a mechanism that dynamically injects and optimizes ephemeral LoRA adapters into the denoising network alongside the latent state. Driven by a regional feature consistency loss, this co-adaptation effectively enforces motion constraints while allowing the pre-trained model to locally adapt its internal representations to the manipulated latent, thereby ensuring generative fidelity and on-manifold adherence. Finally, we develop Guidance Field Rectification, which refines the denoising evolutionary path by optimizing the conditional guidance field through a one-step lookahead strategy, ensuring efficient generative progression towards the target trajectory. Zo3T significantly enhances 3D realism and motion accuracy in trajectory-controlled I2V generation, demonstrating superior performance over existing training-based and zero-shot approaches.
  </details>

- **[S$^2$-Guidance: Stochastic Self Guidance for Training-Free Enhancement of Diffusion Models](https://arxiv.org/abs/2508.12880)**  `arXiv:2508.12880`  `cs.CV`  
  _Chubin Chen, Jiashu Zhu, Xiaokun Feng, Nisha Huang, Meiqi Wu, Fangyuan Mao, et al._
  <details open><summary>Abstract</summary>
  Classifier-free Guidance (CFG) is a widely used technique in modern diffusion models for enhancing sample quality and prompt adherence. However, through an empirical analysis on Gaussian mixture modeling with a closed-form solution, we observe a discrepancy between the suboptimal results produced by CFG and the ground truth. The model's excessive reliance on these suboptimal predictions often leads to semantic incoherence and low-quality outputs. To address this issue, we first empirically demonstrate that the model's suboptimal predictions can be effectively refined using sub-networks of the model itself. Building on this insight, we propose S^2-Guidance, a novel method that leverages stochastic block-dropping during the forward process to construct stochastic sub-networks, effectively guiding the model away from potential low-quality predictions and toward high-quality outputs. Extensive qualitative and quantitative experiments on text-to-image and text-to-video generation tasks demonstrate that S^2-Guidance delivers superior performance, consistently surpassing CFG and other advanced guidance strategies. Our code will be released.
  </details>
