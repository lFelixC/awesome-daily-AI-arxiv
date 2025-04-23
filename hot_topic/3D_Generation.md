# 🔍 3D_Generation Papers · 2025-04-22

[![Total Papers](https://img.shields.io/badge/Papers-6-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[Grounded in Context: Retrieval-Based Method for Hallucination Detection](https://arxiv.org/abs/2504.15771)**  `arXiv:2504.15771`  `cs.LG`  
  _Assaf Gerner, Netta Madvil, Nadav Barak, Alex Zaikman, Jonatan Liberman, Liron Hamra, et al._
  <details open><summary>Abstract</summary>
  Despite advancements in grounded content generation, production Large Language Models (LLMs) based applications still suffer from hallucinated answers. We present "Grounded in Context" - Deepchecks' hallucination detection framework, designed for production-scale long-context data and tailored to diverse use cases, including summarization, data extraction, and RAG. Inspired by RAG architecture, our method integrates retrieval and Natural Language Inference (NLI) models to predict factual consistency between premises and hypotheses using an encoder-based model with only a 512-token context window. Our framework identifies unsupported claims with an F1 score of 0.83 in RAGTruth's response-level classification task, matching methods that trained on the dataset, and outperforming all comparable frameworks using similar-sized models.
  </details>

- **[Survey of Video Diffusion Models: Foundations, Implementations, and Applications](https://arxiv.org/abs/2504.16081)**  `arXiv:2504.16081`  `cs.CV` `cs.CL`  
  _Yimu Wang, Xuye Liu, Wei Pang, Li Ma, Shuai Yuan, Paul Debevec, et al._
  <details open><summary>Abstract</summary>
  Recent advances in diffusion models have revolutionized video generation, offering superior temporal consistency and visual quality compared to traditional generative adversarial networks-based approaches. While this emerging field shows tremendous promise in applications, it faces significant challenges in motion consistency, computational efficiency, and ethical considerations. This survey provides a comprehensive review of diffusion-based video generation, examining its evolution, technical foundations, and practical applications. We present a systematic taxonomy of current methodologies, analyze architectural innovations and optimization strategies, and investigate applications across low-level vision tasks such as denoising and super-resolution. Additionally, we explore the synergies between diffusionbased video generation and related domains, including video representation learning, question answering, and retrieval. Compared to the existing surveys (Lei et al., 2024a;b; Melnik et al., 2024; Cao et al., 2023; Xing et al., 2024c) which focus on specific aspects of video generation, such as human video synthesis (Lei et al., 2024a) or long-form content generation (Lei et al., 2024b), our work provides a broader, more updated, and more fine-grained perspective on diffusion-based approaches with a special section for evaluation metrics, industry solutions, and training engineering techniques in video generation. This survey serves as a foundational resource for researchers and practitioners working at the intersection of diffusion models and video generation, providing insights into both the theoretical frameworks and practical implementations that drive this rapidly evolving field. A structured list of related works involved in this survey is also available onthis https URL.
  </details>

- **[Efficient Temporal Consistency in Diffusion-Based Video Editing with Adaptor Modules: A Theoretical Framework](https://arxiv.org/abs/2504.16016)**  `arXiv:2504.16016`  `cs.CV`  
  _Xinyuan Song, Yangfan He, Sida Li, Jianhui Wang, Hongyang He, Xinhang Yuan, et al._
  <details open><summary>Abstract</summary>
  Adapter-based methods are commonly used to enhance model performance with minimal additional complexity, especially in video editing tasks that require frame-to-frame consistency. By inserting small, learnable modules into pretrained diffusion models, these adapters can maintain temporal coherence without extensive retraining. Approaches that incorporate prompt learning with both shared and frame-specific tokens are particularly effective in preserving continuity across frames at low training cost. In this work, we want to provide a general theoretical framework for adapters that maintain frame consistency in DDIM-based models under a temporal consistency loss. First, we prove that the temporal consistency objective is differentiable under bounded feature norms, and we establish a Lipschitz bound on its gradient. Second, we show that gradient descent on this objective decreases the loss monotonically and converges to a local minimum if the learning rate is within an appropriate range. Finally, we analyze the stability of modules in the DDIM inversion procedure, showing that the associated error remains controlled. These theoretical findings will reinforce the reliability of diffusion-based video editing methods that rely on adapter strategies and provide theoretical insights in video generation tasks.
  </details>

- **[Reasoning Physical Video Generation with Diffusion Timestep Tokens via Reinforcement Learning](https://arxiv.org/abs/2504.15932)**  `arXiv:2504.15932`  `cs.CV`  
  _Wang Lin, Liyu Jia, Wentao Hu, Kaihang Pan, Zhongqi Yue, Wei Zhao, et al._
  <details open><summary>Abstract</summary>
  Despite recent progress in video generation, producing videos that adhere to physical laws remains a significant challenge. Traditional diffusion-based methods struggle to extrapolate to unseen physical conditions (eg, velocity) due to their reliance on data-driven approximations. To address this, we propose to integrate symbolic reasoning and reinforcement learning to enforce physical consistency in video generation. We first introduce the Diffusion Timestep Tokenizer (DDT), which learns discrete, recursive visual tokens by recovering visual attributes lost during the diffusion process. The recursive visual tokens enable symbolic reasoning by a large language model. Based on it, we propose the Phys-AR framework, which consists of two stages: The first stage uses supervised fine-tuning to transfer symbolic knowledge, while the second stage applies reinforcement learning to optimize the model's reasoning abilities through reward functions based on physical conditions. Our approach allows the model to dynamically adjust and improve the physical properties of generated videos, ensuring adherence to physical laws. Experimental results demonstrate that PhysAR can generate videos that are physically consistent.
  </details>

- **[Satellite to GroundScape -- Large-scale Consistent Ground View Generation from Satellite Views](https://arxiv.org/abs/2504.15786)**  `arXiv:2504.15786`  `cs.CV`  
  _Ningli Xu, Rongjun Qin_
  <details open><summary>Abstract</summary>
  Generating consistent ground-view images from satellite imagery is challenging, primarily due to the large discrepancies in viewing angles and resolution between satellite and ground-level domains. Previous efforts mainly concentrated on single-view generation, often resulting in inconsistencies across neighboring ground views. In this work, we propose a novel cross-view synthesis approach designed to overcome these challenges by ensuring consistency across ground-view images generated from satellite views. Our method, based on a fixed latent diffusion model, introduces two conditioning modules: satellite-guided denoising, which extracts high-level scene layout to guide the denoising process, and satellite-temporal denoising, which captures camera motion to maintain consistency across multiple generated views. We further contribute a large-scale satellite-ground dataset containing over 100,000 perspective pairs to facilitate extensive ground scene or video generation. Experimental results demonstrate that our approach outperforms existing methods on perceptual and temporal metrics, achieving high photorealism and consistency in multi-view outputs.
  </details>

- **[DiTPainter: Efficient Video Inpainting with Diffusion Transformers](https://arxiv.org/abs/2504.15661)**  `arXiv:2504.15661`  `cs.CV`  
  _Xian Wu, Chang Liu_
  <details open><summary>Abstract</summary>
  Many existing video inpainting algorithms utilize optical flows to construct the corresponding maps and then propagate pixels from adjacent frames to missing areas by mapping. Despite the effectiveness of the propagation mechanism, they might encounter blurry and inconsistencies when dealing with inaccurate optical flows or large masks. Recently, Diffusion Transformer (DiT) has emerged as a revolutionary technique for video generation tasks. However, pretrained DiT models for video generation all contain a large amount of parameters, which makes it very time consuming to apply to video inpainting tasks. In this paper, we present DiTPainter, an end-to-end video inpainting model based on Diffusion Transformer (DiT). DiTPainter uses an efficient transformer network designed for video inpainting, which is trained from scratch instead of initializing from any large pretrained models. DiTPainter can address videos with arbitrary lengths and can be applied to video decaptioning and video completion tasks with an acceptable time cost. Experiments show that DiTPainter outperforms existing video inpainting algorithms with higher quality and better spatial-temporal consistency.
  </details>
