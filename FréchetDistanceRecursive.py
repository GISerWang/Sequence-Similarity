# -*- coding: utf-8 -*-
import numpy as np
from scipy.spatial.distance import cdist
# 使用递归的方式求解cstMatrix的i,j的数值
# 即cstMatrix右下角的最后一个值为Frechet距离
def _recursive(disMat,cstMatrix,i,j):
    # 如果cstMatrix[i][j]不等于-1，直接返回，不需要计算了（借助动态规划的思想）
    if cstMatrix[i][j] > -1:
        return cstMatrix[i][j]
    # 当i,j都等于0的时候，计算消耗矩阵的值
    if i == 0 and j == 0:
        cstMatrix[i][j] = disMat[0][0]
    # 计算第一列的值
    if i > 0 and j == 0:
        cstMatrix[i][j] = max(_recursive(disMat,cstMatrix, i - 1, 0), disMat[i][0])
    # 计算第一行的值
    if i == 0 and j > 0:
        cstMatrix[i][j] = max(_recursive(disMat,cstMatrix, 0, j - 1), disMat[0][j])
    # 计算其他值
    if i > 0 and j > 0:
        cstMatrix[i][j] = max(min(_recursive(disMat,cstMatrix, i - 1, j), _recursive(disMat,cstMatrix, i - 1, j - 1), _recursive(disMat,cstMatrix, i, j - 1)),
                              disMat[i][j])
    return cstMatrix[i][j]
def FrechetDistance(ptSetA, ptSetB):
    # 获得点集ptSetA中点的个数n
    n = ptSetA.shape[0]
    # 获得点集ptSetB中点的个数m
    m = ptSetB.shape[0]
    # 计算任意两个点的距离矩阵
    disMat = cdist(ptSetA, ptSetB, metric='euclidean')
    # 初始化消耗矩阵
    cstMatrix = np.full((n,m),-1.0)
    # 递归求解Frechet距离
    return _recursive(disMat,cstMatrix,n-1,m-1)
data = np.loadtxt("./data/traj.csv",delimiter=",")
# 加载三条轨迹
traj1, traj2, traj3 = data[:8], data[8:15], data[15:]
print("轨迹1与轨迹2的Frechet距离为：%s"%(FrechetDistance(traj1,traj2)))
print("轨迹2与轨迹3的Frechet距离为：%s"%(FrechetDistance(traj2,traj3)))
print("轨迹1与轨迹3的Frechet距离为：%s"%(FrechetDistance(traj1,traj3)))