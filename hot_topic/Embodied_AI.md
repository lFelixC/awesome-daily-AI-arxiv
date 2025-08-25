# 🔍 Embodied_AI Papers · 2025-08-24

[![Total Papers](https://img.shields.io/badge/Papers-2-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[OmniVTLA: Vision-Tactile-Language-Action Model with Semantic-Aligned Tactile Sensing](https://arxiv.org/abs/2508.08706)**  `arXiv:2508.08706`  `cs.RO`  
  _Zhengxue Cheng, Yiqian Zhang, Wenkang Zhang, Haoyu Li, Keyu Wang, Li Song, et al._
  <details open><summary>Abstract</summary>
  Recent vision-language-action (VLA) models build upon vision-language foundations, and have achieved promising results and exhibit the possibility of task generalization in robot manipulation. However, due to the heterogeneity of tactile sensors and the difficulty of acquiring tactile data, current VLA models significantly overlook the importance of tactile perception and fail in contact-rich tasks. To address this issue, this paper proposes OmniVTLA, a novel architecture involving tactile sensing. Specifically, our contributions are threefold. First, our OmniVTLA features a dual-path tactile encoder framework. This framework enhances tactile perception across diverse vision-based and force-based tactile sensors by using a pretrained vision transformer (ViT) and a semantically-aligned tactile ViT (SA-ViT). Second, we introduce ObjTac, a comprehensive force-based tactile dataset capturing textual, visual, and tactile information for 56 objects across 10 categories. With 135K tri-modal samples, ObjTac supplements existing visuo-tactile datasets. Third, leveraging this dataset, we train a semantically-aligned tactile encoder to learn a unified tactile representation, serving as a better initialization for OmniVTLA. Real-world experiments demonstrate substantial improvements over state-of-the-art VLA baselines, achieving 96.9% success rates with grippers, (21.9% higher over baseline) and 100% success rates with dexterous hands (6.2% higher over baseline) in pick-and-place tasks. Besides, OmniVTLA significantly reduces task completion time and generates smoother trajectories through tactile sensing compared to existing VLA. Our ObjTac dataset can be found atthis https URL
  </details>

- **[Do What? Teaching Vision-Language-Action Models to Reject the Impossible](https://arxiv.org/abs/2508.16292)**  `arXiv:2508.16292`  `cs.AI` `cs.RO`  
  _Wen-Han Hsieh, Elvis Hsieh, Dantong Niu, Trevor Darrell, Roei Herzig, David M. Chan_
  <details open><summary>Abstract</summary>
  Recently, Vision-Language-Action (VLA) models have demonstrated strong performance on a range of robotic tasks. These models rely on multimodal inputs, with language instructions playing a crucial role -- not only in predicting actions, but also in robustly interpreting user intent, even when the requests are impossible to fulfill. In this work, we investigate how VLAs can recognize, interpret, and respond to false-premise instructions: natural language commands that reference objects or conditions absent from the environment. We propose Instruct-Verify-and-Act (IVA), a unified framework that (i) detects when an instruction cannot be executed due to a false premise, (ii) engages in language-based clarification or correction, and (iii) grounds plausible alternatives in perception and action. Towards this end, we construct a large-scale instruction tuning setup with structured language prompts and train a VLA model capable of handling both accurate and erroneous requests. Our approach leverages a contextually augmented, semi-synthetic dataset containing paired positive and false-premise instructions, enabling robust detection and natural language correction. Our experiments show that IVA improves false premise detection accuracy by 97.56% over baselines, while increasing successful responses in false-premise scenarios by 50.78%.
  </details>
