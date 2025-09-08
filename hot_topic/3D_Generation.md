# 🔍 3D_Generation Papers · 2025-09-07

[![Total Papers](https://img.shields.io/badge/Papers-3-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[DirectorLLM for Human-Centric Video Generation](https://arxiv.org/abs/2412.14484)**  `arXiv:2412.14484`  `cs.CV`  
  _Kunpeng Song, Tingbo Hou, Zecheng He, Haoyu Ma, Jialiang Wang, Animesh Sinha, et al._
  <details open><summary>Abstract</summary>
  In this paper, we introduce DirectorLLM, a novel video generation model that employs a large language model (LLM) to orchestrate human poses within videos. As foundational text-to-video models rapidly evolve, the demand for high-quality human motion and interaction grows. To address this need and enhance the authenticity of human motions, we extend the LLM from a text generator to a video director and human motion simulator. Utilizing open-source resources from Llama 3, we train the DirectorLLM to generate detailed instructional signals, such as human poses, to guide video generation. This approach offloads the simulation of human motion from the video generator to the LLM, effectively creating informative outlines for human-centric scenes. These signals are used as conditions by the video renderer, facilitating more realistic and prompt-following video generation. As an independent LLM module, it can be applied to different video renderers, including UNet and DiT, with minimal effort. Experiments on automatic evaluation benchmarks and human evaluations show that our model outperforms existing ones in generating videos with higher human motion fidelity, improved prompt faithfulness, and enhanced rendered subject naturalness.
  </details>

- **[CoCoNUTS: Concentrating on Content while Neglecting Uninformative Textual Styles for AI-Generated Peer Review Detection](https://arxiv.org/abs/2509.04460)**  `arXiv:2509.04460`  `cs.CL` `cs.AI`  
  _Yihan Chen, Jiawei Chen, Guozhao Mo, Xuanang Chen, Ben He, Xianpei Han, et al._
  <details open><summary>Abstract</summary>
  The growing integration of large language models (LLMs) into the peer review process presents potential risks to the fairness and reliability of scholarly evaluation. While LLMs offer valuable assistance for reviewers with language refinement, there is growing concern over their use to generate substantive review content. Existing general AI-generated text detectors are vulnerable to paraphrasing attacks and struggle to distinguish between surface language refinement and substantial content generation, suggesting that they primarily rely on stylistic cues. When applied to peer review, this limitation can result in unfairly suspecting reviews with permissible AI-assisted language enhancement, while failing to catch deceptively humanized AI-generated reviews. To address this, we propose a paradigm shift from style-based to content-based detection. Specifically, we introduce CoCoNUTS, a content-oriented benchmark built upon a fine-grained dataset of AI-generated peer reviews, covering six distinct modes of human-AI collaboration. Furthermore, we develop CoCoDet, an AI review detector via a multi-task learning framework, designed to achieve more accurate and robust detection of AI involvement in review content. Our work offers a practical foundation for evaluating the use of LLMs in peer review, and contributes to the development of more precise, equitable, and reliable detection methods for real-world scholarly applications. Our code and data will be publicly available atthis https URL.
  </details>

- **[HuggingGraph: Understanding the Supply Chain of LLM Ecosystem](https://arxiv.org/abs/2507.14240)**  `arXiv:2507.14240`  `cs.CL` `cs.AI`  
  _Mohammad Shahedur Rahman, Peng Gao, Yuede Ji_
  <details open><summary>Abstract</summary>
  Large language models (LLMs) leverage deep learning architectures to process and predict sequences of words, enabling them to perform a wide range of natural language processing tasks, such as translation, summarization, question answering, and content generation. As existing LLMs are often built from base models or other pre-trained models and use external datasets, they can inevitably inherit vulnerabilities, biases, or malicious components that exist in previous models or datasets. Therefore, it is critical to understand these components' origin and development process to detect potential risks, improve model fairness, and ensure compliance with regulatory frameworks. Motivated by that, this project aims to study such relationships between models and datasets, which are the central parts of the LLM supply chain. First, we design a methodology to systematically collect LLMs' supply chain information. Then, we design a new graph to model the relationships between models and datasets, which is a directed heterogeneous graph, having 402,654 nodes and 462,524 edges. Lastly, we perform different types of analysis and make multiple interesting findings.
  </details>
