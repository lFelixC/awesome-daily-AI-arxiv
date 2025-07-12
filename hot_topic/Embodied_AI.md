# 🔍 Embodied_AI Papers · 2025-07-11

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
  Recent large-scale Vision Language Action (VLA) models have shown superior performance in robotic manipulation tasks guided by natural language. However, their generalization remains limited when applied to novel objects or unfamiliar environments that lie outside the training distribution. To address this, many existing approaches integrate additional components such as depth estimation, segmentation, or even diffusion to improve generalization, at the cost of adding significant computation overhead, resulting in low efficiency. This motivates the exploration of efficient action prediction methods, which are independent of additional high-level visual representations or diffusion techniques. In this work, we propose VOTE, an efficient and general framework for the optimization and acceleration of VLA models. In details, we propose a novel tokenizer-free fine-tuning approach for parallel accurate action prediction, which reduces computational overhead and accelerates inference speed. Additionally, we adopt an ensemble voting strategy for the action sampling, which significantly improves model performance and enhances generalization. Experimental results show that our method achieves state-of-the-art performance with 35x faster inference and 145 Hz throughput. All the details and codes will be open-sourced.
  </details>

- **[One Object, Multiple Lies: A Benchmark for Cross-task Adversarial Attack on Unified Vision-Language Models](https://arxiv.org/abs/2507.07709)**  `arXiv:2507.07709`  `cs.CV`  
  _Jiale Zhao, Xinyang Jiang, Junyao Gao, Yuhao Xue, Cairong Zhao_
  <details open><summary>Abstract</summary>
  Unified vision-language models(VLMs) have recently shown remarkable progress, enabling a single model to flexibly address diverse tasks through different instructions within a shared computational architecture. This instruction-based control mechanism creates unique security challenges, as adversarial inputs must remain effective across multiple task instructions that may be unpredictably applied to process the same malicious content. In this paper, we introduce CrossVLAD, a new benchmark dataset carefully curated from MSCOCO with GPT-4-assisted annotations for systematically evaluating cross-task adversarial attacks on unified VLMs. CrossVLAD centers on the object-change objective-consistently manipulating a target object's classification across four downstream tasks-and proposes a novel success rate metric that measures simultaneous misclassification across all tasks, providing a rigorous evaluation of adversarial transferability. To tackle this challenge, we present CRAFT (Cross-task Region-based Attack Framework with Token-alignment), an efficient region-centric attack method. Extensive experiments on Florence-2 and other popular unified VLMs demonstrate that our method outperforms existing approaches in both overall cross-task attack performance and targeted object-change success rates, highlighting its effectiveness in adversarially influencing unified VLMs across diverse tasks.
  </details>
