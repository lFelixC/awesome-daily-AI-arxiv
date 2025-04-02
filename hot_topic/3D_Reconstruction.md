# 🔍 3D_Reconstruction Papers · 2025-03-31

[![Total Papers](https://img.shields.io/badge/Papers-3-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `Reconstruction` `Nerf` `Gaussian`  
**Filter**: `2D`

---

## 📚 Paper List

- **[Easi3R: Estimating Disentangled Motion from DUSt3R Without Training](http://arxiv.org/abs/2503.24391v1)**  `arXiv:2503.24391`  `cs.CV`  
  _Xingyu Chen, Yue Chen, Yuliang Xiu, Andreas Geiger, Anpei Chen_
  <details open><summary>Abstract</summary>
  Recent advances in DUSt3R have enabled robust estimation of dense pointclouds and camera parameters of static scenes, leveraging Transformer networkarchitectures and direct supervision on large-scale 3D datasets. In contrast,the limited scale and diversity of available 4D datasets present a majorbottleneck for training a highly generalizable 4D model. This constraint hasdriven conventional 4D methods to fine-tune 3D models on scalable dynamic videodata with additional geometric priors such as optical flow and depths. In thiswork, we take an opposite path and introduce Easi3R, a simple yet efficienttraining-free method for 4D reconstruction. Our approach applies attentionadaptation during inference, eliminating the need for from-scratch pre-trainingor network fine-tuning. We find that the attention layers in DUSt3R inherentlyencode rich information about camera and object motion. By carefullydisentangling these attention maps, we achieve accurate dynamic regionsegmentation, camera pose estimation, and 4D dense point map reconstruction.Extensive experiments on real-world dynamic videos demonstrate that ourlightweight attention adaptation significantly outperforms previousstate-of-the-art methods that are trained or finetuned on extensive dynamicdatasets. Our code is publicly available for research purpose athttps://easi3r.github.io/
  </details>

- **[Free360: Layered Gaussian Splatting for Unbounded 360-Degree View Synthesis from Extremely Sparse and Unposed Views](http://arxiv.org/abs/2503.24382v1)**  `arXiv:2503.24382`  `cs.CV`  
  _Chong Bao, Xiyu Zhang, Zehao Yu, Jiale Shi, Guofeng Zhang, Songyou Peng, et al._
  <details open><summary>Abstract</summary>
  Neural rendering has demonstrated remarkable success in high-quality 3Dneural reconstruction and novel view synthesis with dense input views andaccurate poses. However, applying it to extremely sparse, unposed views inunbounded 360{\deg} scenes remains a challenging problem. In this paper, wepropose a novel neural rendering framework to accomplish the unposed andextremely sparse-view 3D reconstruction in unbounded 360{\deg} scenes. Toresolve the spatial ambiguity inherent in unbounded scenes with sparse inputviews, we propose a layered Gaussian-based representation to effectively modelthe scene with distinct spatial layers. By employing a dense stereoreconstruction model to recover coarse geometry, we introduce a layer-specificbootstrap optimization to refine the noise and fill occluded regions in thereconstruction. Furthermore, we propose an iterative fusion of reconstructionand generation alongside an uncertainty-aware training approach to facilitatemutual conditioning and enhancement between these two processes. Comprehensiveexperiments show that our approach outperforms existing state-of-the-artmethods in terms of rendering quality and surface reconstruction accuracy.Project page: https://zju3dv.github.io/free360/
  </details>

- **[ERUPT: Efficient Rendering with Unposed Patch Transformer](http://arxiv.org/abs/2503.24374v1)**  `arXiv:2503.24374`  `cs.CV`  
  _Maxim V. Shugaev, Vincent Chen, Maxim Karrenbach, Kyle Ashley, Bridget Kennedy, Naresh P. Cuntoor_
  <details open><summary>Abstract</summary>
  This work addresses the problem of novel view synthesis in diverse scenesfrom small collections of RGB images. We propose ERUPT (Efficient Renderingwith Unposed Patch Transformer) a state-of-the-art scene reconstruction modelcapable of efficient scene rendering using unposed imagery. We introducepatch-based querying, in contrast to existing pixel-based queries, to reducethe compute required to render a target view. This makes our model highlyefficient both during training and at inference, capable of rendering at 600fps on commercial hardware. Notably, our model is designed to use a learnedlatent camera pose which allows for training using unposed targets in datasetswith sparse or inaccurate ground truth camera pose. We show that our approachcan generalize on large real-world data and introduce a new benchmark dataset(MSVS-1M) for latent view synthesis using street-view imagery collected fromMapillary. In contrast to NeRF and Gaussian Splatting, which require denseimagery and precise metadata, ERUPT can render novel views of arbitrary sceneswith as few as five unposed input images. ERUPT achieves better rendered imagequality than current state-of-the-art methods for unposed image synthesistasks, reduces labeled data requirements by ~95\% and decreases computationalrequirements by an order of magnitude, providing efficient novel view synthesisfor diverse real-world scenes.
  </details>
