# 🔍 3D_Generation Papers · 2025-07-19

[![Total Papers](https://img.shields.io/badge/Papers-4-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[World Model-Based End-to-End Scene Generation for Accident Anticipation in Autonomous Driving](https://arxiv.org/abs/2507.12762)**  `arXiv:2507.12762`  `cs.CV` `cs.LG`  
  _Yanchen Guan, Haicheng Liao, Chengyue Wang, Xingcheng Liu, Jiaxun Zhang, Zhenning Li_
  <details open><summary>Abstract</summary>
  Reliable anticipation of traffic accidents is essential for advancing autonomous driving systems. However, this objective is limited by two fundamental challenges: the scarcity of diverse, high-quality training data and the frequent absence of crucial object-level cues due to environmental disruptions or sensor deficiencies. To tackle these issues, we propose a comprehensive framework combining generative scene augmentation with adaptive temporal reasoning. Specifically, we develop a video generation pipeline that utilizes a world model guided by domain-informed prompts to create high-resolution, statistically consistent driving scenarios, particularly enriching the coverage of edge cases and complex interactions. In parallel, we construct a dynamic prediction model that encodes spatio-temporal relationships through strengthened graph convolutions and dilated temporal operators, effectively addressing data incompleteness and transient visual noise. Furthermore, we release a new benchmark dataset designed to better capture diverse real-world driving risks. Extensive experiments on public and newly released datasets confirm that our framework enhances both the accuracy and lead time of accident anticipation, offering a robust solution to current data and modeling limitations in safety-critical autonomous driving applications.
  </details>

- **[Leveraging Pre-Trained Visual Models for AI-Generated Video Detection](https://arxiv.org/abs/2507.13224)**  `arXiv:2507.13224`  `cs.CV`  
  _Keerthi Veeramachaneni, Praveen Tirupattur, Amrit Singh Bedi, Mubarak Shah_
  <details open><summary>Abstract</summary>
  Recent advances in Generative AI (GenAI) have led to significant improvements in the quality of generated visual content. As AI-generated visual content becomes increasingly indistinguishable from real content, the challenge of detecting the generated content becomes critical in combating misinformation, ensuring privacy, and preventing security threats. Although there has been substantial progress in detecting AI-generated images, current methods for video detection are largely focused on deepfakes, which primarily involve human faces. However, the field of video generation has advanced beyond DeepFakes, creating an urgent need for methods capable of detecting AI-generated videos with generic content. To address this gap, we propose a novel approach that leverages pre-trained visual models to distinguish between real and generated videos. The features extracted from these pre-trained models, which have been trained on extensive real visual content, contain inherent signals that can help distinguish real from generated videos. Using these extracted features, we achieve high detection performance without requiring additional model training, and we further improve performance by training a simple linear classification layer on top of the extracted features. We validated our method on a dataset we compiled (VID-AID), which includes around 10,000 AI-generated videos produced by 9 different text-to-video models, along with 4,000 real videos, totaling over 7 hours of video content. Our evaluation shows that our approach achieves high detection accuracy, above 90% on average, underscoring its effectiveness. Upon acceptance, we plan to publicly release the code, the pre-trained models, and our dataset to support ongoing research in this critical area.
  </details>

- **[LoViC: Efficient Long Video Generation with Context Compression](https://arxiv.org/abs/2507.12952)**  `arXiv:2507.12952`  `cs.CV`  
  _Jiaxiu Jiang, Wenbo Li, Jingjing Ren, Yuping Qiu, Yong Guo, Xiaogang Xu, et al._
  <details open><summary>Abstract</summary>
  Despite recent advances in diffusion transformers (DiTs) for text-to-video generation, scaling to long-duration content remains challenging due to the quadratic complexity of self-attention. While prior efforts -- such as sparse attention and temporally autoregressive models -- offer partial relief, they often compromise temporal coherence or scalability. We introduce LoViC, a DiT-based framework trained on million-scale open-domain videos, designed to produce long, coherent videos through a segment-wise generation process. At the core of our approach is FlexFormer, an expressive autoencoder that jointly compresses video and text into unified latent representations. It supports variable-length inputs with linearly adjustable compression rates, enabled by a single query token design based on the Q-Former architecture. Additionally, by encoding temporal context through position-aware mechanisms, our model seamlessly supports prediction, retradiction, interpolation, and multi-shot generation within a unified paradigm. Extensive experiments across diverse tasks validate the effectiveness and versatility of our approach.
  </details>

- **[MIDI: Multi-Instance Diffusion for Single Image to 3D Scene Generation](https://arxiv.org/abs/2412.03558)**  `arXiv:2412.03558`  `cs.CV`  
  _Zehuan Huang, Yuan-Chen Guo, Xingqiao An, Yunhan Yang, Yangguang Li, Zi-Xin Zou, et al._
  <details open><summary>Abstract</summary>
  This paper introduces MIDI, a novel paradigm for compositional 3D scene generation from a single image. Unlike existing methods that rely on reconstruction or retrieval techniques or recent approaches that employ multi-stage object-by-object generation, MIDI extends pre-trained image-to-3D object generation models to multi-instance diffusion models, enabling the simultaneous generation of multiple 3D instances with accurate spatial relationships and high generalizability. At its core, MIDI incorporates a novel multi-instance attention mechanism, that effectively captures inter-object interactions and spatial coherence directly within the generation process, without the need for complex multi-step processes. The method utilizes partial object images and global scene context as inputs, directly modeling object completion during 3D generation. During training, we effectively supervise the interactions between 3D instances using a limited amount of scene-level data, while incorporating single-object data for regularization, thereby maintaining the pre-trained generalization ability. MIDI demonstrates state-of-the-art performance in image-to-scene generation, validated through evaluations on synthetic data, real-world scene data, and stylized scene images generated by text-to-image diffusion models.
  </details>
