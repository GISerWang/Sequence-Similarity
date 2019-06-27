# Sequence-Similarity
## 1 介绍
### 1.1在本实例中，如果想将代码直接运行需注意以下几点：
* Python版本3.X（本人使用的是Python 3.6）
* numpy版本：1.16.0
* scipy版本：0.19.1
### 1.2 项目说明

* **data**：存放测试数据的文件夹
    * **traj**:存放三条轨迹数据（1-8行是第一条轨迹，9-15行是第二条轨迹，16-21是第三条轨迹）
* **ShowTrajData**：使用matplotlib直观的显示三条轨迹的形状
* **DynamicTimeWarpingRecursive**：动态时间归整（Dynamic Time Warping，DTW）算法的递归实现
* **DynamicTimeWarpingLoop**：动态时间归整（Dynamic Time Warping，DTW）算法的循环实现
* **FréchetDistanceRecursive**：弗雷歇离散距离（Fréchet Distance）算法的递归实现
* **FréchetDistanceLoop**：弗雷歇离散距离（Fréchet Distance）算法的循环实现
* **HausdorffDistance**：豪斯多夫距离（Hausdorff Distance）算法的实现
* **LongestCommonSubsequenceRecursive**：最长公共子序列（Longest Common Subsequence）算法的递归实现
* **LongestCommonSubsequenceLoop**：最长公共子序列（Longest Common Subsequence）算法的循环实现
* **LongestCommonSubsequenceLoopOptimize**：最长公共子序列（Longest Common Subsequence）算法的循环实现,代码进行了优化，速度为**LongestCommonSubsequenceLoop**的**三分之一**
* **EditDistance**：编辑距离（EditDistance）（未完成）
## 2 序列相似度算法原理