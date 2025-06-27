# 🔍 Embodied_AI Papers · 2025-06-26

[![Total Papers](https://img.shields.io/badge/Papers-4-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[WorldVLA: Towards Autoregressive Action World Model](https://arxiv.org/abs/2506.21539)**  `arXiv:2506.21539`  `cs.RO` `cs.AI`  
  _Jun Cen, Chaohui Yu, Hangjie Yuan, Yuming Jiang, Siteng Huang, Jiayan Guo, et al._
  <details open><summary>Abstract</summary>
  We present WorldVLA, an autoregressive action world model that unifies action and image understanding and generation. Our WorldVLA intergrates Vision-Language-Action (VLA) model and world model in one single framework. The world model predicts future images by leveraging both action and image understanding, with the purpose of learning the underlying physics of the environment to improve action generation. Meanwhile, the action model generates the subsequent actions based on image observations, aiding in visual understanding and in turn helps visual generation of the world model. We demonstrate that WorldVLA outperforms standalone action and world models, highlighting the mutual enhancement between the world model and the action model. In addition, we find that the performance of the action model deteriorates when generating sequences of actions in an autoregressive manner. This phenomenon can be attributed to the model's limited generalization capability for action prediction, leading to the propagation of errors from earlier actions to subsequent ones. To address this issue, we propose an attention mask strategy that selectively masks prior actions during the generation of the current action, which shows significant performance improvement in the action chunk generation task.
  </details>

- **[Parallels Between VLA Model Post-Training and Human Motor Learning: Progress, Challenges, and Trends](https://arxiv.org/abs/2506.20966)**  `arXiv:2506.20966`  `cs.RO` `cs.AI`  
  _Tian-Yu Xiang, Ao-Qun Jin, Xiao-Hu Zhou, Mei-Jiang Gui, Xiao-Liang Xie, Shi-Qi Liu, et al._
  <details open><summary>Abstract</summary>
  Vision-language-action (VLA) models extend vision-language models (VLM) by integrating action generation modules for robotic manipulation. Leveraging strengths of VLM in vision perception and instruction understanding, VLA models exhibit promising generalization across diverse manipulation tasks. However, applications demanding high precision and accuracy reveal performance gaps without further adaptation. Evidence from multiple domains highlights the critical role of post-training to align foundational models with downstream applications, spurring extensive research on post-training VLA models. VLA model post-training aims to address the challenge of improving an embodiment's ability to interact with the environment for the given tasks, analogous to the process of humans motor skills acquisition. Accordingly, this paper reviews post-training strategies for VLA models through the lens of human motor learning, focusing on three dimensions: environments, embodiments, and tasks. A structured taxonomy is introduced aligned with human learning mechanisms: (1) enhancing environmental perception, (2) improving embodiment awareness, (3) deepening task comprehension, and (4) multi-component integration. Finally, key challenges and trends in post-training VLA models are identified, establishing a conceptual framework to guide future research. This work delivers both a comprehensive overview of current VLA model post-training methods from a human motor learning perspective and practical insights for VLA model development. (Project website:this https URL)
  </details>

- **[Learning Efficient and Robust Language-conditioned Manipulation using Textual-Visual Relevancy and Equivariant Language Mapping](https://arxiv.org/abs/2406.15677)**  `arXiv:2406.15677`  `cs.RO`  
  _Mingxi Jia, Haojie Huang, Zhewen Zhang, Chenghao Wang, Linfeng Zhao, Dian Wang, et al._
  <details open><summary>Abstract</summary>
  Controlling robots through natural language is pivotal for enhancing human-robot collaboration and synthesizing complex robot behaviors. Recent works that are trained on large robot datasets show impressive generalization abilities. However, such pretrained methods are (1) often fragile to unseen scenarios, and (2) expensive to adapt to new tasks. This paper introduces Grounded Equivariant Manipulation (GEM), a robust yet efficient approach that leverages pretrained vision-language models with equivariant language mapping for language-conditioned manipulation tasks. Our experiments demonstrate GEM's high sample efficiency and generalization ability across diverse tasks in both simulation and the real world. GEM achieves similar or higher performance with orders of magnitude fewer robot data compared with major data-efficient baselines such as CLIPort and VIMA. Finally, our approach demonstrates greater robustness compared to large VLA model, e.g, OpenVLA, at correctly interpreting natural language commands on unseen objects and poses. Code, data, and training details are availablethis https URL
  </details>

- **[UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent](https://arxiv.org/abs/2501.18867)**  `arXiv:2501.18867`  `cs.CV` `cs.AI`  
  _Jianke Zhang, Yanjiang Guo, Yucheng Hu, Xiaoyu Chen, Xiang Zhu, Jianyu Chen_
  <details open><summary>Abstract</summary>
  Recent advancements in Vision-Language-Action (VLA) models have leveraged pre-trained Vision-Language Models (VLMs) to improve the generalization capabilities. VLMs, typically pre-trained on vision-language understanding tasks, provide rich semantic knowledge and reasoning abilities. However, prior research has shown that VLMs often focus on high-level semantic content and neglect low-level features, limiting their ability to capture detailed spatial information and understand physical dynamics. These aspects, which are crucial for embodied control tasks, remain underexplored in existing pre-training paradigms. In this paper, we investigate the training paradigm for VLAs, and introduce \textbf{UP-VLA}, a \textbf{U}nified VLA model training with both multi-modal \textbf{U}nderstanding and future \textbf{P}rediction objectives, enhancing both high-level semantic comprehension and low-level spatial understanding. Experimental results show that UP-VLA achieves a 33% improvement on the Calvin ABC-D benchmark compared to the previous state-of-the-art method. Additionally, UP-VLA demonstrates improved success rates in real-world manipulation tasks, particularly those requiring precise spatial information.
  </details>
