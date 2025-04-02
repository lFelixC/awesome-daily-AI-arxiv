# 🔍 Benchmark Papers · 2025-03-31

[![Total Papers](https://img.shields.io/badge/Papers-3-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Benchmark`  
**Filter**: `None`

---

## 📚 Paper List

- **[UniOcc: A Unified Benchmark for Occupancy Forecasting and Prediction in Autonomous Driving](http://arxiv.org/abs/2503.24381v1)**  `arXiv:2503.24381`  `cs.MA` `cs.RO` `cs.LG` `cs.CV` `cs.AI`  
  _Yuping Wang, Xiangyu Huang, Xiaokang Sun, Mingxuan Yan, Shuo Xing, Zhengzhong Tu, et al._
  <details open><summary>Abstract</summary>
  We introduce UniOcc, a comprehensive, unified benchmark for occupancyforecasting (i.e., predicting future occupancies based on historicalinformation) and current-frame occupancy prediction from camera images. UniOccunifies data from multiple real-world datasets (i.e., nuScenes, Waymo) andhigh-fidelity driving simulators (i.e., CARLA, OpenCOOD), which provides 2D/3Doccupancy labels with per-voxel flow annotations and support for cooperativeautonomous driving. In terms of evaluation, unlike existing studies that relyon suboptimal pseudo labels for evaluation, UniOcc incorporates novel metricsthat do not depend on ground-truth occupancy, enabling robust assessment ofadditional aspects of occupancy quality. Through extensive experiments onstate-of-the-art models, we demonstrate that large-scale, diverse training dataand explicit flow information significantly enhance occupancy prediction andforecasting performance.
  </details>

- **[Exploring the Effect of Reinforcement Learning on Video Understanding: Insights from SEED-Bench-R1](http://arxiv.org/abs/2503.24376v1)**  `arXiv:2503.24376`  `cs.CL` `cs.CV` `cs.AI` `cs.LG`  
  _Yi Chen, Yuying Ge, Rui Wang, Yixiao Ge, Lu Qiu, Ying Shan, et al._
  <details open><summary>Abstract</summary>
  Recent advancements in Chain of Thought (COT) generation have significantlyimproved the reasoning capabilities of Large Language Models (LLMs), withreinforcement learning (RL) emerging as an effective post-training approach.Multimodal Large Language Models (MLLMs) inherit this reasoning potential butremain underexplored in tasks requiring both perception and logical reasoning.To address this, we introduce SEED-Bench-R1, a benchmark designed tosystematically evaluate post-training methods for MLLMs in video understanding.It includes intricate real-world videos and complex everyday planning tasks inthe format of multiple-choice questions, requiring sophisticated perception andreasoning. SEED-Bench-R1 assesses generalization through a three-levelhierarchy: in-distribution, cross-environment, and cross-environment-taskscenarios, equipped with a large-scale training dataset with easily verifiableground-truth answers. Using Qwen2-VL-Instruct-7B as a base model, we compare RLwith supervised fine-tuning (SFT), demonstrating RL's data efficiency andsuperior performance on both in-distribution and out-of-distribution tasks,even outperforming SFT on general video understanding benchmarks likeLongVideoBench. Our detailed analysis reveals that RL enhances visualperception but often produces less logically coherent reasoning chains. Weidentify key limitations such as inconsistent reasoning and overlooked visualcues, and suggest future improvements in base model reasoning, reward modeling,and RL robustness against noisy signals.
  </details>

- **[ERUPT: Efficient Rendering with Unposed Patch Transformer](http://arxiv.org/abs/2503.24374v1)**  `arXiv:2503.24374`  `cs.CV`  
  _Maxim V. Shugaev, Vincent Chen, Maxim Karrenbach, Kyle Ashley, Bridget Kennedy, Naresh P. Cuntoor_
  <details open><summary>Abstract</summary>
  This work addresses the problem of novel view synthesis in diverse scenesfrom small collections of RGB images. We propose ERUPT (Efficient Renderingwith Unposed Patch Transformer) a state-of-the-art scene reconstruction modelcapable of efficient scene rendering using unposed imagery. We introducepatch-based querying, in contrast to existing pixel-based queries, to reducethe compute required to render a target view. This makes our model highlyefficient both during training and at inference, capable of rendering at 600fps on commercial hardware. Notably, our model is designed to use a learnedlatent camera pose which allows for training using unposed targets in datasetswith sparse or inaccurate ground truth camera pose. We show that our approachcan generalize on large real-world data and introduce a new benchmark dataset(MSVS-1M) for latent view synthesis using street-view imagery collected fromMapillary. In contrast to NeRF and Gaussian Splatting, which require denseimagery and precise metadata, ERUPT can render novel views of arbitrary sceneswith as few as five unposed input images. ERUPT achieves better rendered imagequality than current state-of-the-art methods for unposed image synthesistasks, reduces labeled data requirements by ~95\% and decreases computationalrequirements by an order of magnitude, providing efficient novel view synthesisfor diverse real-world scenes.
  </details>
