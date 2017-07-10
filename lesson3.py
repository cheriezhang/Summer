#!/usr/bin/python
# -*- coding: UTF-8 -*-

#数据可视化
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
#按照key1的值分类,即为a,b分类,然后求a类的data1的均值和b类的data1的均值
print df['data1'].groupby(df['key1']).mean()

x = np.arange(0, 100)
y = random.sample(x, 10)
print x
print y
y1 = [(x > 90) | (x < 10)]
print y1
y2 = np.arange(0,50)
for i in np.arange(0,50):
    if i>=10 and i<=30 :
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

#matplotlib操作
#matplotlib:包 pyplot:类 gcf():方法
#fig = plt.gcf() 等价于下面的语句
#fig = matplotlib.pyplot.gcf()  #gcf = get current figure
#fig.set_size_inches(10, 10)
#展示图形 clear axis 清空坐标 clear figure 清空图 关闭图
# plt.show(), plt.cla(),plt.clf(),plt.close()

#正态分布
plt.figure(figsize=(10,5))
x = np.arange(-5,5,0.01)
y = stats.norm.pdf(x,0,1) #0,1为均值和方差
plt.plot(x,y)
plt.show()
