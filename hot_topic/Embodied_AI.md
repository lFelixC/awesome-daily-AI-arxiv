# 🔍 Embodied_AI Papers · 2025-05-18

[![Total Papers](https://img.shields.io/badge/Papers-2-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[Conditioning Matters: Training Diffusion Policies is Faster Than You Think](https://arxiv.org/abs/2505.11123)**  `arXiv:2505.11123`  `cs.RO` `cs.AI`  
  _Zibin Dong, Yicheng Liu, Yinchuan Li, Hang Zhao, Jianye Hao_
  <details open><summary>Abstract</summary>
  Diffusion policies have emerged as a mainstream paradigm for building vision-language-action (VLA) models. Although they demonstrate strong robot control capabilities, their training efficiency remains suboptimal. In this work, we identify a fundamental challenge in conditional diffusion policy training: when generative conditions are hard to distinguish, the training objective degenerates into modeling the marginal action distribution, a phenomenon we term loss collapse. To overcome this, we propose Cocos, a simple yet general solution that modifies the source distribution in the conditional flow matching to be condition-dependent. By anchoring the source distribution around semantics extracted from condition inputs, Cocos encourages stronger condition integration and prevents the loss collapse. We provide theoretical justification and extensive empirical results across simulation and real-world benchmarks. Our method achieves faster convergence and higher success rates than existing approaches, matching the performance of large-scale pre-trained VLAs using significantly fewer gradient steps and parameters. Cocos is lightweight, easy to implement, and compatible with diverse policy architectures, offering a general-purpose improvement to diffusion policy training.
  </details>

- **[Unveiling the Potential of Vision-Language-Action Models with Open-Ended Multimodal Instructions](https://arxiv.org/abs/2505.11214)**  `arXiv:2505.11214`  `cs.RO`  
  _Wei Zhao, Gongsheng Li, Zhefei Gong, Pengxiang Ding, Han Zhao, Donglin Wang_
  <details open><summary>Abstract</summary>
  Vision-Language-Action (VLA) models have recently become highly prominent in the field of robotics. Leveraging vision-language foundation models trained on large-scale internet data, the VLA model can generate robotic actions directly from visual observations and human instructions through a single end-to-end neural network. Despite their effectiveness, current VLA models usually accept only one form of human prompting, language instructions, which may constrain their applicability in open-ended human-robot interactions. For example, a user might expect the robot to retrieve an object shown in an image, follow an instruction written on the whiteboard, or imitate a behavior demonstrated in a video, rather than relying solely on language-based descriptions. To address this gap, we introduce OE-VLA, which explores the potential of VLA models for open-ended multimodal instructions. Extensive results demonstrate that our OE-VLA not only achieves comparable performance to traditional VLA models with linguistic input but also delivers impressive results across four additional categories of open-ended tasks. The proposed methodology could significantly expand the applications of VLA models across various everyday scenarios and facilitate human-robot interaction.
  </details>
