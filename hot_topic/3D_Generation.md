# 🔍 3D_Generation Papers · 2025-03-31

[![Total Papers](https://img.shields.io/badge/Papers-5-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Video Generation` `Scene Generation` `Content Generation`  
**Filter**: `2D`

---

## 📚 Paper List

- **[Consistent Subject Generation via Contrastive Instantiated Concepts](http://arxiv.org/abs/2503.24387v1)**  `arXiv:2503.24387`  `cs.CV`  
  _Lee Hsin-Ying, Kelvin C. K. Chan, Ming-Hsuan Yang_
  <details open><summary>Abstract</summary>
  While text-to-image generative models can synthesize diverse and faithfulcontents, subject variation across multiple creations limits the application inlong content generation. Existing approaches require time-consuming tuning,references for all subjects, or access to other creations. We introduceContrastive Concept Instantiation (CoCoIns) to effectively synthesizeconsistent subjects across multiple independent creations. The frameworkconsists of a generative model and a mapping network, which transforms inputlatent codes into pseudo-words associated with certain instances of concepts.Users can generate consistent subjects with the same latent codes. To constructsuch associations, we propose a contrastive learning approach that trains thenetwork to differentiate the combination of prompts and latent codes. Extensiveevaluations of human faces with a single subject show that CoCoIns performscomparably to existing methods while maintaining higher flexibility. We alsodemonstrate the potential of extending CoCoIns to multiple subjects and otherobject categories.
  </details>

- **[Any2Caption:Interpreting Any Condition to Caption for Controllable Video Generation](http://arxiv.org/abs/2503.24379v1)**  `arXiv:2503.24379`  `cs.CV` `cs.AI`  
  _Shengqiong Wu, Weicai Ye, Jiahao Wang, Quande Liu, Xintao Wang, Pengfei Wan, et al._
  <details open><summary>Abstract</summary>
  To address the bottleneck of accurate user intent interpretation within thecurrent video generation community, we present Any2Caption, a novel frameworkfor controllable video generation under any condition. The key idea is todecouple various condition interpretation steps from the video synthesis step.By leveraging modern multimodal large language models (MLLMs), Any2Captioninterprets diverse inputs--text, images, videos, and specialized cues such asregion, motion, and camera poses--into dense, structured captions that offerbackbone video generators with better guidance. We also introduce Any2CapIns, alarge-scale dataset with 337K instances and 407K conditions forany-condition-to-caption instruction tuning. Comprehensive evaluationsdemonstrate significant improvements of our system in controllability and videoquality across various aspects of existing video generation models. ProjectPage: https://sqwu.top/Any2Cap/
  </details>

- **[Level the Level: Balancing Game Levels for Asymmetric Player Archetypes With Reinforcement Learning](http://arxiv.org/abs/2503.24099v1)**  `arXiv:2503.24099`  `cs.LG`  
  _Florian Rupp, Kai Eckert_
  <details open><summary>Abstract</summary>
  Balancing games, especially those with asymmetric multiplayer content,requires significant manual effort and extensive human playtesting duringdevelopment. For this reason, this work focuses on generating balanced levelstailored to asymmetric player archetypes, where the disparity in abilities isbalanced entirely through the level design. For instance, while one archetypemay have an advantage over another, both should have an equal chance ofwinning. We therefore conceptualize game balancing as a procedural contentgeneration problem and build on and extend a recently introduced method thatuses reinforcement learning to balance tile-based game levels. We evaluate themethod on four different player archetypes and demonstrate its ability tobalance a larger proportion of levels compared to two baseline approaches.Furthermore, our results indicate that as the disparity between playerarchetypes increases, the required number of training steps grows, while themodel's accuracy in achieving balance decreases.
  </details>

- **[JointTuner: Appearance-Motion Adaptive Joint Training for Customized Video Generation](http://arxiv.org/abs/2503.23951v1)**  `arXiv:2503.23951`  `cs.CV`  
  _Fangda Chen, Shanshan Zhao, Chuanfu Xu, Long Lan_
  <details open><summary>Abstract</summary>
  Recent text-to-video advancements have enabled coherent video synthesis fromprompts and expanded to fine-grained control over appearance and motion.However, existing methods either suffer from concept interference due tofeature domain mismatch caused by naive decoupled optimizations or exhibitappearance contamination induced by spatial feature leakage resulting from theentanglement of motion and appearance in reference video reconstructions. Inthis paper, we propose JointTuner, a novel adaptive joint training framework,to alleviate these issues. Specifically, we develop Adaptive LoRA, whichincorporates a context-aware gating mechanism, and integrate the gated LoRAcomponents into the spatial and temporal Transformers within the diffusionmodel. These components enable simultaneous optimization of appearance andmotion, eliminating concept interference. In addition, we introduce theAppearance-independent Temporal Loss, which decouples motion patterns fromintrinsic appearance in reference video reconstructions through anappearance-agnostic noise prediction task. The key innovation lies in addingframe-wise offset noise to the ground-truth Gaussian noise, perturbing itsdistribution, thereby disrupting spatial attributes associated with frameswhile preserving temporal coherence. Furthermore, we construct a benchmarkcomprising 90 appearance-motion customized combinations and 10 multi-typeautomatic metrics across four dimensions, facilitating a more comprehensiveevaluation for this customization task. Extensive experiments demonstrate thesuperior performance of our method compared to current advanced approaches.
  </details>

- **[On-device Sora: Enabling Training-Free Diffusion-based Text-to-Video Generation for Mobile Devices](http://arxiv.org/abs/2502.04363v2)**  `arXiv:2502.04363`  `cs.CV`  
  _Bosung Kim, Kyuhwan Lee, Isu Jeong, Jungmin Cheon, Yeojin Lee, Seulki Lee_
  <details open><summary>Abstract</summary>
  We present On-device Sora, the first model training-free solution fordiffusion-based on-device text-to-video generation that operates efficiently onsmartphone-grade devices. To address the challenges of diffusion-basedtext-to-video generation on computation- and memory-limited mobile devices, theproposed On-device Sora applies three novel techniques to pre-trained videogenerative models. First, Linear Proportional Leap (LPL) reduces the excessivedenoising steps required in video diffusion through an efficient leap-basedapproach. Second, Temporal Dimension Token Merging (TDTM) minimizes intensivetoken-processing computation in attention layers by merging consecutive tokensalong the temporal dimension. Third, Concurrent Inference with Dynamic Loading(CI-DL) dynamically partitions large models into smaller blocks and loads theminto memory for concurrent model inference, effectively addressing thechallenges of limited device memory. We implement On-device Sora on the iPhone15 Pro, and the experimental evaluations show that it is capable of generatinghigh-quality videos on the device, comparable to those produced by high-endGPUs. These results show that On-device Sora enables efficient and high-qualityvideo generation on resource-constrained mobile devices. We envision theproposed On-device Sora as a significant first step toward democratizingstate-of-the-art generative technologies, enabling video generation oncommodity mobile and embedded devices without resource-intensive re-trainingfor model optimization (compression). The code implementation is available at aGitHub repository(https://github.com/eai-lab/On-device-Sora).
  </details>
