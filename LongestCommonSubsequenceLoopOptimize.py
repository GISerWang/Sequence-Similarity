# -*- coding: utf-8 -*-
import time
import numpy as np
from scipy.spatial.distance import cdist
def extractCommonSequence(lcsMat,isEqual):
    # 获得seqA与seqB的长度
    n,m = isEqual.shape
    # 公共序列在序列A中的索引
    subSeqAIndex=[]
    # 公共序列在序列B中的索引
    subSeqBIndex=[]
    i = n-1
    j = m-1
    # 回溯寻找
    while i != 0 and j != 0:
        if isEqual[i][j] == 1:
            # 如果这两个值都相等，那么回溯到isEqual[i-1][i-1]
            subSeqAIndex.insert(0, i)
            subSeqBIndex.insert(0, j)
            i = i-1
            j = j-1
        elif lcsMat[i+1][j] >= lcsMat[i][j+1]:
            # 进入到这里，说明不相等，且矩阵矩阵左边大于上面
            # 即lcsMat[i+1][j+1]是由lcsMat[i+1][j]得到，向左回退，因此j回退
            j = j - 1
        else:
            # 进入到这里，说明不相等，且矩阵上面大于左边
            # 即lcsMat[i+1][j+1]是由lcsMat[i][j+1]得到，向上回退，因此j回退
            i = i - 1
    return [subSeqAIndex, subSeqBIndex]
# 循环求解最长公共子序列
def LongestCommonSubsequence(seqA,seqB,tol):
    # 获取序列A的长度
    n = seqA.shape[0]
    # 获取序列B的长度
    m = seqB.shape[0]
    # 生成0矩阵，序列矩阵lcsMat[i][j]
    # lcsMat[i][j]：表示seqA前i个序列与seqB前j个序列的最长公共子序列长度
    # lcsMat[0][j]，与lcsMat[i][0]都为0，即，当一个序列为0时，没有公共子序列
    lcsMat = np.zeros((n+1, m+1), dtype=np.int)
    # 计算任意两个点的距离
    disMat = cdist(seqA, seqB, metric='euclidean')
    # 用于判断，元素是否相等
    # isEqual[i][j]==1表示seqA[i]==seqB[j]
    # isEqual[i][j]==0表示seqA[i]!=seqB[j]
    isEqual = np.where(disMat < tol, 1, 0)
    # 循环为lcsMat赋值
    # lcsMat[n][m]为最长公共子序列的长度
    for i in range(n):
        # 为lcsMat一行一行的赋值（注意：要思考为什么可以一行一行的赋值）
        # 原因：lcsMat[i][j]的值仅与三个位置有关，分别为：lcsMat[i-1][j-1]、lcsMat[i-1][j]、lcsMat[i][j-1]
        # 因此每一次迭代，所有的三个元素肯定都已经有值了
        for j in range(m):
            # seqA[i]seqB[j]的公共子序列长度，记录在lcsMat[i + 1][j + 1]
            # 因为有了0序列，矩阵多了一行一列（均为0）
            if isEqual[i][j] == 1:
                # 如果最后一个元素相等，那么就是lcsMat[i][j]+1，即当前元素等于左上角元素加1
                lcsMat[i + 1][j + 1] = lcsMat[i][j] + 1
            else:
                # 如果最后一个元素不相等，即当前元素等于左边元素或者上面元素中最大的那个
                lcsMat[i + 1][j + 1] = max(lcsMat[i + 1][j],lcsMat[i][j + 1])
    # 用于求解公共子序列相应的位置
    sequence = extractCommonSequence(lcsMat,isEqual)
    # 用于计算相似度
    similarity = 1-lcsMat[n][m]*1.0/min(n,m)
    return lcsMat[n][m],similarity,sequence
data = np.loadtxt("./data/traj.csv",delimiter=",")
# 加载三条轨迹
traj1, traj2, traj3 = data[:8], data[8:15], data[15:]
starttime = time.clock()
l1, similarity1, sequence1 = LongestCommonSubsequence(traj1, traj2, 5)
l2, similarity2, sequence2 = LongestCommonSubsequence(traj2, traj3, 5)
l3, similarity3, sequence3 = LongestCommonSubsequence(traj1, traj3, 5)
endtime = time.clock()
print("轨迹1与轨迹2的LCSS距离为：%s\n轨迹1与轨迹2公共子序列的长度为：%s"%(similarity1,l1))
print("轨迹2与轨迹3的LCSS距离为：%s\n轨迹1与轨迹2公共子序列的长度为：%s"%(similarity2,l2))
print("轨迹1与轨迹3的LCSS距离为：%s\n轨迹1与轨迹2公共子序列的长度为：%s"%(similarity3,l3))
print("轨迹1与轨迹3公共轨迹点的索引如下：\n     traj1:%s\n     traj3:%s"%(sequence3[0],sequence3[1]))
print("运行时间：%s秒"%(endtime - starttime,))