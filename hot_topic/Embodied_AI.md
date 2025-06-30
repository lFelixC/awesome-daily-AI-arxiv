# 🔍 Embodied_AI Papers · 2025-06-29

[![Total Papers](https://img.shields.io/badge/Papers-2-2688EB)]()
[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()

---

## 📌 Filter by Category
**Keywords**: `VLA` `Vision-Language-Action`  
**Filter**: `None`

---

## 📚 Paper List

- **[AeroLite-MDNet: Lightweight Multi-task Deviation Detection Network for UAV Landing](https://arxiv.org/abs/2506.21635)**  `arXiv:2506.21635`  `cs.RO` `cs.AI` `cs.CV`  
  _Haiping Yang, Huaxing Liu, Wei Wu, Zuohui Chen, Ning Wu_
  <details open><summary>Abstract</summary>
  Unmanned aerial vehicles (UAVs) are increasingly employed in diverse applications such as land surveying, material transport, and environmental monitoring. Following missions like data collection or inspection, UAVs must land safely at docking stations for storage or recharging, which is an essential requirement for ensuring operational continuity. However, accurate landing remains challenging due to factors like GPS signal interference. To address this issue, we propose a deviation warning system for UAV landings, powered by a novel vision-based model called AeroLite-MDNet. This model integrates a multiscale fusion module for robust cross-scale object detection and incorporates a segmentation branch for efficient orientation estimation. We introduce a new evaluation metric, Average Warning Delay (AWD), to quantify the system's sensitivity to landing deviations. Furthermore, we contribute a new dataset, UAVLandData, which captures real-world landing deviation scenarios to support training and evaluation. Experimental results show that our system achieves an AWD of 0.7 seconds with a deviation detection accuracy of 98.6\%, demonstrating its effectiveness in enhancing UAV landing reliability. Code will be available atthis https URL
  </details>

- **[4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration](https://arxiv.org/abs/2506.22242)**  `arXiv:2506.22242`  `cs.CV`  
  _Jiahui Zhang, Yurui Chen, Yueming Xu, Ze Huang, Yanpeng Zhou, Yu-Jie Yuan, et al._
  <details open><summary>Abstract</summary>
  Leveraging diverse robotic data for pretraining remains a critical challenge. Existing methods typically model the dataset's action distribution using simple observations as inputs. However, these inputs are often incomplete, resulting in a dispersed conditional action distribution-an issue we refer to as coordinate system chaos and state chaos. This inconsistency significantly hampers pretraining efficiency. To address this, we propose 4D-VLA, a novel approach that effectively integrates 4D information into the input to mitigate these sources of chaos. Our model introduces depth and temporal information into visual features with sequential RGB-D inputs, aligning the coordinate systems of the robot and the scene. This alignment endows the model with strong spatiotemporal reasoning capabilities while minimizing training overhead. Additionally, we introduce memory bank sampling, a frame sampling strategy designed to extract informative frames from historical images, further improving effectiveness and efficiency. Experimental results demonstrate that our pretraining method and architectural components substantially enhance model performance. In both simulated and real-world experiments, our model achieves a significant increase in success rate over OpenVLA. To further assess spatial perception and generalization to novel views, we introduce MV-Bench, a multi-view simulation benchmark. Our model consistently outperforms existing methods, demonstrating stronger spatial understanding and adaptability.
  </details>
