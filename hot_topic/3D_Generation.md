# 🔍 3D_Generation Papers · 2025-05-14

[![Total Papers](https://img.shields.io/badge/Papers-3-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[Generating time-consistent dynamics with discriminator-guided image diffusion models](https://arxiv.org/abs/2505.09089)**  `arXiv:2505.09089`  `cs.LG`  
  _Philipp Hess, Maximilian Gelbrecht, Christof Schötz, Michael Aich, Yu Huang, Shangshang Yang, et al._
  <details open><summary>Abstract</summary>
  Realistic temporal dynamics are crucial for many video generation, processing and modelling applications, e.g. in computational fluid dynamics, weather prediction, or long-term climate simulations. Video diffusion models (VDMs) are the current state-of-the-art method for generating highly realistic dynamics. However, training VDMs from scratch can be challenging and requires large computational resources, limiting their wider application. Here, we propose a time-consistency discriminator that enables pretrained image diffusion models to generate realistic spatiotemporal dynamics. The discriminator guides the sampling inference process and does not require extensions or finetuning of the image diffusion model. We compare our approach against a VDM trained from scratch on an idealized turbulence simulation and a real-world global precipitation dataset. Our approach performs equally well in terms of temporal consistency, shows improved uncertainty calibration and lower biases compared to the VDM, and achieves stable centennial-scale climate simulations at daily time steps.
  </details>

- **[A Comprehensive Social Bias Audit of Contrastive Vision Language Models](https://arxiv.org/abs/2501.13223)**  `arXiv:2501.13223`  `cs.LG`  
  _Zahraa Al Sahili, Ioannis Patras, Matthew Purver_
  <details open><summary>Abstract</summary>
  In the domain of text-to-image generative models, biases inherent in training datasets often propagate into generated content, posing significant ethical challenges, particularly in socially sensitive contexts. We introduce FairCoT, a novel framework that enhances fairness in text-to-image models through Chain-of-Thought (CoT) reasoning within multimodal generative large language models. FairCoT employs iterative CoT refinement to systematically mitigate biases, and dynamically adjusts textual prompts in real time, ensuring diverse and equitable representation in generated images. By integrating iterative reasoning processes, FairCoT addresses the limitations of zero-shot CoT in sensitive scenarios, balancing creativity with ethical responsibility. Experimental evaluations across popular text-to-image systems--including DALL-E and various Stable Diffusion variants--demonstrate that FairCoT significantly enhances fairness and diversity without sacrificing image quality or semantic fidelity. By combining robust reasoning, lightweight deployment, and extensibility to multiple models, FairCoT represents a promising step toward more socially responsible and transparent AI-driven content generation.
  </details>

- **[Generative AI for Autonomous Driving: Frontiers and Opportunities](https://arxiv.org/abs/2505.08854)**  `arXiv:2505.08854`  `cs.CV` `cs.AI` `cs.RO`  
  _Yuping Wang, Shuo Xing, Cui Can, Renjie Li, Hongyuan Hua, Kexin Tian, et al._
  <details open><summary>Abstract</summary>
  Generative Artificial Intelligence (GenAI) constitutes a transformative technological wave that reconfigures industries through its unparalleled capabilities for content creation, reasoning, planning, and multimodal understanding. This revolutionary force offers the most promising path yet toward solving one of engineering's grandest challenges: achieving reliable, fully autonomous driving, particularly the pursuit of Level 5 autonomy. This survey delivers a comprehensive and critical synthesis of the emerging role of GenAI across the autonomous driving stack. We begin by distilling the principles and trade-offs of modern generative modeling, encompassing VAEs, GANs, Diffusion Models, and Large Language Models (LLMs). We then map their frontier applications in image, LiDAR, trajectory, occupancy, video generation as well as LLM-guided reasoning and decision making. We categorize practical applications, such as synthetic data workflows, end-to-end driving strategies, high-fidelity digital twin systems, smart transportation networks, and cross-domain transfer to embodied AI. We identify key obstacles and possibilities such as comprehensive generalization across rare cases, evaluation and safety checks, budget-limited implementation, regulatory compliance, ethical concerns, and environmental effects, while proposing research plans across theoretical assurances, trust metrics, transport integration, and socio-technical influence. By unifying these threads, the survey provides a forward-looking reference for researchers, engineers, and policymakers navigating the convergence of generative AI and advanced autonomous mobility. An actively maintained repository of cited works is available atthis https URL.
  </details>
