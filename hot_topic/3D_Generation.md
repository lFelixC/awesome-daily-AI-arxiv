# 🔍 3D_Generation Papers · 2025-04-01

[![Total Papers](https://img.shields.io/badge/Papers-4-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[Video-T1: Test-Time Scaling for Video Generation](https://arxiv.org/abs/2503.18942)**  `arXiv:2503.18942`  `cs.CV` `cs.AI`  
  _Fangfu Liu, Hanyang Wang, Yimo Cai, Kaiyan Zhang, Xiaohang Zhan, Yueqi Duan_
  <details open><summary>Abstract</summary>
  With the scale capability of increasing training data, model size, and computational cost, video generation has achieved impressive results in digital creation, enabling users to express creativity across various domains. Recently, researchers in Large Language Models (LLMs) have expanded the scaling to test-time, which can significantly improve LLM performance by using more inference-time computation. Instead of scaling up video foundation models through expensive training costs, we explore the power of Test-Time Scaling (TTS) in video generation, aiming to answer the question: if a video generation model is allowed to use non-trivial amount of inference-time compute, how much can it improve generation quality given a challenging text prompt. In this work, we reinterpret the test-time scaling of video generation as a searching problem to sample better trajectories from Gaussian noise space to the target video distribution. Specifically, we build the search space with test-time verifiers to provide feedback and heuristic algorithms to guide searching process. Given a text prompt, we first explore an intuitive linear search strategy by increasing noise candidates at inference time. As full-step denoising all frames simultaneously requires heavy test-time computation costs, we further design a more efficient TTS method for video generation called Tree-of-Frames (ToF) that adaptively expands and prunes video branches in an autoregressive manner. Extensive experiments on text-conditioned video generation benchmarks demonstrate that increasing test-time compute consistently leads to significant improvements in the quality of videos. Project page:this https URL
  </details>

- **[PhyT2V: LLM-Guided Iterative Self-Refinement for Physics-Grounded Text-to-Video Generation](https://arxiv.org/abs/2412.00596)**  `arXiv:2412.00596`  `cs.CV` `cs.AI`  
  _Qiyao Xue, Xiangyu Yin, Boyuan Yang, Wei Gao_
  <details open><summary>Abstract</summary>
  Text-to-video (T2V) generation has been recently enabled by transformer-based diffusion models, but current T2V models lack capabilities in adhering to the real-world common knowledge and physical rules, due to their limited understanding of physical realism and deficiency in temporal modeling. Existing solutions are either data-driven or require extra model inputs, but cannot be generalizable to out-of-distribution domains. In this paper, we present PhyT2V, a new data-independent T2V technique that expands the current T2V model's capability of video generation to out-of-distribution domains, by enabling chain-of-thought and step-back reasoning in T2V prompting. Our experiments show that PhyT2V improves existing T2V models' adherence to real-world physical rules by 2.3x, and achieves 35% improvement compared to T2V prompt enhancers. The source codes are available at:this https URL.
  </details>

- **[On-device Sora: Enabling Training-Free Diffusion-based Text-to-Video Generation for Mobile Devices](https://arxiv.org/abs/2503.23796)**  `arXiv:2503.23796`  `cs.CV`  
  _Bosung Kim, Kyuhwan Lee, Isu Jeong, Jungmin Cheon, Yeojin Lee, Seulki Lee_
  <details open><summary>Abstract</summary>
  We present On-device Sora, the first model training-free solution for diffusion-based on-device text-to-video generation that operates efficiently on smartphone-grade devices. To address the challenges of diffusion-based text-to-video generation on computation- and memory-limited mobile devices, the proposed On-device Sora applies three novel techniques to pre-trained video generative models. First, Linear Proportional Leap (LPL) reduces the excessive denoising steps required in video diffusion through an efficient leap-based approach. Second, Temporal Dimension Token Merging (TDTM) minimizes intensive token-processing computation in attention layers by merging consecutive tokens along the temporal dimension. Third, Concurrent Inference with Dynamic Loading (CI-DL) dynamically partitions large models into smaller blocks and loads them into memory for concurrent model inference, effectively addressing the challenges of limited device memory. We implement On-device Sora on the iPhone 15 Pro, and the experimental evaluations show that it is capable of generating high-quality videos on the device, comparable to those produced by high-end GPUs. These results show that On-device Sora enables efficient and high-quality video generation on resource-constrained mobile devices. We envision the proposed On-device Sora as a significant first step toward democratizing state-of-the-art generative technologies, enabling video generation on commodity mobile and embedded devices without resource-intensive re-training for model optimization (compression). The code implementation is available at a GitHub repository(this https URL).
  </details>

- **[StarGen: A Spatiotemporal Autoregression Framework with Video Diffusion Model for Scalable and Controllable Scene Generation](https://arxiv.org/abs/2501.05763)**  `arXiv:2501.05763`  `cs.CV`  
  _Shangjin Zhai, Zhichao Ye, Jialin Liu, Weijian Xie, Jiaqi Hu, Zhen Peng, et al._
  <details open><summary>Abstract</summary>
  Recent advances in large reconstruction and generative models have significantly improved scene reconstruction and novel view generation. However, due to compute limitations, each inference with these large models is confined to a small area, making long-range consistent scene generation challenging. To address this, we propose StarGen, a novel framework that employs a pre-trained video diffusion model in an autoregressive manner for long-range scene generation. The generation of each video clip is conditioned on the 3D warping of spatially adjacent images and the temporally overlapping image from previously generated clips, improving spatiotemporal consistency in long-range scene generation with precise pose control. The spatiotemporal condition is compatible with various input conditions, facilitating diverse tasks, including sparse view interpolation, perpetual view generation, and layout-conditioned city generation. Quantitative and qualitative evaluations demonstrate StarGen's superior scalability, fidelity, and pose accuracy compared to state-of-the-art methods. Project page:this https URL.
  </details>
