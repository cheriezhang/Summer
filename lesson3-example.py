#!/usr/bin/python
# -*- coding: UTF-8 -*-

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import matplotlib

import pandas as pd
import urllib
import tempfile
import shutil
import zipfile

# temp_dir = tempfile.mkdtemp()
# data_source = "http://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip"
# zipname = temp_dir + '/Bike-Sharing-Dataset.zip'
# urllib.urlretrieve(data_source, zipname)  # 获取数据
#
# zip_ref = zipfile.ZipFile(zipname, 'r')
# zip_ref.extractall(temp_dir)
# daily_path = temp_dir + '/day.csv'
# daily_data = pd.read_csv(daily_path)
# zip_ref.close()
# shutil.rmtree(temp_dir)  # 删除临时文件目录

matplotlib.rc('figure', figsize=(14, 7))
matplotlib.rc('font', size=14)
matplotlib.rc('axes', grid=False)
matplotlib.rc('axes', facecolor='white')

daily_data = pd.read_csv('Bike-Sharing-Dataset/day.csv')
daily_data['dteday'] = pd.to_datetime(daily_data['dteday'])

drop_list = ['instant', 'season', 'yr', 'mnth', 'holiday', 'workingday', 'weathersit', 'atemp', 'hum']  # 丢掉上述列数据
daily_data.drop(drop_list, inplace=True, axis=1)  # 返回到原表(inplace=true),即删除不需要的列数据


# 关联分析
# 1、散点图——分析变量关系
def scatterplot(x_data, y_data, x_label, y_label, title):
    # 创建一个子图对象,因是一个图,无输入参数,返回两个变量
    fig, ax = plt.subplots()  # fig:容器对象,ax:画图对象
    # 不显示顶部和右侧的坐标线
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    # x轴,y轴,点的大小,点的颜色,点的透明度
    ax.scatter(x_data, y_data, s=10, color='#539caf', alpha=0.75)
    # 颜色是调色板
    ax.set_title(title)  # 标题
    ax.set_xlabel(x_label)  # x轴标签
    ax.set_ylabel(y_label)  # y轴标签


# scatterplot(x_data=daily_data['temp'],
#             y_data=daily_data['cnt'],
#             x_label='Normalized temperature (C)',
#             y_label='Check outs',
#             title='Number of Check Outs vs Temperature')

# 2、曲线图——拟合
import statsmodels.api as sm  # 统计模块
from statsmodels.stats.outliers_influence import summary_table

x = sm.add_constant(daily_data['temp'])  # 模型中的b0项,即常数项
y = daily_data['cnt']  # 需要拟合的y数据
regr = sm.OLS(y, x)  # 模型为y=b0+bi*x
res = regr.fit()  # 拟合
# st:数据汇总,data:数据详情,ss2:数据列 置信度95%
st, data, ss2 = summary_table(res, alpha=0.05)  # 从模型获得拟合数据
fitted_values = data[:, 2]  # data是一个矩阵,x行,y列,data[:,2]表示第二列对应的所有x值


# 包装曲线绘制函数
def lineplot(x_data, y_data, x_label, y_label, title):
    _, ax = plt.subplots()  # 创建绘图对象,返回两个参数
    #  绘制拟合曲线,lw=linewidth,alpha=transparency
    ax.plot(x_data, y_data, lw=2, color='#539caf', alpha=1)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)


# 调用绘图函数
# lineplot(x_data=daily_data['temp'],
#          y_data=fitted_values,
#          x_label='Normalized temperature (C)',
#          y_label='Check outs',
#          title='Line of Best Fit for Number of Check Outs vs Temperature')

# 3、带置信区间的曲线图——评估拟合结果
# 获得5%置信区间的上下界

predict_mean_ci_low = data[:, 4]  # data 中的第 4 列 Mean ci \n 95% low,data 是一个 array
predict_mean_ci_upp = data[:, 5]  # data 中的第 5 列 Mean ci \n 95% upp,data 是一个 array

