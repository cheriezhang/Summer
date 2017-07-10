#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

train = pd.read_csv('Train.csv', encoding='latin-1')
test = pd.read_csv('Test.csv', encoding='latin-1')

print "查看数据量"
print "train.csv", train.shape
print "test.csv", test.shape
print "查看数据基本情况"
print "describe()"
print train.describe()
print "查看列名"
print train.columns
print "查看每列的type"
print train.dtypes
print "查看数据前5条"
print train.head()
print "合并两个数据集"

data = pd.concat([train, test], ignore_index=True)

print data.shape
print "未知数据的数量"
print data.apply(lambda x: sum(x.isnull()))
# #apply括号里为匿名函数 用lambda来定义
# 语法为lambda [arg1 [,arg2,.....argn]]:expression

print "查看某一字段数据"
print data['City'].value_counts()[1:5]  # 提取最多的城市2到5名 的数量
print data['City'][1:5]  # 提取最前面的城市2到5名的名字
print len(data['City'].unique())  # 类似于distinct
data.drop('City', axis=1, inplace=True)
print data.columns
print "DOB列前10个"
print data['DOB'].head(n=10)
data['Age'] = data['DOB'].apply(lambda x: 117 - int(x[-2:]))  # 从DOB字段的倒数第二个字符起到结尾,结果是取年份
print data['Age'].head()

data.boxplot(column=['EMI_Loan_Submitted'], return_type='axes')
# data['EMI_Loan_Submitted'].plot(kind='box')  #等价与上一句
plt.show()

data['EMI_Loan_Submitted_Missing'] = data['EMI_Loan_Submitted'].apply(lambda x: 1 if (pd.isnull(x)) else 0)
print data[['EMI_Loan_Submitted', 'EMI_Loan_Submitted_Missing']].head(10)  # [[]]
data.drop('EMI_Loan_Submitted', axis=1, inplace=True)  # 有了新值将旧值删除

data.drop('Employer_Name', axis=1, inplace=True)

data['Existing_EMI'].fillna(data['Existing_EMI'].describe()['mean'], inplace=True)  # NaN值用空值代替

data['Interest_Rate_Missing'] = data['Interest_Rate'].apply(lambda x: 1 if pd.isnull(x) else 0)
data.drop('Interest_Rate', axis=1, inplace=True)

data['Lead_Creation_Date_Missing'] = data['Lead_Creation_Date'].apply(lambda x: 1 if pd.isnull(x) else 0)
data.drop('Lead_Creation_Date', axis=1, inplace=True)

data['Loan_Amount_Applied'].fillna(data['Loan_Amount_Applied'].median(), inplace=True)
data['Loan_Tenure_Applied'].fillna(data['Loan_Tenure_Applied'].median(), inplace=True)

data['Loan_Amount_Submitted_Missing'] = data['Loan_Amount_Submitted'].apply(lambda x: 1 if pd.isnull(x) else 0)
data['Loan_Tenure_Submitted_Missing'] = data['Loan_Tenure_Submitted'].apply(lambda x: 1 if pd.isnull(x) else 0)
data.drop(['Loan_Amount_Submitted', 'Loan_Tenure_Submitted'], axis=1, inplace=True)

data.drop('LoggedIn', axis=1, inplace=True)

data.drop('Salary_Account', axis=1, inplace=True)

data['Processing_Fee_Missing'] = data['Processing_Fee'].apply(lambda x: 1 if pd.isnull(x) else 0)
data.drop('Processing_Fee', axis=1, inplace=True)

data['Source'] = data['Source'].apply(lambda x: 'others' if x not in ['S122', 'S133'] else x)

print data.dtypes

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

var_to_Encode = ['Device_Type', 'Filled_Form', 'Var1', 'Var2', 'Mobile_Verified', 'Source']
for col in var_to_Encode:
    data[col] = le.fit_transform(data[col])

# 扩展成冗余列
# var_to_Encode = ['Device_Type', 'Filled_Form', 'Var1', 'Var2', 'Mobile_Verified', 'Source']
# data = pd.get_dummies(data, columns=var_to_Encode)
print data.dtypes

# 分离两个数据集
train = data.loc[data['Source'] == 0]
test = data.loc[data['Source'] == 1]
# 将区别数据集的 column 丢弃
train.drop('Source', axis=1, inplace=True)
test.drop(['Source', 'Disbursed'], axis=1, inplace=True)
# 分别写入文件
# train.to_csv('train_modified.csv', index=False)
# test.to_csv('test_modified.csv', index=False)

train_modified = pd.read_csv('Train.csv', encoding='latin-1')
test_modified = pd.read_csv('Test.csv', encoding='latin-1')
print "train size"
print train_modified.shape
print "test size"
print test_modified.shape