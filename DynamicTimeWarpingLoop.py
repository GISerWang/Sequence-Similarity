# -*- coding: utf-8 -*-
import numpy as np
from scipy.spatial.distance import cdist
import time
# 提取路径对齐
def extractPath(costMatrix,i,j):
    # 初始化路径
    path = []
    # 从右下角循环，寻找对齐点
    while i != 0 and j != 0:
        # 首先加入右下角点
        path.insert(0, (i, j))
        # 循环的元素，三个坐标
        idxArr = [(i-1,j),(i-1,j-1),(i,j-1)]
        # 寻找到最小的那个值
        minArg = np.argmin(np.array([
            costMatrix[i - 1][j],
            costMatrix[i - 1][j - 1],
            costMatrix[i][j - 1]]))
        # 对应的消耗矩阵的元素
        minIndex = idxArr[minArg]
        # 重新迭代
        i = minIndex[0]
        j = minIndex[1]
    # 寻找靠边的点
    while i != 0:
        path.insert(0, (i, 0))
        i = i-1
    # 寻找靠边的点
    while j != 0:
        path.insert(0, (0, j))
        j = j - 1
    # 加入0，0
    path.insert(0, (0, 0))
    return path
# 使用循环的方式求解costMatrix的i,j的数值
# 即costMatrix右下角的最后一个值为dtw距离
# 返回值：dtw值+路径
def DynamicTimeWarping(ptSetA, ptSetB):
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
                costMatrix[0][j] = costMatrix[0][j-1]+disMat[0][j]
            if i > 0 and j == 0:
                # 给第一列赋值
                costMatrix[i][0] = costMatrix[i-1][0]+disMat[i][0]
            if i > 0 and j > 0:
                # 给其他赋值
                costMatrix[i][j] = min(costMatrix[i-1][j],
                                           costMatrix[i-1][j-1],
                                           costMatrix[i][j-1]) + disMat[i][j]
    # 提取路径
    path = extractPath(costMatrix, n - 1, m - 1)
    return costMatrix[n-1][m-1],path
data = np.loadtxt("./data/traj.csv",delimiter=",")
# 加载三条轨迹
traj1, traj2, traj3 = data[:8], data[8:15], data[15:]
starttime = time.clock()
print("轨迹1与轨迹2的DTW距离为：%s"%(DynamicTimeWarping(traj1,traj2)[0]))
print("轨迹1与轨迹2的path路径为：%s"%(DynamicTimeWarping(traj1,traj2)[1]))
print("轨迹2与轨迹3的DTW距离为：%s"%(DynamicTimeWarping(traj2,traj3)[0]))
print("轨迹2与轨迹3的path路径为：%s"%(DynamicTimeWarping(traj2,traj3)[1]))
print("轨迹1与轨迹3的DTW距离为：%s"%(DynamicTimeWarping(traj1,traj3)[0]))
print("轨迹1与轨迹3的path路径为：%s"%(DynamicTimeWarping(traj1,traj3)[1]))
endtime = time.clock()
print("运行时间：%s秒"%(endtime - starttime,))