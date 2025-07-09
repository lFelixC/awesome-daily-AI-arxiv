# 🔍 Embodied_AI Papers · 2025-07-08

[![Total Papers](https://img.shields.io/badge/Papers-2-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[Hume: Introducing System-2 Thinking in Visual-Language-Action Model](https://arxiv.org/abs/2505.21432)**  `arXiv:2505.21432`  `cs.RO` `cs.AI`  
  _Haoming Song, Delin Qu, Yuanqi Yao, Qizhi Chen, Qi Lv, Yiwen Tang, et al._
  <details open><summary>Abstract</summary>
  Humans practice slow thinking before performing actual actions when handling complex tasks in the physical world. This thinking paradigm, recently, has achieved remarkable advancement in boosting Large Language Models (LLMs) to solve complex tasks in digital domains. However, the potential of slow thinking remains largely unexplored for robotic foundation models interacting with the physical world. In this work, we propose Hume: a dual-system Vision-Language-Action (VLA) model with value-guided System-2 thinking and cascaded action denoising, exploring human-like thinking capabilities of Vision-Language-Action models for dexterous robot control. System 2 of Hume implements value-Guided thinking by extending a Vision-Language-Action Model backbone with a novel value-query head to estimate the state-action value of predicted actions. The value-guided thinking is conducted by repeat sampling multiple action candidates and selecting one according to state-action value. System 1 of Hume is a lightweight reactive visuomotor policy that takes System 2 selected action and performs cascaded action denoising for dexterous robot control. At deployment time, System 2 performs value-guided thinking at a low frequency while System 1 asynchronously receives the System 2 selected action candidate and predicts fluid actions in real time. We show that Hume outperforms the existing state-of-the-art Vision-Language-Action models across multiple simulation benchmark and real-robot deployments.
  </details>

- **[MCAM: Multimodal Causal Analysis Model for Ego-Vehicle-Level Driving Video Understanding](https://arxiv.org/abs/2507.06072)**  `arXiv:2507.06072`  `cs.CV`  
  _Tongtong Cheng, Rongzhen Li, Yixin Xiong, Tao Zhang, Jing Wang, Kai Liu_
  <details open><summary>Abstract</summary>
  Accurate driving behavior recognition and reasoning are critical for autonomous driving video understanding. However, existing methods often tend to dig out the shallow causal, fail to address spurious correlations across modalities, and ignore the ego-vehicle level causality modeling. To overcome these limitations, we propose a novel Multimodal Causal Analysis Model (MCAM) that constructs latent causal structures between visual and language modalities. Firstly, we design a multi-level feature extractor to capture long-range dependencies. Secondly, we design a causal analysis module that dynamically models driving scenarios using a directed acyclic graph (DAG) of driving states. Thirdly, we utilize a vision-language transformer to align critical visual features with their corresponding linguistic expressions. Extensive experiments on the BDD-X, and CoVLA datasets demonstrate that MCAM achieves SOTA performance in visual-language causal relationship learning. Furthermore, the model exhibits superior capability in capturing causal characteristics within video sequences, showcasing its effectiveness for autonomous driving applications. The code is available atthis https URL.
  </details>
