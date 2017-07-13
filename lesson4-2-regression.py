#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# tips示例
tips = sns.load_dataset("tips")
# print tips
# sns.lmplot(x="total_bill", y="tip", data=tips, size=10)
# sns.lmplot(x="size", y="tip", data=tips, size=10)
# sns.lmplot(x="size", y="tip", data=tips, size=10, x_jitter=0.2)  # 左右抖动
# sns.lmplot(x="size", y="tip", data=tips, x_estimator=np.mean)
# tips["big_tip"] = (tips.tip / tips.total_bill) > .15  # 小费与帐单的比例超过 15%的消费
# sns.lmplot(x="total_bill", y="big_tip", data=tips, y_jitter=0.2)  # y轴抖动
# sns.lmplot(x="total_bill", y="big_tip", data=tips, logistic=True, y_jitter=.05, ci=None)  # 逻辑拟合
# sns.lmplot(x="total_bill",y="tip",hue="smoker",data=tips)   #hue 小窗
# sns.lmplot(x="total_bill",y="tip",hue="smoker",data=tips,markers=["o","x"])
# sns.lmplot(x="total_bill", y="tip", hue="sex", data=tips, markers=["o", "x"])
# sns.lmplot(x="total_bill", y="tip", hue="smoker", col="time", data=tips)    # 生成两幅图,并列在一行,列区分为时间
# sns.lmplot(x="total_bill", y="tip", hue="smoker", col="time", row="sex", data=tips) # 生成四幅图,列区分为时间,行区分为性别
# sns.lmplot(x="total_bill", y="tip", col="day", data=tips, col_wrap=2, size=7)  # 控制每行多少个图
# sns.lmplot(x="total_bill", y="tip", col="day", data=tips, aspect=3)  # aspect:控制切面的缩放比例

'''
# anscombe示例
anscombe = sns.load_dataset("anscombe")
# print anscombe
# 只取dataset为"I"的数据,可简单查询
# sns.lmplot(x="x", y="y", data=anscombe.query("dataset=='I'"), ci=None, scatter_kws={"s": 100})  # s:100是点的大小
# sns.lmplot(x="x", y="y", data=anscombe.query("dataset=='II'"), ci=None, order=2, scatter_kws={"s": 80})  # order是几阶的意思
# sns.lmplot(x="x", y="y", data=anscombe.query("dataset=='III'"), robust=False, ci=None, scatter_kws={"s": 80})  # robust异常值不容错
# sns.lmplot(x="x", y="y", data=anscombe.query("dataset=='III'"), ci=None, robust=True, scatter_kws={"s": 80})    # robust异常值容错
#sns.residplot(x="x", y="y", data=anscombe.query("dataset=='I'"), scatter_kws={"s": 80})  # 拟合效果好
#sns.residplot(x="x", y="y", data=anscombe.query("dataset=='II'"), scatter_kws={"s": 80})    # 拟合效果差
'''

plt.show()
