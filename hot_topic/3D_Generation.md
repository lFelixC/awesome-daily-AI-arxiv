# 🔍 3D_Generation Papers · 2025-06-17

[![Total Papers](https://img.shields.io/badge/Papers-5-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[FlagEvalMM: A Flexible Framework for Comprehensive Multimodal Model Evaluation](https://arxiv.org/abs/2506.09081)**  `arXiv:2506.09081`  `cs.CV` `cs.AI` `cs.CL`  
  _Zheqi He, Yesheng Liu, Jing-shu Zheng, Xuejing Li, Jin-Ge Yao, Bowen Qin, et al._
  <details open><summary>Abstract</summary>
  We present FlagEvalMM, an open-source evaluation framework designed to comprehensively assess multimodal models across a diverse range of vision-language understanding and generation tasks, such as visual question answering, text-to-image/video generation, and image-text retrieval. We decouple model inference from evaluation through an independent evaluation service, thus enabling flexible resource allocation and seamless integration of new tasks and models. Moreover, FlagEvalMM utilizes advanced inference acceleration tools (e.g., vLLM, SGLang) and asynchronous data loading to significantly enhance evaluation efficiency. Extensive experiments show that FlagEvalMM offers accurate and efficient insights into model strengths and limitations, making it a valuable tool for advancing multimodal research. The framework is publicly accessible athttps://github.com/flageval-baai/FlagEvalMM.
  </details>

- **[Causally Steered Diffusion for Automated Video Counterfactual Generation](https://arxiv.org/abs/2506.14404)**  `arXiv:2506.14404`  `cs.CV` `cs.AI`  
  _Nikos Spyrou, Athanasios Vlontzos, Paraskevas Pegios, Thomas Melistas, Nefeli Gkouti, Yannis Panagakis, et al._
  <details open><summary>Abstract</summary>
  Adapting text-to-image (T2I) latent diffusion models for video editing has shown strong visual fidelity and controllability, but challenges remain in maintaining causal relationships in video content. Edits affecting causally dependent attributes risk generating unrealistic or misleading outcomes if these relationships are ignored. In this work, we propose a causally faithful framework for counterfactual video generation, guided by a vision-language model (VLM). Our method is agnostic to the underlying video editing system and does not require access to its internal mechanisms or finetuning. Instead, we guide the generation by optimizing text prompts based on an assumed causal graph, addressing the challenge of latent space control in LDMs. We evaluate our approach using standard video quality metrics and counterfactual-specific criteria, such as causal effectiveness and minimality. Our results demonstrate that causally faithful video counterfactuals can be effectively generated within the learned distribution of LDMs through prompt-based causal steering. With its compatibility with any black-box video editing system, our method holds significant potential for generating realistic "what-if" video scenarios in diverse areas such as healthcare and digital media.
  </details>

- **[VideoMAR: Autoregressive Video Generatio with Continuous Tokens](https://arxiv.org/abs/2506.14168)**  `arXiv:2506.14168`  `cs.CV` `cs.AI`  
  _Hu Yu, Biao Gong, Hangjie Yuan, DanDan Zheng, Weilong Chai, Jingdong Chen, et al._
  <details open><summary>Abstract</summary>
  Masked-based autoregressive models have demonstrated promising image generation capability in continuous space. However, their potential for video generation remains under-explored. In this paper, we propose \textbf{VideoMAR}, a concise and efficient decoder-only autoregressive image-to-video model with continuous tokens, composing temporal frame-by-frame and spatial masked generation. We first identify temporal causality and spatial bi-directionality as the first principle of video AR models, and propose the next-frame diffusion loss for the integration of mask and video generation. Besides, the huge cost and difficulty of long sequence autoregressive modeling is a basic but crucial issue. To this end, we propose the temporal short-to-long curriculum learning and spatial progressive resolution training, and employ progressive temperature strategy at inference time to mitigate the accumulation error. Furthermore, VideoMAR replicates several unique capacities of language models to video generation. It inherently bears high efficiency due to simultaneous temporal-wise KV cache and spatial-wise parallel generation, and presents the capacity of spatial and temporal extrapolation via 3D rotary embeddings. On the VBench-I2V benchmark, VideoMAR surpasses the previous state-of-the-art (Cosmos I2V) while requiring significantly fewer parameters ($9.3\%$), training data ($0.5\%$), and GPU resources ($0.2\%$).
  </details>

- **[Hardware-Friendly Static Quantization Method for Video Diffusion Transformers](https://arxiv.org/abs/2502.15077)**  `arXiv:2502.15077`  `cs.CV` `cs.AI`  
  _Sanghyun Yi, Qingfeng Liu, Mostafa El-Khamy_
  <details open><summary>Abstract</summary>
  Diffusion Transformers for video generation have gained significant research interest since the impressive performance of SORA. Efficient deployment of such generative-AI models on GPUs has been demonstrated with dynamic quantization. However, resource-constrained devices cannot support dynamic quantization, and need static quantization of the models for their efficient deployment on AI processors. In this paper, we propose a novel method for the post-training quantization of OpenSora\cite{opensora}, a Video Diffusion Transformer, without relying on dynamic quantization techniques. Our approach employs static quantization, achieving video quality comparable to FP16 and dynamically quantized ViDiT-Q methods, as measured by CLIP, and VQA metrics. In particular, we utilize per-step calibration data to adequately provide a post-training statically quantized model for each time step, incorporating channel-wise quantization for weights and tensor-wise quantization for activations. By further applying the smooth-quantization technique, we can obtain high-quality video outputs with the statically quantized models. Extensive experimental results demonstrate that static quantization can be a viable alternative to dynamic quantization for video diffusion transformers, offering a more efficient approach without sacrificing performance.
  </details>

- **[LARP: Tokenizing Videos with a Learned Autoregressive Generative Prior](https://arxiv.org/abs/2410.21264)**  `arXiv:2410.21264`  `cs.CV` `cs.AI`  
  _Hanyu Wang, Saksham Suri, Yixuan Ren, Hao Chen, Abhinav Shrivastava_
  <details open><summary>Abstract</summary>
  We present LARP, a novel video tokenizer designed to overcome limitations in current video tokenization methods for autoregressive (AR) generative models. Unlike traditional patchwise tokenizers that directly encode local visual patches into discrete tokens, LARP introduces a holistic tokenization scheme that gathers information from the visual content using a set of learned holistic queries. This design allows LARP to capture more global and semantic representations, rather than being limited to local patch-level information. Furthermore, it offers flexibility by supporting an arbitrary number of discrete tokens, enabling adaptive and efficient tokenization based on the specific requirements of the task. To align the discrete token space with downstream AR generation tasks, LARP integrates a lightweight AR transformer as a training-time prior model that predicts the next token on its discrete latent space. By incorporating the prior model during training, LARP learns a latent space that is not only optimized for video reconstruction but is also structured in a way that is more conducive to autoregressive generation. Moreover, this process defines a sequential order for the discrete tokens, progressively pushing them toward an optimal configuration during training, ensuring smoother and more accurate AR generation at inference time. Comprehensive experiments demonstrate LARP's strong performance, achieving state-of-the-art FVD on the UCF101 class-conditional video generation benchmark. LARP enhances the compatibility of AR models with videos and opens up the potential to build unified high-fidelity multimodal large language models (MLLMs).
  </details>
