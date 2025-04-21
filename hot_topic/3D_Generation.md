# 🔍 3D_Generation Papers · 2025-04-20

[![Total Papers](https://img.shields.io/badge/Papers-4-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[Diffusion Transformers for Tabular Data Time Series Generation](https://arxiv.org/abs/2504.07566)**  `arXiv:2504.07566`  `cs.LG` `cs.AI`  
  _Fabrizio Garuti, Enver Sangineto, Simone Luetto, Lorenzo Forni, Rita Cucchiara_
  <details open><summary>Abstract</summary>
  Tabular data generation has recently attracted a growing interest due to its different application scenarios. However, generating time series of tabular data, where each element of the series depends on the others, remains a largely unexplored domain. This gap is probably due to the difficulty of jointly solving different problems, the main of which are the heterogeneity of tabular data (a problem common to non-time-dependent approaches) and the variable length of a time series. In this paper, we propose a Diffusion Transformers (DiTs) based approach for tabular data series generation. Inspired by the recent success of DiTs in image and video generation, we extend this framework to deal with heterogeneous data and variable-length sequences. Using extensive experiments on six datasets, we show that the proposed approach outperforms previous work by a large margin.
  </details>

- **[SkyReels-V2: Infinite-length Film Generative Model](https://arxiv.org/abs/2504.13074)**  `arXiv:2504.13074`  `cs.CV`  
  _Guibin Chen, Dixuan Lin, Jiangping Yang, Chunze Lin, Juncheng Zhu, Mingyuan Fan, et al._
  <details open><summary>Abstract</summary>
  Recent advances in video generation have been driven by diffusion models and autoregressive frameworks, yet critical challenges persist in harmonizing prompt adherence, visual quality, motion dynamics, and duration: compromises in motion dynamics to enhance temporal visual quality, constrained video duration (5-10 seconds) to prioritize resolution, and inadequate shot-aware generation stemming from general-purpose MLLMs' inability to interpret cinematic grammar, such as shot composition, actor expressions, and camera motions. These intertwined limitations hinder realistic long-form synthesis and professional film-style generation. To address these limitations, we propose SkyReels-V2, an Infinite-length Film Generative Model, that synergizes Multi-modal Large Language Model (MLLM), Multi-stage Pretraining, Reinforcement Learning, and Diffusion Forcing Framework. Firstly, we design a comprehensive structural representation of video that combines the general descriptions by the Multi-modal LLM and the detailed shot language by sub-expert models. Aided with human annotation, we then train a unified Video Captioner, named SkyCaptioner-V1, to efficiently label the video data. Secondly, we establish progressive-resolution pretraining for the fundamental video generation, followed by a four-stage post-training enhancement: Initial concept-balanced Supervised Fine-Tuning (SFT) improves baseline quality; Motion-specific Reinforcement Learning (RL) training with human-annotated and synthetic distortion data addresses dynamic artifacts; Our diffusion forcing framework with non-decreasing noise schedules enables long-video synthesis in an efficient search space; Final high-quality SFT refines visual fidelity. All the code and models are available atthis https URL.
  </details>

- **[LDM-ISP: Enhancing Neural ISP for Low Light with Latent Diffusion Models](https://arxiv.org/abs/2312.01027)**  `arXiv:2312.01027`  `cs.CV`  
  _Qiang Wen, Zhefan Rao, Yazhou Xing, Qifeng Chen_
  <details open><summary>Abstract</summary>
  Enhancing a low-light noisy RAW image into a well-exposed and clean sRGB image is a significant challenge for modern digital cameras. Prior approaches have difficulties in recovering fine-grained details and true colors of the scene under extremely low-light environments due to near-to-zero SNR. Meanwhile, diffusion models have shown significant progress towards general domain image generation. In this paper, we propose to leverage the pre-trained latent diffusion model to perform the neural ISP for enhancing extremely low-light images. Specifically, to tailor the pre-trained latent diffusion model to operate on the RAW domain, we train a set of lightweight taming modules to inject the RAW information into the diffusion denoising process via modulating the intermediate features of UNet. We further observe different roles of UNet denoising and decoder reconstruction in the latent diffusion model, which inspires us to decompose the low-light image enhancement task into latent-space low-frequency content generation and decoding-phase high-frequency detail maintenance. Through extensive experiments on representative datasets, we demonstrate our simple design not only achieves state-of-the-art performance in quantitative evaluations but also shows significant superiority in visual comparisons over strong baselines, which highlight the effectiveness of powerful generative priors for neural ISP under extremely low-light environments. The project page is available atthis https URL
  </details>

- **[LaMD: Latent Motion Diffusion for Image-Conditional Video Generation](https://arxiv.org/abs/2304.11603)**  `arXiv:2304.11603`  `cs.CV`  
  _Yaosi Hu, Zhenzhong Chen, Chong Luo_
  <details open><summary>Abstract</summary>
  The video generation field has witnessed rapid improvements with the introduction of recent diffusion models. While these models have successfully enhanced appearance quality, they still face challenges in generating coherent and natural movements while efficiently sampling videos. In this paper, we propose to condense video generation into a problem of motion generation, to improve the expressiveness of motion and make video generation more manageable. This can be achieved by breaking down the video generation process into latent motion generation and video reconstruction. Specifically, we present a latent motion diffusion (LaMD) framework, which consists of a motion-decomposed video autoencoder and a diffusion-based motion generator, to implement this idea. Through careful design, the motion-decomposed video autoencoder can compress patterns in movement into a concise latent motion representation. Consequently, the diffusion-based motion generator is able to efficiently generate realistic motion on a continuous latent space under multi-modal conditions, at a cost that is similar to that of image diffusion models. Results show that LaMD generates high-quality videos on various benchmark datasets, including BAIR, Landscape, NATOPS, MUG and CATER-GEN, that encompass a variety of stochastic dynamics and highly controllable movements on multiple image-conditional video generation tasks, while significantly decreases sampling time.
  </details>
