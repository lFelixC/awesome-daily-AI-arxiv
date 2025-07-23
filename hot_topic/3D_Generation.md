# 🔍 3D_Generation Papers · 2025-07-22

[![Total Papers](https://img.shields.io/badge/Papers-3-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[MotionShot: Adaptive Motion Transfer across Arbitrary Objects for Text-to-Video Generation](https://arxiv.org/abs/2507.16310)**  `arXiv:2507.16310`  `cs.CV`  
  _Yanchen Liu, Yanan Sun, Zhening Xing, Junyao Gao, Kai Chen, Wenjie Pei_
  <details open><summary>Abstract</summary>
  Existing text-to-video methods struggle to transfer motion smoothly from a reference object to a target object with significant differences in appearance or structure between them. To address this challenge, we introduce MotionShot, a training-free framework capable of parsing reference-target correspondences in a fine-grained manner, thereby achieving high-fidelity motion transfer while preserving coherence in appearance. To be specific, MotionShot first performs semantic feature matching to ensure high-level alignments between the reference and target objects. It then further establishes low-level morphological alignments through reference-to-target shape retargeting. By encoding motion with temporal attention, our MotionShot can coherently transfer motion across objects, even in the presence of significant appearance and structure disparities, demonstrated by extensive experiments. The project page is available at:this https URL.
  </details>

- **[PUSA V1.0: Surpassing Wan-I2V with $500 Training Cost by Vectorized Timestep Adaptation](https://arxiv.org/abs/2507.16116)**  `arXiv:2507.16116`  `cs.CV`  
  _Yaofang Liu, Yumeng Ren, Aitor Artola, Yuxuan Hu, Xiaodong Cun, Xiaotong Zhao, et al._
  <details open><summary>Abstract</summary>
  The rapid advancement of video diffusion models has been hindered by fundamental limitations in temporal modeling, particularly the rigid synchronization of frame evolution imposed by conventional scalar timestep variables. While task-specific adaptations and autoregressive models have sought to address these challenges, they remain constrained by computational inefficiency, catastrophic forgetting, or narrow applicability. In this work, we present Pusa, a groundbreaking paradigm that leverages vectorized timestep adaptation (VTA) to enable fine-grained temporal control within a unified video diffusion framework. Besides, VTA is a non-destructive adaptation, which means it fully preserves the capabilities of the base model. By finetuning the SOTA Wan2.1-T2V-14B model with VTA, we achieve unprecedented efficiency -- surpassing the performance of Wan-I2V-14B with $\leq$ 1/200 of the training cost (\$500 vs. $\geq$ \$100,000) and $\leq$ 1/2500 of the dataset size (4K vs. $\geq$ 10M samples). Pusa not only sets a new standard for image-to-video (I2V) generation, achieving a VBench-I2V total score of 87.32\% (vs. 86.86\% of Wan-I2V-14B), but also unlocks many zero-shot multi-task capabilities such as start-end frames and video extension -- all without task-specific training. Meanwhile, Pusa can still perform text-to-video generation. Mechanistic analyses reveal that our approach preserves the foundation model's generative priors while surgically injecting temporal dynamics, avoiding the combinatorial explosion inherent to vectorized timesteps. This work establishes a scalable, efficient, and versatile paradigm for next-generation video synthesis, democratizing high-fidelity video generation for research and industry alike. Code is open-sourced atthis https URL
  </details>

- **[EmotiCrafter: Text-to-Emotional-Image Generation based on Valence-Arousal Model](https://arxiv.org/abs/2501.05710)**  `arXiv:2501.05710`  `cs.CV`  
  _Shengqi Dang, Yi He, Long Ling, Ziqing Qian, Nanxuan Zhao, Nan Cao_
  <details open><summary>Abstract</summary>
  Recent research shows that emotions can enhance users' cognition and influence information communication. While research on visual emotion analysis is extensive, limited work has been done on helping users generate emotionally rich image content. Existing work on emotional image generation relies on discrete emotion categories, making it challenging to capture complex and subtle emotional nuances accurately. Additionally, these methods struggle to control the specific content of generated images based on text prompts. In this work, we introduce the new task of continuous emotional image content generation (C-EICG) and present EmotiCrafter, an emotional image generation model that generates images based on text prompts and Valence-Arousal values. Specifically, we propose a novel emotion-embedding mapping network that embeds Valence-Arousal values into textual features, enabling the capture of specific emotions in alignment with intended input prompts. Additionally, we introduce a loss function to enhance emotion expression. The experimental results show that our method effectively generates images representing specific emotions with the desired content and outperforms existing techniques.
  </details>
