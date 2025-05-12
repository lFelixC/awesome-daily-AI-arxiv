# 🔍 Embodied_AI Papers · 2025-05-11

[![Total Papers](https://img.shields.io/badge/Papers-4-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[3D CAVLA: Leveraging Depth and 3D Context to Generalize Vision Language Action Models for Unseen Tasks](https://arxiv.org/abs/2505.05800)**  `arXiv:2505.05800`  `cs.RO` `cs.CV`  
  _Vineet Bhat, Yu-Hsiang Lan, Prashanth Krishnamurthy, Ramesh Karri, Farshad Khorrami_
  <details open><summary>Abstract</summary>
  Robotic manipulation in 3D requires learning an $N$ degree-of-freedom joint space trajectory of a robot manipulator. Robots must possess semantic and visual perception abilities to transform real-world mappings of their workspace into the low-level control necessary for object manipulation. Recent work has demonstrated the capabilities of fine-tuning large Vision-Language Models (VLMs) to learn the mapping between RGB images, language instructions, and joint space control. These models typically take as input RGB images of the workspace and language instructions, and are trained on large datasets of teleoperated robot demonstrations. In this work, we explore methods to improve the scene context awareness of a popular recent Vision-Language-Action model by integrating chain-of-thought reasoning, depth perception, and task-oriented region of interest detection. Our experiments in the LIBERO simulation environment show that our proposed model, 3D-CAVLA, improves the success rate across various LIBERO task suites, achieving an average success rate of 98.1$\%$. We also evaluate the zero-shot capabilities of our method, demonstrating that 3D scene awareness leads to robust learning and adaptation for completely unseen tasks. 3D-CAVLA achieves an absolute improvement of 8.8$\%$ on unseen tasks. We will open-source our code and the unseen tasks dataset to promote community-driven research here:this https URL
  </details>

- **[UniVLA: Learning to Act Anywhere with Task-centric Latent Actions](https://arxiv.org/abs/2505.06111)**  `arXiv:2505.06111`  `cs.RO` `cs.AI` `cs.LG`  
  _Qingwen Bu, Yanting Yang, Jisong Cai, Shenyuan Gao, Guanghui Ren, Maoqing Yao, et al._
  <details open><summary>Abstract</summary>
  A generalist robot should perform effectively across various environments. However, most existing approaches heavily rely on scaling action-annotated data to enhance their capabilities. Consequently, they are often limited to single physical specification and struggle to learn transferable knowledge across different embodiments and environments. To confront these limitations, we propose UniVLA, a new framework for learning cross-embodiment vision-language-action (VLA) policies. Our key innovation is to derive task-centric action representations from videos with a latent action model. This enables us to exploit extensive data across a wide spectrum of embodiments and perspectives. To mitigate the effect of task-irrelevant dynamics, we incorporate language instructions and establish a latent action model within the DINO feature space. Learned from internet-scale videos, the generalist policy can be deployed to various robots through efficient latent action decoding. We obtain state-of-the-art results across multiple manipulation and navigation benchmarks, as well as real-robot deployments. UniVLA achieves superior performance over OpenVLA with less than 1/20 of pretraining compute and 1/10 of downstream data. Continuous performance improvements are observed as heterogeneous data, even including human videos, are incorporated into the training pipeline. The results underscore UniVLA's potential to facilitate scalable and efficient robot policy learning.
  </details>

- **[Benchmarking Vision, Language, & Action Models in Procedurally Generated, Open Ended Action Environments](https://arxiv.org/abs/2505.05540)**  `arXiv:2505.05540`  `cs.CV` `cs.LG`  
  _Pranav Guruprasad, Yangyue Wang, Sudipta Chowdhury, Harshvardhan Sikka_
  <details open><summary>Abstract</summary>
  Vision-language-action (VLA) models represent an important step toward general-purpose robotic systems by integrating visual perception, language understanding, and action execution. However, systematic evaluation of these models, particularly their zero-shot generalization capabilities in out-of-distribution (OOD) environments, remains limited. In this paper, we introduce MultiNet v0.2, a comprehensive benchmark designed to evaluate and analyze the generalization performance of state-of-the-art VLM and VLA models-including GPT-4o, GPT-4.1, OpenVLA,Pi0 Base, and Pi0 FAST-on diverse procedural tasks from the Procgen benchmark. Our analysis reveals several critical insights: (1) all evaluated models exhibit significant limitations in zero-shot generalization to OOD tasks, with performance heavily influenced by factors such as action representation and task complexit; (2) VLAs generally outperform other models due to their robust architectural design; and (3) VLM variants demonstrate substantial improvements when constrained appropriately, highlighting the sensitivity of model performance to precise prompt engineering.
  </details>

- **[VladVA: Discriminative Fine-tuning of LVLMs](https://arxiv.org/abs/2412.04378)**  `arXiv:2412.04378`  `cs.CV` `cs.AI`  
  _Yassine Ouali, Adrian Bulat, Alexandros Xenos, Anestis Zaganidis, Ioannis Maniadis Metaxas, Brais Martinez, et al._
  <details open><summary>Abstract</summary>
  Contrastively-trained Vision-Language Models (VLMs) like CLIP have become the de facto approach for discriminative vision-language representation learning. However, these models have limited language understanding, often exhibiting a "bag of words" behavior. At the same time, Large Vision-Language Models (LVLMs), which combine vision encoders with LLMs, have been shown to be capable of detailed vision-language reasoning, yet their autoregressive nature renders them less suitable for discriminative tasks.In this work, we propose to combine "the best of both worlds": a new training approach for discriminative fine-tuning of LVLMs that results in strong discriminative and compositional capabilities. Essentially, our approach converts a generative LVLM into a discriminative one, unlocking its capability for powerful image-text discrimination combined with enhanced language understanding.Our contributions include (1) a carefully designed training/optimization framework that utilizes image-text pairs of variable length and granularity for training the model with both contrastive and next-token prediction losses. This is accompanied by ablation studies that justify the necessity of our framework's components; (2) a parameter-efficient adaptation method using a combination of soft prompting and LoRA adapters; (3) significant improvements over state-of-the-art CLIP-like models of similar size, including standard image-text retrieval benchmarks and notable gains in compositionality.
  </details>
