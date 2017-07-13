#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    # linespace用于间隔采样
    # numpy.linspace(start(起点), stop(终点), num=50(采样点个数), endpoint=True, retstep=False, dtype=None)
    for i in range(1, 7):  # up to 7 but not include 7
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
    plt.legend(range(1, 7))  # 图例
#下面两句是matplotlib的显示
#sinplot()
#plt.show()

import seaborn as sns
#引入seaborn后设置风格
'''
sns.set_style('ticks')  # 强调坐标轴模式darkgrid/whitegrid,dark/white,ticks
sns.set_context('paper') #paper, notebook, talk, poster 没什么区别??
sns.despine()   # 默认显示左下坐标轴
sns.despine(offset=20)   # 偏移量20point 不紧挨着
sinplot()
plt.show()
'''

#颜色管理
sns.set()  # 一键设置
#sns.palplot(sns.color_palette())  # 画出当前的调色板,默认 6 色 palplot是绘制调色板图类似boxplot

sns.set_palette(sns.color_palette("hls", 10))  # 设置为 hls 调色板,10 色
#sns.palplot(sns.color_palette())

sns.set_palette(sns.color_palette("husl", 10))  # 设置为 husl 调色板,http://www.hsluv.org
#sns.palplot(sns.color_palette())

#sns.palplot(sns.color_palette("Greens", 20))    #设置20个绿色调色板

#sns.palplot(sns.color_palette("spring", 11))
#sns.palplot(sns.color_palette("summer", 11))
#sns.palplot(sns.color_palette("autumn", 11))
#sns.palplot(sns.color_palette("winter", 11))
plt.show()
