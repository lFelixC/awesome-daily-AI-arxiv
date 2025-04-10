# 🔍 3D_Generation Papers · 2025-04-09

[![Total Papers](https://img.shields.io/badge/Papers-2-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[EIDT-V: Exploiting Intersections in Diffusion Trajectories for Model-Agnostic, Zero-Shot, Training-Free Text-to-Video Generation](https://arxiv.org/abs/2504.06861)**  `arXiv:2504.06861`  `cs.CV` `cs.AI`  
  _Diljeet Jagpal, Xi Chen, Vinay P. Namboodiri_
  <details open><summary>Abstract</summary>
  Zero-shot, training-free, image-based text-to-video generation is an emerging area that aims to generate videos using existing image-based diffusion models. Current methods in this space require specific architectural changes to image generation models, which limit their adaptability and scalability. In contrast to such methods, we provide a model-agnostic approach. We use intersections in diffusion trajectories, working only with the latent values. We could not obtain localized frame-wise coherence and diversity using only the intersection of trajectories. Thus, we instead use a grid-based approach. An in-context trained LLM is used to generate coherent frame-wise prompts; another is used to identify differences between frames. Based on these, we obtain a CLIP-based attention mask that controls the timing of switching the prompts for each grid cell. Earlier switching results in higher variance, while later switching results in more coherence. Therefore, our approach can ensure appropriate control between coherence and variance for the frames. Our approach results in state-of-the-art performance while being more flexible when working with diverse image-generation models. The empirical analysis using quantitative metrics and user studies confirms our model's superior temporal consistency, visual fidelity and user satisfaction, thus providing a novel way to obtain training-free, image-based text-to-video generation.
  </details>

- **[RAGME: Retrieval Augmented Video Generation for Enhanced Motion Realism](https://arxiv.org/abs/2504.06672)**  `arXiv:2504.06672`  `cs.CV`  
  _Elia Peruzzo, Dejia Xu, Xingqian Xu, Humphrey Shi, Nicu Sebe_
  <details open><summary>Abstract</summary>
  Video generation is experiencing rapid growth, driven by advances in diffusion models and the development of better and larger datasets. However, producing high-quality videos remains challenging due to the high-dimensional data and the complexity of the task. Recent efforts have primarily focused on enhancing visual quality and addressing temporal inconsistencies, such as flickering. Despite progress in these areas, the generated videos often fall short in terms of motion complexity and physical plausibility, with many outputs either appearing static or exhibiting unrealistic motion. In this work, we propose a framework to improve the realism of motion in generated videos, exploring a complementary direction to much of the existing literature. Specifically, we advocate for the incorporation of a retrieval mechanism during the generation phase. The retrieved videos act as grounding signals, providing the model with demonstrations of how the objects move. Our pipeline is designed to apply to any text-to-video diffusion model, conditioning a pretrained model on the retrieved samples with minimal fine-tuning. We demonstrate the superiority of our approach through established metrics, recently proposed benchmarks, and qualitative results, and we highlight additional applications of the framework.
  </details>
