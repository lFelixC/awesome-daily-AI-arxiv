# 🔍 Embodied_AI Papers · 2025-06-08

[![Total Papers](https://img.shields.io/badge/Papers-3-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies](https://arxiv.org/abs/2412.10345)**  `arXiv:2412.10345`  `cs.RO` `cs.AI`  
  _Ruijie Zheng, Yongyuan Liang, Shuaiyi Huang, Jianfeng Gao, Hal Daumé III, Andrey Kolobov, et al._
  <details open><summary>Abstract</summary>
  Although large vision-language-action (VLA) models pretrained on extensive robot datasets offer promising generalist policies for robotic learning, they still struggle with spatial-temporal dynamics in interactive robotics, making them less effective in handling complex tasks, such as manipulation. In this work, we introduce visual trace prompting, a simple yet effective approach to facilitate VLA models' spatial-temporal awareness for action prediction by encoding state-action trajectories visually. We develop a new TraceVLA model by finetuning OpenVLA on our own collected dataset of 150K robot manipulation trajectories using visual trace prompting. Evaluations of TraceVLA across 137 configurations in SimplerEnv and 4 tasks on a physical WidowX robot demonstrate state-of-the-art performance, outperforming OpenVLA by 10% on SimplerEnv and 3.5x on real-robot tasks and exhibiting robust generalization across diverse embodiments and scenarios. To further validate the effectiveness and generality of our method, we present a compact VLA model based on 4B Phi-3-Vision, pretrained on the Open-X-Embodiment and finetuned on our dataset, rivals the 7B OpenVLA baseline while significantly improving inference efficiency.
  </details>

- **[RoboOS: A Hierarchical Embodied Framework for Cross-Embodiment and Multi-Agent Collaboration](https://arxiv.org/abs/2505.03673)**  `arXiv:2505.03673`  `cs.RO`  
  _Huajie Tan, Xiaoshuai Hao, Cheng Chi, Minglan Lin, Yaoxu Lyu, Mingyu Cao, et al._
  <details open><summary>Abstract</summary>
  The dawn of embodied intelligence has ushered in an unprecedented imperative for resilient, cognition-enabled multi-agent collaboration across next-generation ecosystems, revolutionizing paradigms in autonomous manufacturing, adaptive service robotics, and cyber-physical production architectures. However, current robotic systems face significant limitations, such as limited cross-embodiment adaptability, inefficient task scheduling, and insufficient dynamic error correction. While End-to-end VLA models demonstrate inadequate long-horizon planning and task generalization, hierarchical VLA models suffer from a lack of cross-embodiment and multi-agent coordination capabilities. To address these challenges, we introduce RoboOS, the first open-source embodied system built on a Brain-Cerebellum hierarchical architecture, enabling a paradigm shift from single-agent to multi-agent intelligence. Specifically, RoboOS consists of three key components: (1) Embodied Brain Model (RoboBrain), a MLLM designed for global perception and high-level decision-making; (2) Cerebellum Skill Library, a modular, plug-and-play toolkit that facilitates seamless execution of multiple skills; and (3) Real-Time Shared Memory, a spatiotemporal synchronization mechanism for coordinating multi-agent states. By integrating hierarchical information flow, RoboOS bridges Embodied Brain and Cerebellum Skill Library, facilitating robust planning, scheduling, and error correction for long-horizon tasks, while ensuring efficient multi-agent collaboration through Real-Time Shared Memory. Furthermore, we enhance edge-cloud communication and cloud-based distributed inference to facilitate high-frequency interactions and enable scalable deployment. Extensive real-world experiments across various scenarios, demonstrate RoboOS's versatility in supporting heterogeneous embodiments. Project website:this https URL
  </details>

- **[DriveAction: A Benchmark for Exploring Human-like Driving Decisions in VLA Models](https://arxiv.org/abs/2506.05667)**  `arXiv:2506.05667`  `cs.CV` `cs.AI`  
  _Yuhan Hao, Zhengning Li, Lei Sun, Weilong Wang, Naixin Yi, Sheng Song, et al._
  <details open><summary>Abstract</summary>
  Vision-Language-Action (VLA) models have advanced autonomous driving, but existing benchmarks still lack scenario diversity, reliable action-level annotation, and evaluation protocols aligned with human preferences. To address these limitations, we introduce DriveAction, the first action-driven benchmark specifically designed for VLA models, comprising 16,185 QA pairs generated from 2,610 driving scenarios. DriveAction leverages real-world driving data proactively collected by users of production-level autonomous vehicles to ensure broad and representative scenario coverage, offers high-level discrete action labels collected directly from users' actual driving operations, and implements an action-rooted tree-structured evaluation framework that explicitly links vision, language, and action tasks, supporting both comprehensive and task-specific assessment. Our experiments demonstrate that state-of-the-art vision-language models (VLMs) require both vision and language guidance for accurate action prediction: on average, accuracy drops by 3.3% without vision input, by 4.1% without language input, and by 8.0% without either. Our evaluation supports precise identification of model bottlenecks with robust and consistent results, thus providing new insights and a rigorous foundation for advancing human-like decisions in autonomous driving.
  </details>
