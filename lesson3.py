#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 数据可视化
import pandas as pd
import numpy as np
import scipy as sp
import matplotlib
import random
from matplotlib import pyplot as plt
from scipy import stats

df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.normal(size=5),
                   'data2': np.random.normal(size=5)})
print "df"
print df
print "df['data1']"
print df['data1']
print "df['data1'].groupby(df['key1']).mean()"
# 按照key1的值分类,即为a,b分类,然后求a类的data1的均值和b类的data1的均值
print df['data1'].groupby(df['key1']).mean()

x = np.arange(0, 100)  # 生成0开始的整数序列100个
y = random.sample(x, 10)  # 对x采样,步幅10
print x
print y
y1 = [(x > 90) | (x < 10)]
print y1
y2 = np.arange(0, 50)
for i in np.arange(0, 50):
    if i >= 10 and i <= 30:
        y2[i] = 0
    else:
        y2[i] = i
print y2

from numpy import nan

data = pd.Series([1, nan, 2, nan, 3, nan])
print data
print "丢弃NaN数据"
print data.dropna()
print "填充NaN数据"
print data.fillna(0)
print data.fillna(data.mean())

# matplotlib操作
# matplotlib:包 pyplot:类 gcf():方法
# fig = matplotlib.pyplot.gcf()  #gcf = get current figure
# fig = plt.gcf() 等价于上面的语句
# fig.set_size_inches(10, 10)

# 展示图形:plt.show()
# 清空坐标(clear axis):plt.cla()
# 清空图(clear figure):plt.clf()
# 关闭图:plt.close()

# 正态分布
plt.figure(figsize=(10, 5))  # 初始化的时候设置大小
x = np.arange(-5, 5, 0.01)
y = stats.norm.pdf(x, 0, 1)  # 生成正态分布,0,1为均值和方差
plt.plot(x, y)
# plt.savefig("figure_nor.png")
plt.show()

# 修改图 首先获取图像
fig_nor = plt.gcf()
fig_nor.set_size_inches(5, 5)  # 有图之后修改大小
plt.plot(x, y)
# plt.savefig("figure_nor.png")
plt.show()

'''
# 直方图
x2 = np.random.normal(size=1000)
# 从正态分布数据中随机取出 1000 个样本,array
plt.hist(x2, bins=10)  # 10 个 bins
#plt.show()

# 散点图
x3=np.random.normal(size=1000) #随机生成 1000 个正态分布数据
y3=np.random.normal(size=1000) #随机生成另 1000 个正态分布数据
plt.scatter(x3,y3)
#plt.show()

# 箱式图
plt.boxplot(x)
#plt.show()


# 曲线图
x1 = np.arange(-5, 5, 0.01)
y1 = x1 ** 2
plt.plot(x1, y1)
plt.show()
plt.plot(x1, y1, color='g')  # 设置线为绿色
plt.plot(x1, y1, linestyle='--')
plt.plot(x1, y1, marker='+')
plt.show()
plt.plot(x1, y1,'ro-')  # 顺序是颜色,标记,线型,
plt.show()
plt.plot(x1, y1,'b:d')  # 顺序是颜色,标记,线型,
plt.show()
plt.plot(x, y, 'g^', x1, y1, 'g-')  # 两张图画一起
plt.show()
'''
#图例
y4=x**2
y5=x**3
plt.plot(x,y4,'r-',label='line 1')  # 图例
plt.plot(x,y5,'b-',label='line 2')  # 图例
plt.title("style config")   # 最上面的title
plt.xlabel("x range")   # x轴说明
plt.ylabel("y range")   # y轴说明
plt.legend(loc="best")   # 图例所在位置,默认upper right,最好设成best
plt.grid(color='k', linestyle='--', alpha=0.5)    # 显示网格(默认不显示),黑色、虚线、半透明
plt.show()