# 创建置信区间 DataFrame,上下界
CI_df = pd.DataFrame(columns=['x_data', 'low_CI', 'upper_CI'])
CI_df['x_data'] = daily_data['temp']  # 温度
CI_df['low_CI'] = predict_mean_ci_low  # 置信区间下限
CI_df['upper_CI'] = predict_mean_ci_upp  # 置信区间上限
CI_df.sort_values('x_data', inplace=True)  # 根据 x_data(温度)进行排序


def lineplotCI(x_data, y_data, sorted_x, low_CI, upper_CI, x_label, y_label, title):
    _, ax = plt.subplots()  # 创建绘图对象,一个子图
    ax.plot(x_data, y_data, lw=1, color='#539caf', alpha=1, label='Fit')  # OLS 预测曲线
    # #顺序填充,绘制置信区间之间的区域
    # (排序后)x 坐标 下界 上界 填充色 透明度 标签
    ax.fill_between(sorted_x, low_CI, upper_CI, color='#539caf', alpha=0.4, label='95% CI')
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.legend(loc='best')


# 绘图
# lineplotCI(x_data=daily_data['temp'],
#            y_data=fitted_values,
#            sorted_x=CI_df['x_data'],
#            low_CI=CI_df['low_CI'],
#            upper_CI=CI_df['upper_CI'],
#            x_label='Normalized temperature (C)',
#            y_label='Check outs',
#            title='Line of Best Fit for Number of Check Outs vs Temperature')

# 4、双坐标曲线图——左右都有纵坐标
def lineplot2y(x_data, x_label, y1_data, y1_color, y1_label, y2_data, y2_color, y2_label, title):
    _, ax1 = plt.subplots()
    ax1.plot(x_data, y1_data, color=y1_color)
    ax1.set_ylabel(y1_label, color=y1_color)
    ax1.set_xlabel(x_label)
    ax1.set_title(title)
    ax2 = ax1.twinx()
    ax2.plot(x_data, y2_data, color=y2_color)
    ax2.set_ylabel(y2_label, color=y2_color)
    # ax2.spines['right'].set_visible(True)


# lineplot2y(x_data=daily_data['dteday'],  # x 轴:日期
#            x_label='Day',  # x 轴标签
#            y1_data=daily_data['cnt'],  # 第一个图:租赁总数曲线
#            y1_color='#539caf',  # 租赁曲线颜色
#            y1_label='Check outs',  # 左 y 轴标签
#            y2_data=daily_data['windspeed'],  # 第二个图:风速曲线
#            y2_color='#7663b0',  # 风速曲线颜色
#            y2_label='Normalized windspeed',  # 右 y 轴标签
#            title='Check Outs and Windspeed Over Time')    # 图的标题

# 分布分析
# 1、灰度图
def histogram(data, x_label, y_label, title, bins):
    _, ax = plt.subplots()
    res = ax.hist(data, color='#539caf', bins=bins)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    return res


# res = histogram(data=daily_data['registered'],
#                 x_label='Check outs',
#                 y_label='Frequency',
#                 title='Distribution of Registered Check Outs', bins=10)


# 2、堆叠直方图
def overlaid_histogram(data1, data1_name, data1_color,
                       data2, data2_name, data2_color,
                       x_label, y_label, title):
    # 归一化数据区间,对齐两个直方图的 bins
    max_nbins = 10
    # 取两个数据中的最小值作为最小值,最大值作为最大值
    data_range = [min(min(data1), min(data2)), max(max(data1), max(data2))]
    binwidth = (data_range[1] - data_range[0]) / max_nbins
    # 生成直方图 bins 区间,bins 可以是数字或者区间范围
    bins = np.arange(data_range[0], data_range[1] + binwidth, binwidth)
    # Create the plot
    _, ax = plt.subplots()
    ax.hist(data1, bins=bins, color=data1_color, alpha=1, label=data1_name)
    ax.hist(data2, bins=bins, color=data2_color, alpha=0.75, label=data2_name)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    ax.legend(loc='best')
    return bins


