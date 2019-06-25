# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
data = np.loadtxt("./data/traj.csv",delimiter=",")
# 加载第一条轨迹
traj1 = data[:8]
# 加载第二条轨迹
traj2 = data[8:15]
# 加载第三条轨迹
traj3 = data[15:]
fig = plt.figure()
# 绘制第一条轨迹
plt.plot(traj1[:,0],traj1[:,1],label='traj1')
# 绘制第二条轨迹
plt.plot(traj2[:,0],traj2[:,1],label='traj2')
# 绘制第三条轨迹
plt.plot(traj3[:,0],traj3[:,1],label='traj3')
# 显示图例
plt.legend(loc='upper right')
plt.show()