# 🔍 3D_Generation Papers · 2025-04-14

[![Total Papers](https://img.shields.io/badge/Papers-6-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[Training-free Guidance in Text-to-Video Generation via Multimodal Planning and Structured Noise Initialization](https://arxiv.org/abs/2504.08641)**  `arXiv:2504.08641`  `cs.CV` `cs.AI` `cs.CL`  
  _Jialu Li, Shoubin Yu, Han Lin, Jaemin Cho, Jaehong Yoon, Mohit Bansal_
  <details open><summary>Abstract</summary>
  Recent advancements in text-to-video (T2V) diffusion models have significantly enhanced the visual quality of the generated videos. However, even recent T2V models find it challenging to follow text descriptions accurately, especially when the prompt requires accurate control of spatial layouts or object trajectories. A recent line of research uses layout guidance for T2V models that require fine-tuning or iterative manipulation of the attention map during inference time. This significantly increases the memory requirement, making it difficult to adopt a large T2V model as a backbone. To address this, we introduce Video-MSG, a training-free Guidance method for T2V generation based on Multimodal planning and Structured noise initialization. Video-MSG consists of three steps, where in the first two steps, Video-MSG creates Video Sketch, a fine-grained spatio-temporal plan for the final video, specifying background, foreground, and object trajectories, in the form of draft video frames. In the last step, Video-MSG guides a downstream T2V diffusion model with Video Sketch through noise inversion and denoising. Notably, Video-MSG does not need fine-tuning or attention manipulation with additional memory during inference time, making it easier to adopt large T2V models. Video-MSG demonstrates its effectiveness in enhancing text alignment with multiple T2V backbones (VideoCrafter2 and CogVideoX-5B) on popular T2V generation benchmarks (T2VCompBench and VBench). We provide comprehensive ablation studies about noise inversion ratio, different background generators, background object detection, and foreground object segmentation.
  </details>

- **[Seaweed-7B: Cost-Effective Training of Video Generation Foundation Model](https://arxiv.org/abs/2504.08685)**  `arXiv:2504.08685`  `cs.CV` `cs.AI`  
  _Team Seawead, Ceyuan Yang, Zhijie Lin, Yang Zhao, Shanchuan Lin, Zhibei Ma, et al._
  <details open><summary>Abstract</summary>
  This technical report presents a cost-efficient strategy for training a video generation foundation model. We present a mid-sized research model with approximately 7 billion parameters (7B) called Seaweed-7B trained from scratch using 665,000 H100 GPU hours. Despite being trained with moderate computational resources, Seaweed-7B demonstrates highly competitive performance compared to contemporary video generation models of much larger size. Design choices are especially crucial in a resource-constrained setting. This technical report highlights the key design decisions that enhance the performance of the medium-sized diffusion model. Empirically, we make two observations: (1) Seaweed-7B achieves performance comparable to, or even surpasses, larger models trained on substantially greater GPU resources, and (2) our model, which exhibits strong generalization ability, can be effectively adapted across a wide range of downstream applications either by lightweight fine-tuning or continue training. See the project page atthis https URL
  </details>

- **[TokenMotion: Decoupled Motion Control via Token Disentanglement for Human-centric Video Generation](https://arxiv.org/abs/2504.08181)**  `arXiv:2504.08181`  `cs.CV` `cs.AI`  
  _Ruineng Li, Daitao Xing, Huiming Sun, Yuanzhou Ha, Jinglin Shen, Chiuman Ho_
  <details open><summary>Abstract</summary>
  Human-centric motion control in video generation remains a critical challenge, particularly when jointly controlling camera movements and human poses in scenarios like the iconic Grammy Glambot moment. While recent video diffusion models have made significant progress, existing approaches struggle with limited motion representations and inadequate integration of camera and human motion controls. In this work, we present TokenMotion, the first DiT-based video diffusion framework that enables fine-grained control over camera motion, human motion, and their joint interaction. We represent camera trajectories and human poses as spatio-temporal tokens to enable local control granularity. Our approach introduces a unified modeling framework utilizing a decouple-and-fuse strategy, bridged by a human-aware dynamic mask that effectively handles the spatially-and-temporally varying nature of combined motion signals. Through extensive experiments, we demonstrate TokenMotion's effectiveness across both text-to-video and image-to-video paradigms, consistently outperforming current state-of-the-art methods in human-centric motion control tasks. Our work represents a significant advancement in controllable video generation, with particular relevance for creative production applications.
  </details>

- **[RealCam-Vid: High-resolution Video Dataset with Dynamic Scenes and Metric-scale Camera Movements](https://arxiv.org/abs/2504.08212)**  `arXiv:2504.08212`  `cs.CV`  
  _Guangcong Zheng, Teng Li, Xianpan Zhou, Xi Li_
  <details open><summary>Abstract</summary>
  Recent advances in camera-controllable video generation have been constrained by the reliance on static-scene datasets with relative-scale camera annotations, such as RealEstate10K. While these datasets enable basic viewpoint control, they fail to capture dynamic scene interactions and lack metric-scale geometric consistency-critical for synthesizing realistic object motions and precise camera trajectories in complex environments. To bridge this gap, we introduce the first fully open-source, high-resolution dynamic-scene dataset with metric-scale camera annotations inthis https URL.
  </details>

- **[ELSA: A Style Aligned Dataset for Emotionally Intelligent Language Generation](https://arxiv.org/abs/2504.08281)**  `arXiv:2504.08281`  `cs.CL` `cs.AI` `cs.LG`  
  _Vishal Gandhi, Sagar Gandhi_
  <details open><summary>Abstract</summary>
  Advancements in emotion aware language processing increasingly shape vital NLP applications ranging from conversational AI and affective computing to computational psychology and creative content generation. Existing emotion datasets either lack emotional granularity or fail to capture necessary stylistic diversity, limiting the advancement of effective emotion conditioned text generation systems. Seeking to bridge this crucial gap between granularity and style diversity, this paper introduces a novel systematically constructed dataset named ELSA Emotion and Language Style Alignment Dataset leveraging fine grained emotion taxonomies adapted from existing sources such as dair ai emotion dataset and GoEmotions taxonomy. This dataset comprises multiple emotionally nuanced variations of original sentences regenerated across distinct contextual styles such as conversational, formal, poetic, and narrative, using advanced Large Language Models LLMs. Rigorous computational evaluation using metrics such as perplexity, embedding variance, readability, lexical diversity, and semantic coherence measures validates the datasets emotional authenticity, linguistic fluency, and textual diversity. Comprehensive metric analyses affirm its potential to support deeper explorations into emotion conditioned style adaptive text generation. By enabling precision tuned emotionally nuanced language modeling, our dataset creates fertile ground for research on fine grained emotional control, prompt driven explanation, interpretability, and style adaptive expressive language generation with LLMs.
  </details>

- **[Harnessing the Unseen: The Hidden Influence of Intrinsic Knowledge in Long-Context Language Models](https://arxiv.org/abs/2504.08202)**  `arXiv:2504.08202`  `cs.CL`  
  _Yu Fu, Haz Sameen Shahgir, Hui Liu, Xianfeng Tang, Qi He, Yue Dong_
  <details open><summary>Abstract</summary>
  Recent advances in long-context models (LCMs), designed to handle extremely long input contexts, primarily focus on utilizing external contextual information, often leaving the influence of large language models' intrinsic knowledge underexplored. In this work, we investigate how this intrinsic knowledge affects content generation and demonstrate that its impact becomes increasingly pronounced as context length extends. Furthermore, we show that the model's ability to utilize intrinsic knowledge, which we call intrinsic retrieval ability, does not improve simultaneously with its ability to leverage contextual knowledge through extrinsic retrieval ability. Moreover, better extrinsic retrieval can interfere with the model's ability to use its own knowledge effectively, limiting its full potential. To bridge this gap, we design a simple yet effective Hybrid Needle-in-a-Haystack test that evaluates models based on their capabilities across both retrieval abilities, rather than solely emphasizing extrinsic retrieval ability. Our experimental results reveal that Qwen-2.5 models significantly outperform Llama-3.1 models, demonstrating superior intrinsic retrieval ability. Moreover, even the more powerful Llama-3.1-70B-Instruct model fails to exhibit better performance under LCM conditions, highlighting the importance of evaluating models from a dual-retrieval perspective.
  </details>
