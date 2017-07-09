#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

# 一维的Series
'''
s = pd.Series([0.1, 0.2, 0.3, 0.4], index=['a', 'b', 'c', 'd'])
print "Pandas数据结构之Series 默认索引:"
print s
print s[1], type(s[1])
print s['b'], type(s['b'])
s1 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4})
print "Pandas数据结构之Series dict构造:"
print s1
print dir(s1)
print "乘100"
print s1 * 100
print "取一段数据"
print s1['a':'c']
print "取特定数据"
print s1[['a', 'c']]  #双[[]]
print "有条件取数据"
print s1[s1 > 3]
print "计算平均值"
print s1.mean()
print "加法,取并集相加"
s1_1 = s1[['a', 'c']]
s1_2 = s1[['b', 'c']]
print s1_1 + s1_2    #为什么NaN了?
'''
# 二维的DataFrame  是表的结构
data = {'country': ['Belgium', 'France', 'Germany', 'Netherlands', 'United Kingdom'],
        'population': [11.3, 64.3, 81.3, 16.9, 64.9],
        'area': [30510, 671308, 357050, 41526, 244820],
        'capital': ['Brussels', 'Paris', 'Berlin', 'Amserdam', 'London']}
countries = pd.DataFrame(data)
print "原始表"
print countries
print "横轴"
print countries.index  # 输出:RangeIndex(start=0, stop=5, step=1)
print "纵轴"
print countries.columns  # 输出: Index([u'area', u'capital', u'country', u'population'], dtype='object')
print "内容"
print countries.values
print "数据类型"  # 按列分
print countries.dtypes
# print "数据信息"
# print countries.info()
print "设置 纵轴"  # 设置哪个,哪个就成为了index 即纵轴
print countries.set_index('country')
print "取一列"  # 设置哪个,哪个就成为了index 即纵轴
print countries['population']
print "计算人口密度并加一列"
countries['density'] = countries['population'] * 1000000 / countries['area']
print countries
print "根据条件取"
print countries[countries['density'] > 300]
print "根据某一列排序"  # 一定要有by,by写字段名,升序排列为true,降序为false
print countries.sort_values(by='density', ascending=False)
print "统计学(包括平均值,标准差,最小值,前25%,50%,75%,最大值)"  # 一定要有by,by写字段名,升序排列为true,降序为false
print countries.describe()  # 参数由,百分比分界线,包括哪列,不包括哪列

print "图表操作"
# 可以拖动和局部放大

# countries.plot()
# plt.show()  # plt是import matplotlib.pyplot as plt的简称

# kind有几种line(折线图default),bar,barh,hist,box(箱型图),kde(平滑曲线),area,pie(饼图),scatter(散点图),hexbin(热力图)

# countries['population'].plot(kind='kde')   #两张图片都显示了,但不能同时显示
# plt.show()

print "去除数据"
countries1 = countries.set_index(keys='country')
countries2 = countries.drop(['area'], axis=1)
print countries1
print countries2
print "使用loc选取数据loc['条件','列名']"
print countries1.loc['France', 'density']  #结果是一个值95.7831576564
print countries1.loc['France': 'Netherlands', :]   #结果是一个表
print countries1.loc[countries1['density'] > 300, ['capital', 'population', 'density']]
print "使用loc选取数据iloc['选行','选列']"
print countries1.iloc[0:2, 0:3]
