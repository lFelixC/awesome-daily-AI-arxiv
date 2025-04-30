# 🔍 3D_Generation Papers · 2025-04-29

[![Total Papers](https://img.shields.io/badge/Papers-6-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[DDPS: Discrete Diffusion Posterior Sampling for Paths in Layered Graphs](https://arxiv.org/abs/2504.20754)**  `arXiv:2504.20754`  `cs.LG`  
  _Hao Luan, See-Kiong Ng, Chun Kai Ling_
  <details open><summary>Abstract</summary>
  Diffusion models form an important class of generative models today, accounting for much of the state of the art in cutting edge AI research. While numerous extensions beyond image and video generation exist, few of such approaches address the issue of explicit constraints in the samples generated. In this paper, we study the problem of generating paths in a layered graph (a variant of a directed acyclic graph) using discrete diffusion models, while guaranteeing that our generated samples are indeed paths. Our approach utilizes a simple yet effective representation for paths which we call the padded adjacency-list matrix (PALM). In addition, we show how to effectively perform classifier guidance, which helps steer the sampled paths to specific preferred edges without any retraining of the diffusion model. Our preliminary results show that empirically, our method outperforms alternatives which do not explicitly account for path constraints.
  </details>

- **[The Best of Both Worlds: Integrating Language Models and Diffusion Models for Video Generation](https://arxiv.org/abs/2503.04606)**  `arXiv:2503.04606`  `cs.CV` `cs.AI` `cs.CL` `cs.LG`  
  _Aoxiong Yin, Kai Shen, Yichong Leng, Xu Tan, Xinyu Zhou, Juncheng Li, et al._
  <details open><summary>Abstract</summary>
  Recent advancements in text-to-video (T2V) generation have been driven by two competing paradigms: autoregressive language models and diffusion models. However, each paradigm has intrinsic limitations: language models struggle with visual quality and error accumulation, while diffusion models lack semantic understanding and causal modeling. In this work, we propose LanDiff, a hybrid framework that synergizes the strengths of both paradigms through coarse-to-fine generation. Our architecture introduces three key innovations: (1) a semantic tokenizer that compresses 3D visual features into compact 1D discrete representations through efficient semantic compression, achieving a $\sim$14,000$\times$ compression ratio; (2) a language model that generates semantic tokens with high-level semantic relationships; (3) a streaming diffusion model that refines coarse semantics into high-fidelity videos. Experiments show that LanDiff, a 5B model, achieves a score of 85.43 on the VBench T2V benchmark, surpassing the state-of-the-art open-source models Hunyuan Video (13B) and other commercial models such as Sora, Kling, and Hailuo. Furthermore, our model also achieves state-of-the-art performance in long video generation, surpassing other open-source models in this field. Our demo can be viewed atthis https URL.
  </details>

- **[Video-Bench: Human-Aligned Video Generation Benchmark](https://arxiv.org/abs/2504.04907)**  `arXiv:2504.04907`  `cs.CV` `cs.AI`  
  _Hui Han, Siyuan Li, Jiaqi Chen, Yiwen Yuan, Yuling Wu, Chak Tou Leong, et al._
  <details open><summary>Abstract</summary>
  Video generation assessment is essential for ensuring that generative models produce visually realistic, high-quality videos while aligning with human expectations. Current video generation benchmarks fall into two main categories: traditional benchmarks, which use metrics and embeddings to evaluate generated video quality across multiple dimensions but often lack alignment with human judgments; and large language model (LLM)-based benchmarks, though capable of human-like reasoning, are constrained by a limited understanding of video quality metrics and cross-modal consistency. To address these challenges and establish a benchmark that better aligns with human preferences, this paper introduces Video-Bench, a comprehensive benchmark featuring a rich prompt suite and extensive evaluation dimensions. This benchmark represents the first attempt to systematically leverage MLLMs across all dimensions relevant to video generation assessment in generative models. By incorporating few-shot scoring and chain-of-query techniques, Video-Bench provides a structured, scalable approach to generated video evaluation. Experiments on advanced models including Sora demonstrate that Video-Bench achieves superior alignment with human preferences across all dimensions. Moreover, in instances where our framework's assessments diverge from human evaluations, it consistently offers more objective and accurate insights, suggesting an even greater potential advantage over traditional human judgment.
  </details>

- **[Image Interpolation with Score-based Riemannian Metrics of Diffusion Models](https://arxiv.org/abs/2504.20288)**  `arXiv:2504.20288`  `cs.CV`  
  _Shinnosuke Saito, Takashi Matsubara_
  <details open><summary>Abstract</summary>
  Diffusion models excel in content generation by implicitly learning the data manifold, yet they lack a practical method to leverage this manifold - unlike other deep generative models equipped with latent spaces. This paper introduces a novel framework that treats the data space of pre-trained diffusion models as a Riemannian manifold, with a metric derived from the score function. Experiments with MNIST and Stable Diffusion show that this geometry-aware approach yields image interpolations that are more realistic, less noisy, and more faithful to prompts than existing methods, demonstrating its potential for improved content generation and editing.
  </details>

- **[HANDI: Hand-Centric Text-and-Image Conditioned Video Generation](https://arxiv.org/abs/2412.04189)**  `arXiv:2412.04189`  `cs.CV`  
  _Yayuan Li, Zhi Cao, Jason J. Corso_
  <details open><summary>Abstract</summary>
  Despite the recent strides in video generation, state-of-the-art methods still struggle with elements of visual detail. One particularly challenging case is the class of videos in which the intricate motion of the hand coupled with a mostly stable and otherwise distracting environment is necessary to convey the execution of some complex action and its effects. To address these challenges, we introduce a new method for video generation that focuses on hand-centric actions. Our diffusion-based method incorporates two distinct innovations. First, we propose an automatic method to generate the motion area -- the region in the video in which the detailed activities occur -- guided by both the visual context and the action text prompt, rather than assuming this region can be provided manually as is now commonplace. Second, we introduce a critical Hand Refinement Loss to guide the diffusion model to focus on smooth and consistent hand poses. We evaluate our method on challenging augmented datasets based on EpicKitchens and Ego4D, demonstrating significant improvements over state-of-the-art methods in terms of action clarity, especially of the hand motion in the target region, across diverse environments and actions. Video results can be found inthis https URL
  </details>

- **[JaccDiv: A Metric and Benchmark for Quantifying Diversity of Generated Marketing Text in the Music Industry](https://arxiv.org/abs/2504.20849)**  `arXiv:2504.20849`  `cs.CL`  
  _Anum Afzal, Alexandre Mercier, Florian Matthes_
  <details open><summary>Abstract</summary>
  Online platforms are increasingly interested in using Data-to-Text technologies to generate content and help their users. Unfortunately, traditional generative methods often fall into repetitive patterns, resulting in monotonous galleries of texts after only a few iterations. In this paper, we investigate LLM-based data-to-text approaches to automatically generate marketing texts that are of sufficient quality and diverse enough for broad adoption. We leverage Language Models such as T5, GPT-3.5, GPT-4, and LLaMa2 in conjunction with fine-tuning, few-shot, and zero-shot approaches to set a baseline for diverse marketing texts. We also introduce a metric JaccDiv to evaluate the diversity of a set of texts. This research extends its relevance beyond the music industry, proving beneficial in various fields where repetitive automated content generation is prevalent.
  </details>
