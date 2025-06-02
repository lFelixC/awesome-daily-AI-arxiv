# 🔍 Embodied_AI Papers · 2025-06-01

[![Total Papers](https://img.shields.io/badge/Papers-3-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[ChatVLA-2: Vision-Language-Action Model with Open-World Embodied Reasoning from Pretrained Knowledge](https://arxiv.org/abs/2505.21906)**  `arXiv:2505.21906`  `cs.RO` `cs.AI` `cs.CV`  
  _Zhongyi Zhou, Yichen Zhu, Junjie Wen, Chaomin Shen, Yi Xu_
  <details open><summary>Abstract</summary>
  Vision-language-action (VLA) models have emerged as the next generation of models in robotics. However, despite leveraging powerful pre-trained Vision-Language Models (VLMs), existing end-to-end VLA systems often lose key capabilities during fine-tuning as the model adapts to specific robotic tasks. We argue that a generalizable VLA model should retain and expand upon the VLM's core competencies: 1) Open-world embodied reasoning - the VLA should inherit the knowledge from VLM, i.e., recognize anything that the VLM can recognize, be capable of solving math problems, and possess visual-spatial intelligence, 2) Reasoning following - effectively translating the open-world reasoning into actionable steps for the robot. In this work, we introduce ChatVLA-2, a novel mixture-of-expert VLA model coupled with a specialized two-stage training pipeline designed to preserve the VLM's original strengths while enabling actionable reasoning. To validate our approach, we design a math-matching task wherein a robot interprets math problems written on a whiteboard and picks corresponding number cards from a table to solve equations. Remarkably, our method exhibits exceptional mathematical reasoning and OCR capabilities, despite these abilities not being explicitly trained within the VLA. Furthermore, we demonstrate that the VLA possesses strong spatial reasoning skills, enabling it to interpret novel directional instructions involving previously unseen objects. Overall, our method showcases reasoning and comprehension abilities that significantly surpass state-of-the-art imitation learning methods such as OpenVLA, DexVLA, and pi-zero. This work represents a substantial advancement toward developing truly generalizable robotic foundation models endowed with robust reasoning capacities.
  </details>

- **[Saliency-Aware Quantized Imitation Learning for Efficient Robotic Control](https://arxiv.org/abs/2505.15304)**  `arXiv:2505.15304`  `cs.RO`  
  _Seongmin Park, Hyungmin Kim, Sangwoo Kim, Wonseok Jeon, Juyoung Yang, Byeongwook Jeon, et al._
  <details open><summary>Abstract</summary>
  Deep neural network (DNN)-based policy models, such as vision-language-action (VLA) models, excel at automating complex decision-making from multi-modal inputs. However, scaling these models greatly increases computational overhead, complicating deployment in resource-constrained settings like robot manipulation and autonomous driving. To address this, we propose Saliency-Aware Quantized Imitation Learning (SQIL), which combines quantization-aware training with a selective loss-weighting strategy for mission-critical states. By identifying these states via saliency scores and emphasizing them in the training loss, SQIL preserves decision fidelity under low-bit precision. We validate SQIL's generalization capability across extensive simulation benchmarks with environment variations, real-world tasks, and cross-domain tasks (self-driving, physics simulation), consistently recovering full-precision performance. Notably, a 4-bit weight-quantized VLA model for robotic manipulation achieves up to 2.5x speedup and 2.5x energy savings on an edge GPU with minimal accuracy loss. These results underline SQIL's potential for efficiently deploying large IL-based policy models on resource-limited devices.
  </details>

- **[Towards a Generalizable Bimanual Foundation Policy via Flow-based Video Prediction](https://arxiv.org/abs/2505.24156)**  `arXiv:2505.24156`  `cs.CV` `cs.RO`  
  _Chenyou Fan, Fangzheng Yan, Chenjia Bai, Jiepeng Wang, Chi Zhang, Zhen Wang, et al._
  <details open><summary>Abstract</summary>
  Learning a generalizable bimanual manipulation policy is extremely challenging for embodied agents due to the large action space and the need for coordinated arm movements. Existing approaches rely on Vision-Language-Action (VLA) models to acquire bimanual policies. However, transferring knowledge from single-arm datasets or pre-trained VLA models often fails to generalize effectively, primarily due to the scarcity of bimanual data and the fundamental differences between single-arm and bimanual manipulation. In this paper, we propose a novel bimanual foundation policy by fine-tuning the leading text-to-video models to predict robot trajectories and training a lightweight diffusion policy for action generation. Given the lack of embodied knowledge in text-to-video models, we introduce a two-stage paradigm that fine-tunes independent text-to-flow and flow-to-video models derived from a pre-trained text-to-video model. Specifically, optical flow serves as an intermediate variable, providing a concise representation of subtle movements between images. The text-to-flow model predicts optical flow to concretize the intent of language instructions, and the flow-to-video model leverages this flow for fine-grained video prediction. Our method mitigates the ambiguity of language in single-stage text-to-video prediction and significantly reduces the robot-data requirement by avoiding direct use of low-level actions. In experiments, we collect high-quality manipulation data for real dual-arm robot, and the results of simulation and real-world experiments demonstrate the effectiveness of our method.
  </details>
