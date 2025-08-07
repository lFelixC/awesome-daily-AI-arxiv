# 🔍 Embodied_AI Papers · 2025-08-06

[![Total Papers](https://img.shields.io/badge/Papers-2-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[VOTE: Vision-Language-Action Optimization with Trajectory Ensemble Voting](https://arxiv.org/abs/2507.05116)**  `arXiv:2507.05116`  `cs.CV` `cs.AI` `cs.RO`  
  _Juyi Lin, Amir Taherin, Arash Akbari, Arman Akbari, Lei Lu, Guangyu Chen, et al._
  <details open><summary>Abstract</summary>
  Recent large-scale Vision Language Action (VLA) models have shown superior performance in robotic manipulation tasks guided by natural language. However, current VLA models suffer from two drawbacks: (i) generation of massive tokens leading to high inference latency and increased training cost, and (ii) insufficient utilization of generated actions resulting in potential performance loss. To address these issues, we develop a training framework to finetune VLA models for generating significantly fewer action tokens with high parallelism, effectively reducing inference latency and training cost. Furthermore, we introduce an inference optimization technique with a novel voting-based ensemble strategy to combine current and previous action predictions, improving the utilization of generated actions and overall performance. Our results demonstrate that we achieve superior performance compared with state-of-the-art VLA models, achieving significantly higher success rates and 39$\times$ faster inference than OpenVLA with 46 Hz throughput on edge platforms, demonstrating practical deployability. The code is available atthis https URL.
  </details>

- **[Perceiving and Acting in First-Person: A Dataset and Benchmark for Egocentric Human-Object-Human Interactions](https://arxiv.org/abs/2508.04681)**  `arXiv:2508.04681`  `cs.CV`  
  _Liang Xu, Chengqun Yang, Zili Lin, Fei Xu, Yifan Liu, Congsheng Xu, et al._
  <details open><summary>Abstract</summary>
  Learning action models from real-world human-centric interaction datasets is important towards building general-purpose intelligent assistants with efficiency. However, most existing datasets only offer specialist interaction category and ignore that AI assistants perceive and act based on first-person acquisition. We urge that both the generalist interaction knowledge and egocentric modality are indispensable. In this paper, we embed the manual-assisted task into a vision-language-action framework, where the assistant provides services to the instructor following egocentric vision and commands. With our hybrid RGB-MoCap system, pairs of assistants and instructors engage with multiple objects and the scene following GPT-generated scripts. Under this setting, we accomplish InterVLA, the first large-scale human-object-human interaction dataset with 11.4 hours and 1.2M frames of multimodal data, spanning 2 egocentric and 5 exocentric videos, accurate human/object motions and verbal commands. Furthermore, we establish novel benchmarks on egocentric human motion estimation, interaction synthesis, and interaction prediction with comprehensive analysis. We believe that our InterVLA testbed and the benchmarks will foster future works on building AI agents in the physical world.
  </details>
