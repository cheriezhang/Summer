#!/usr/bin/python
# -*- coding:UTF-8 -*-


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", color_codes=True)
titanic = sns.load_dataset("titanic")  # titanic 号
tips = sns.load_dataset("tips")  # 小费
iris = sns.load_dataset("iris")  # 茑尾花

# 观测点直接展示
# 1、条带图
sns.stripplot(x="day", y="total_bill", data=tips)
sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)  # 最好使用抖动
# 2、蜂群图
sns.swarmplot(x="day", y="total_bill", data=tips)
sns.swarmplot(x="day", y="total_bill", hue='sex', data=tips)  # hue代表子集

# 近似分布展示
# 1、箱图
sns.boxplot(x="day", y="total_bill", hue="time", data=tips)
# 2、提琴图
sns.violinplot(x="total_bill", y="day", hue="time", data=tips)
sns.violinplot(x="total_bill", y="day", hue="time", data=tips, scale="count",scale_hue=False)  # scale决定小提琴宽度的因素 count area width
sns.violinplot(x="day", y="total_bill", hue="sex", data=tips, split=True, inner="box")  # inner里面显示的样式 box stick quartiles

# 均值和置信区间展示
# 1、统计柱状图
sns.barplot(x="sex",y="survived",hue="class",data=titanic)
# 2、灰度图
sns.countplot(x="deck",data=titanic,palette="Greens_d")
# 3、点图
sns.pointplot(x="sex", y="survived", hue="class", data=titanic)
sns.pointplot(x="class", y="survived", hue="sex", data=titanic,
              palette={"male": "g", "female": "m"},markers=["^", "o"], linestyles=["-", "--"])
#分类子图
sns.factorplot(x="day",y="total_bill",hue="smoker",col="time",data=tips,kind="swarm")
g = sns.PairGrid(tips, x_vars=["smoker", "time", "sex"], y_vars=["total_bill", "tip"], aspect=.75, size=3.5)
g.map(sns.violinplot, palette="pastel")
plt.show()
