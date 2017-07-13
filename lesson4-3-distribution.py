#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(color_codes=True)  # 设置简写颜色码

# x = np.random.normal(size=100)  # 从正态分布数据中随机取出 100 个样本
# sns.distplot(x, kde=True)  # kde=True是表示显示正态分布线,是否绘制高斯核密度估计
# sns.distplot(x, kde=False, bins=20, rug=True)   # bins 柱形图的宽度?
# sns.kdeplot(x)    # 画正态密度函数
# sns.kdeplot(x, label='bw:scott')
# sns.kdeplot(x, bw=.2, label="bw:0.2")
# sns.kdeplot(x, bw=2, label="bw:2")
# plt.legend(loc="best")

# x1 = np.random.gamma(6, size=200)
# sns.distplot(x)
# sns.distplot(x, kde=True, fit=stats.gamma)  # fit 为模型名字
# sns.distplot(x, kde=True, fit=stats.norm)

# 联合分布
# mean, cov = [0, 1], [(1, 0.5), (0.5, 1)]
# data = np.random.multivariate_normal(mean, cov, 200)
# df = pd.DataFrame(data, columns=["x", "y"])
# sns.jointplot(x="x", y="y", data=df, kind="scatter")
# sns.jointplot(x="x", y="y", data=df, kind="kde")

# 核密度估计 等高线图效果
# f, ax = plt.subplots(figsize=(8, 8))  # 产生8*8的子图,以numpy数组的方式保存在ax中，而f仍然是整个图像对象，
# sns.kdeplot(df.x, df.y, ax=ax, shade=True)
# sns.rugplot(df.x, color="b", ax=ax)
# sns.rugplot(df.y, vertical=True, ax=ax, color="r")

# # 更梦幻的效果1
# cmap = sns.cubehelix_palette(as_cmap=True, dark=1, light=0)  # cmap: color map
# sns.kdeplot(df.x, df.y, cmap=cmap, n_levels=60, shade=True)  # n_level 决定密集度

# 更梦幻的效果2
# g = sns.jointplot(x="x", y="y", data=df, kind="kde", color="m")
# g.plot_joint(plt.scatter, c="w", s=30, linewidth=1, marker="+")
# g.ax_joint.collections[0].set_alpha(0)
# # 设置中间图片背景的透明度
# g.set_axis_labels("$X$", "$Y$")  # Latex

# 六角相图
# x, y = np.random.multivariate_normal(mean, cov, 1000).T  # 转置
# with sns.axes_style("ticks"):
#     sns.jointplot(x=x, y=y, kind="hex")

iris = sns.load_dataset("iris")
print iris
sns.pairplot(iris)
sns.pairplot(iris, hue='species', size=2.5)
# g = sns.PairGrid(iris)  # 得到一个实例
# g.map_diag(sns.kdeplot)  # 对角线为 KDE 图
# g.map_offdiag(sns.kdeplot, cmap="Blues_d", n_levels=20)
# 非对角线为两变量间的 KDE 图
# plt.show()
