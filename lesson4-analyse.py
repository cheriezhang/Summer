#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

'''
# tips示例
tips = sns.load_dataset("tips")
print tips
sns.lmplot(x="total_bill", y="tip", data=tips, size=10)
sns.lmplot(x="size", y="tip", data=tips, size=10)
sns.lmplot(x="size", y="tip", data=tips, size=10, x_jitter=0.2)  # 左右抖动
sns.lmplot(x="size", y="tip", data=tips, x_estimator=np.mean)
'''

# anscombe示例
anscombe = sns.load_dataset("anscombe")
# print anscombe
# 只取dataset为"I"的数据,可简单查询
sns.lmplot(x="x", y="y", data=anscombe.query("dataset=='I'"), ci=None, scatter_kws={"s": 100})  # s:100是点的大小
sns.lmplot(x="x", y="y", data=anscombe.query("dataset=='II'"), ci=None, order=2, scatter_kws={"s": 80})  # order是几阶的意思
sns.lmplot(x="x", y="y", data=anscombe.query("dataset=='III'"), robust=False, ci=None,
           scatter_kws={"s": 80})  # robust异常值不容错
# sns.lmplot(x="x", y="y", data=anscombe.query("dataset=='III'"), robust=True, ci=None, scatter_kws={"s": 80})   # robust异常值容错

plt.show()