# Call the function to create plot
# bins_boundary = overlaid_histogram(data1=daily_data['registered'],
#                                    data1_name='Registered',
#                                    data1_color='#539caf',
#                                    data2=daily_data['casual'],
#                                    data2_name='Casual',
#                                    data2_color='#7663b0',
#                                    x_label='Check outs',
#                                    y_label='Frequency',
#                                    title='Distribution of Check Outs By Type')

# 3、概率密度图
# 计算概率密度
from scipy.stats import gaussian_kde  # 导入 gaussian_kde 模块,使用高斯核函数 kde=核密度估计

data = daily_data['registered']  # 有预约的租赁数量

# kde = kernal density estimate: https://en.wikipedia.org/wiki/Kernel_density_estimation
density_est = gaussian_kde(data)  # 返回 KDE 类的一个实例
# Computes the coefficient (`kde.factor`) that multiplies the data covariance matrix to obtain the kernel covariance matrix.
# The default is `scotts_factor`.
# A subclass can overwrite this method to provide a different method, or set it through a call to `kde.set_bandwidth`.

density_est.covariance_factor = lambda: .3  # 0.3 是带宽。h为控制平滑程度的参数。数值越大,越平滑。过大刻画细节差,过小不平滑
# Computes the covariance matrix for each Gaussian kernel using covariance_factor().
density_est._compute_covariance()  #
x_data = np.arange(min(data), max(data), 200)  #


# 定义函数,绘制密度估计曲线
def densityplot(x_data, density_est, x_label, y_label, title):
    _, ax = plt.subplots()
    # 纵轴:density_est(x_data),高斯核的数据点:x_data
    ax.plot(x_data, density_est(x_data), color='#539caf', lw=2)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)


# 调用自定义绘图函数
# densityplot(x_data=x_data,
#             # 横轴,是从小到大排列的预约租赁数,间隔 200 #纵轴,是一个类的实例
#             density_est=density_est,
#             x_label='Check outs',
#             y_label='Frequency',
#             title='Distribution of Registered Check Outs')

# 组间分析
# 1、柱状图
# 取出 weekday、cnt 两列数据 按 weekday 分组 计算均值和方差
mean_total_co_day = daily_data[['weekday', 'cnt']].groupby('weekday').agg([np.mean, np.std])
# 将 MultiIndex 中的 level = 0 去掉,变为非 MultiIndex
mean_total_co_day.columns = mean_total_co_day.columns.droplevel()


# 定义函数,绘制柱状图(bar)
def barplot(x_data, y_data, error_data, x_label, y_label, title):
    _, ax = plt.subplots()
    ax.bar(x_data, y_data, color='#539caf', align='center')  # 柱状图
    # ls='None'或 lingstyle='None',表示将 errorbar 之间的连线去掉
    # lw = linewidth
    ax.errorbar(x_data, y_data, yerr=error_data, color='#297083', ls='none', lw=5)  # 方差曲线
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)


# barplot(x_data=mean_total_co_day.index.values,
#         y_data=mean_total_co_day['mean'],
#         error_data=mean_total_co_day['std'],
#         x_label='Day of week',
#         y_label='Check outs',
#         title='Total Check Outs By Day of Week (0 = Sunday)')

# 2、堆积柱状图
# 按 weekday 将字段 registered 和 casual 分组后,计算均值
mean_by_reg_co_day = daily_data[['weekday', 'registered', 'casual']].groupby('weekday').mean()
# 统计总数,增加字段 total
mean_by_reg_co_day['total'] = mean_by_reg_co_day['registered'] + mean_by_reg_co_day['casual']
# 统计预约租赁的占比,增加字段 reg_prop,值范围 0 ~ 1
mean_by_reg_co_day['reg_prop'] = mean_by_reg_co_day['registered'] / mean_by_reg_co_day['total']
# 统计偶然租赁的占比,增加字段 casual_prop,值范围 0 ~ 1
mean_by_reg_co_day['casual_prop'] = mean_by_reg_co_day['casual'] / mean_by_reg_co_day['total']


