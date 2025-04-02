# 🔍 Diffusion Papers · 2025-03-31

[![Total Papers](https://img.shields.io/badge/Papers-2-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Diffusion` `DDPM` `DDIM`  
**Filter**: `None`

---

## 📚 Paper List

- **[InstructRestore: Region-Customized Image Restoration with Human Instructions](http://arxiv.org/abs/2503.24357v1)**  `arXiv:2503.24357`  `cs.CV`  
  _Shuaizheng Liu, Jianqi Ma, Lingchen Sun, Xiangtao Kong, Lei Zhang_
  <details open><summary>Abstract</summary>
  Despite the significant progress in diffusion prior-based image restoration,most existing methods apply uniform processing to the entire image, lacking thecapability to perform region-customized image restoration according to userinstructions. In this work, we propose a new framework, namely InstructRestore,to perform region-adjustable image restoration following human instructions. Toachieve this, we first develop a data generation engine to produce trainingtriplets, each consisting of a high-quality image, the target regiondescription, and the corresponding region mask. With this engine and carefuldata screening, we construct a comprehensive dataset comprising 536,945triplets to support the training and evaluation of this task. We then examinehow to integrate the low-quality image features under the ControlNetarchitecture to adjust the degree of image details enhancement. Consequently,we develop a ControlNet-like model to identify the target region and allocatedifferent integration scales to the target and surrounding regions, enablingregion-customized image restoration that aligns with user instructions.Experimental results demonstrate that our proposed InstructRestore approachenables effective human-instructed image restoration, such as images with bokeheffects and user-instructed local enhancement. Our work advances theinvestigation of interactive image restoration and enhancement techniques.Data, code, and models will be found athttps://github.com/shuaizhengliu/InstructRestore.git.
  </details>

- **[ORAL: Prompting Your Large-Scale LoRAs via Conditional Recurrent Diffusion](http://arxiv.org/abs/2503.24354v1)**  `arXiv:2503.24354`  `cs.CL` `cs.AI` `cs.CV` `cs.LG`  
  _Rana Muhammad Shahroz Khan, Dongwen Tang, Pingzhi Li, Kai Wang, Tianlong Chen_
  <details open><summary>Abstract</summary>
  Parameter generation has emerged as a novel paradigm for neural networkdevelopment, offering an alternative to traditional neural network training bysynthesizing high-quality model weights directly. In the context of Low-RankAdaptation (LoRA) for evolving ($\textit{i.e.}$, constantly updated) largelanguage models (LLMs), this approach promises efficient adaptation withoutcostly retraining. However, existing methods face critical limitations insimultaneously achieving scalability and controllability. In this paper, weintroduce $\texttt{ORAL}$, a novel $\textbf{conditional recurrent diffusion}$framework that addresses these challenges. $\texttt{ORAL}$ incorporates a novelconditioning mechanism that integrates model architecture and textual taskspecifications, enabling the generation of task-specific LoRA parameters thatcan seamlessly transfer across evolving foundation models. Our approachsuccessfully scales to billions-of-parameter LLMs and maintainscontrollability. Through extensive experiments across seven language tasks,four vision tasks, and three multimodal tasks using five pre-trained LLMs, wedemonstrate that $\texttt{ORAL}$ generates high-quality LoRA parameters thatachieve comparable or superior performance to vanilla trained counterparts.
  </details>
