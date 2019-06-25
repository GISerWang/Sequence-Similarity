# -*- coding: utf-8 -*-
import numpy as np
from scipy.spatial.distance import cdist
import time
# 计算单向的Hausdorff距离
# max（a∈ptSetA）min（b∈ptSetB）‖a-b‖
def OneWayHausdorffDistance(ptSetA, ptSetB):
    # 计算任意向量之间的距离，假设ptSetA有n个向量，ptSetB有m个向量
    # 得到矩阵C（n行m列）Cij代表A中都第i个向量到B中第j向量都距离
    dist = cdist(ptSetA, ptSetB, metric='euclidean')
    # np.min(dist,axis=1):计算每一行的的最小值
    # 即：固定点集A的值，求点集A中到集合B的最小值
    return np.max(np.min(dist, axis=1))
# 计算双向的Hausdorff距离=====>H(ptSetA,ptSetB)=max(h(ptSetA,ptSetB),h(ptSetB,ptSetA))
# ptSetA：输入的第一个点集
# ptSetB：输入的第二个点集
# Hausdorff距离度量了两个点集间的最大不匹配程度
def HausdorffDistance(ptSetA, ptSetB):
    # 计算双向的Hausdorff距离距离
    res = np.array([
        OneWayHausdorffDistance(ptSetA, ptSetB),
        OneWayHausdorffDistance(ptSetB, ptSetA)
    ])
    return np.max(res)
data = np.loadtxt("./data/traj.csv",delimiter=",")
# 加载三条轨迹
traj1, traj2, traj3 = data[:8], data[8:15], data[15:]
starttime = time.clock()
print("轨迹1与轨迹2的Hausdorff距离为：%s"%(HausdorffDistance(traj1,traj2)))
print("轨迹2与轨迹3的Hausdorff距离为：%s"%(HausdorffDistance(traj2,traj3)))
print("轨迹1与轨迹3的Hausdorff距离为：%s"%(HausdorffDistance(traj1,traj3)))
endtime = time.clock()
print("运行时间：%s秒"%(endtime - starttime,))