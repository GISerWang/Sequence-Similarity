# -*- coding: utf-8 -*-
import numpy as np
from scipy.spatial.distance import cdist
import time
# 使用循环的方式求解两个序列点对的相似度（距离）
# 即costMatrix右下角的最后一个值为Frechet距离
def FrechetDistance(ptSetA, ptSetB):
    # 获得点集ptSetA中点的个数n
    n = ptSetA.shape[0]
    # 获得点集ptSetB中点的个数m
    m = ptSetB.shape[0]
    # 计算任意两个点的距离矩阵
    # disMat[i][j]对应ptSetA的第i个点到ptSetB中第j点的距离
    disMat = cdist(ptSetA, ptSetB, metric='euclidean')
    # 初始化消耗矩阵
    costMatrix = np.full((n, m), -1.0)
    # 逐行给消耗矩阵赋值
    # 首先给第一行赋值
    # 然后依次给2,3,4,...,m行赋值
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                # 给左上角赋值
                costMatrix[0][0] = disMat[0][0]
            if i == 0 and j > 0:
                # 给第一行赋值
                costMatrix[0][j] = max(costMatrix[0][j-1], disMat[0][j])
            if i > 0 and j == 0:
                # 给第一列赋值
                costMatrix[i][0] = max(costMatrix[i-1][0], disMat[i][0])
            if i > 0 and j > 0:
                # 给其他赋值
                costMatrix[i][j] = max(min(costMatrix[i-1][j],
                                           costMatrix[i-1][j-1],
                                           costMatrix[i][j-1]), disMat[i][j])
    return costMatrix[n-1][m-1]
data = np.loadtxt("./data/traj.csv",delimiter=",")
# 加载三条轨迹
traj1, traj2, traj3 = data[:8], data[8:15], data[15:]
starttime = time.clock()
print("轨迹1与轨迹2的Frechet距离为：%s"%(FrechetDistance(traj2,traj1)))
print("轨迹2与轨迹3的Frechet距离为：%s"%(FrechetDistance(traj2,traj3)))
print("轨迹1与轨迹3的Frechet距离为：%s"%(FrechetDistance(traj1,traj3)))
endtime = time.clock()
print("运行时间：%s秒"%(endtime - starttime,))