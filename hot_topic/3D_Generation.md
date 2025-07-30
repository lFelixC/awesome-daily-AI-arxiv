# 🔍 3D_Generation Papers · 2025-07-29

[![Total Papers](https://img.shields.io/badge/Papers-4-2688EB)]()
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
  We present FlagEvalMM, an open-source evaluation framework designed to comprehensively assess multimodal models across a diverse range of vision-language understanding and generation tasks, such as visual question answering, text-to-image/video generation, and image-text retrieval. We decouple model inference from evaluation through an independent evaluation service, thus enabling flexible resource allocation and seamless integration of new tasks and models. Moreover, FlagEvalMM utilizes advanced inference acceleration tools (e.g., vLLM, SGLang) and asynchronous data loading to significantly enhance evaluation efficiency. Extensive experiments show that FlagEvalMM offers accurate and efficient insights into model strengths and limitations, making it a valuable tool for advancing multimodal research. The framework is publicly accessible atthis https URL.
  </details>

- **[JWB-DH-V1: Benchmark for Joint Whole-Body Talking Avatar and Speech Generation Version 1](https://arxiv.org/abs/2507.20987)**  `arXiv:2507.20987`  `cs.CV` `cs.AI`  
  _Xinhan Di, Kristin Qi, Pengqian Yu_
  <details open><summary>Abstract</summary>
  Recent advances in diffusion-based video generation have enabled photo-realistic short clips, but current methods still struggle to achieve multi-modal consistency when jointly generating whole-body motion and natural speech. Current approaches lack comprehensive evaluation frameworks that assess both visual and audio quality, and there are insufficient benchmarks for region-specific performance analysis. To address these gaps, we introduce the Joint Whole-Body Talking Avatar and Speech Generation Version I(JWB-DH-V1), comprising a large-scale multi-modal dataset with 10,000 unique identities across 2 million video samples, and an evaluation protocol for assessing joint audio-video generation of whole-body animatable avatars. Our evaluation of SOTA models reveals consistent performance disparities between face/hand-centric and whole-body performance, which incidates essential areas for future research. The dataset and evaluation tools are publicly available atthis https URL.
  </details>

- **[DreamScene: 3D Gaussian-based End-to-end Text-to-3D Scene Generation](https://arxiv.org/abs/2507.13985)**  `arXiv:2507.13985`  `cs.CV`  
  _Haoran Li, Yuli Tian, Kun Lan, Yong Liao, Lin Wang, Pan Hui, et al._
  <details open><summary>Abstract</summary>
  Generating 3D scenes from natural language holds great promise for applications in gaming, film, and design. However, existing methods struggle with automation, 3D consistency, and fine-grained control. We present DreamScene, an end-to-end framework for high-quality and editable 3D scene generation from text or dialogue. DreamScene begins with a scene planning module, where a GPT-4 agent infers object semantics and spatial constraints to construct a hybrid graph. A graph-based placement algorithm then produces a structured, collision-free layout. Based on this layout, Formation Pattern Sampling (FPS) generates object geometry using multi-timestep sampling and reconstructive optimization, enabling fast and realistic synthesis. To ensure global consistent, DreamScene employs a progressive camera sampling strategy tailored to both indoor and outdoor settings. Finally, the system supports fine-grained scene editing, including object movement, appearance changes, and 4D dynamic motion. Experiments demonstrate that DreamScene surpasses prior methods in quality, consistency, and flexibility, offering a practical solution for open-domain 3D content creation. Code and demos are available atthis https URL.
  </details>

- **[NarrLV: Towards a Comprehensive Narrative-Centric Evaluation for Long Video Generation Models](https://arxiv.org/abs/2507.11245)**  `arXiv:2507.11245`  `cs.CV`  
  _X. Feng, H. Yu, M. Wu, S. Hu, J. Chen, C. Zhu, et al._
  <details open><summary>Abstract</summary>
  With the rapid development of foundation video generation technologies, long video generation models have exhibited promising research potential thanks to expanded content creation space. Recent studies reveal that the goal of long video generation tasks is not only to extend video duration but also to accurately express richer narrative content within longer videos. However, due to the lack of evaluation benchmarks specifically designed for long video generation models, the current assessment of these models primarily relies on benchmarks with simple narrative prompts (e.g., VBench). To the best of our knowledge, our proposed NarrLV is the first benchmark to comprehensively evaluate the Narrative expression capabilities of Long Video generation models. Inspired by film narrative theory, (i) we first introduce the basic narrative unit maintaining continuous visual presentation in videos as Temporal Narrative Atom (TNA), and use its count to quantitatively measure narrative richness. Guided by three key film narrative elements influencing TNA changes, we construct an automatic prompt generation pipeline capable of producing evaluation prompts with a flexibly expandable number of TNAs. (ii) Then, based on the three progressive levels of narrative content expression, we design an effective evaluation metric using the MLLM-based question generation and answering framework. (iii) Finally, we conduct extensive evaluations on existing long video generation models and the foundation generation models. Experimental results demonstrate that our metric aligns closely with human judgments. The derived evaluation outcomes reveal the detailed capability boundaries of current video generation models in narrative content expression.
  </details>