def stackedbarplot(x_data, y_data_list, y_data_names, colors, x_label, y_label, title):
    _, ax = plt.subplots()
    # 循环绘制堆积柱状图
    for i in range(0, len(y_data_list)):  # 此处有两个柱状图,可以不用循环
        if i == 0:  # 第一个柱状图
            ax.bar(x_data, y_data_list[i],
                   color=colors[i], align='center',
                   label=y_data_names[i])

        else:  # 第二个柱状图
            ax.bar(x_data, y_data_list[i],
                   color=colors[i], bottom=y_data_list[i - 1],  # 底部为上一个柱状图的顶端
                   align='center',
                   label=y_data_names[i])
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    ax.legend(loc='best')


# stackedbarplot(x_data=mean_by_reg_co_day.index.values,
#                y_data_list=[mean_by_reg_co_day['reg_prop'], mean_by_reg_co_day['casual_prop']],
#                y_data_names=['Registered', 'Casual'],
#                colors=['#539caf', '#7663b0'],
#                x_label='Day of week',
#                y_label='Proportion of check outs',
#                title='Check Outs By Registration Status and Day of Week (0 = Sunday)')


# 3、分组柱状图
def groupedbarplot(x_data, y_data_list, y_data_names, colors, x_label, y_label, title):
    _, ax = plt.subplots()
    total_width = 0.8  # 每一组柱状图的宽度
    ind_width = total_width / len(y_data_list)  # 每一个柱状图的宽度
    #  计算每一个柱状图的中心偏移
    alteration = np.arange(-total_width + ind_width, total_width - ind_width, ind_width)
    for i in range(0, len(y_data_list)):  # 横向散开绘制
        ax.bar(x_data + alteration[i], y_data_list[i],
               color=colors[i], label=y_data_names[i], width=ind_width)
    # 分别绘制每一个柱状图
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    ax.legend(loc='upper right')

# groupedbarplot(x_data=mean_by_reg_co_day.index.values,  # array([0, 1, 2, 3, 4, 5, 6])
#                y_data_list=[mean_by_reg_co_day['registered'],  # 预约租赁数量
#                             mean_by_reg_co_day['casual']],  # 偶然租赁数量
#                y_data_names=['Registered', 'Casual'], colors=['#539caf', '#7663b0'],
#                x_label='Day of week', y_label='Check outs',
#                title='Check Outs By Registration Status and Day of Week (0 = Sunday)')

# 4、箱式图
days = np.unique(daily_data['weekday'])
bp_data = []
for day in days:
    bp_data.append(daily_data[daily_data['weekday'] == day]['cnt'].values)
    # 自定义绘图函数


def myboxplot(x_data, y_data, base_color, median_color, x_label, y_label, title):
    _, ax = plt.subplots()
    ax.boxplot(y_data, patch_artist=True,  # 箱子是否颜色填充
               #medianprops={'color': base_color},  # 中位数线颜色
               # 箱子颜色设置,color:边框颜色,facecolor:填充颜色
               #boxprops={'color': base_color, 'facecolor': median_color},
               #whiskerprops={'color': median_color},  # 猫须颜色 whisker
               #capprops={'color': base_color})  # 猫须界限颜色 whisker cap
               )
    # 箱图与 x_data 保持一致
    ax.set_xticklabels(x_data)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)


# 调用绘图函数
# myboxplot(x_data=days,
#         y_data=bp_data,
#         base_color='#539caf',
#         median_color='#7663b0',
#         x_label='Day of week',
#         y_label='Check outs',
#         title='Total Check Outs By Day of Week (0 = Sunday)')

plt.show()

