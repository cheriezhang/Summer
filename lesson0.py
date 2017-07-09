#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 预习课python
# part1 数据类型 重点string
x = 5  # 整型
print x
print type(x)
print x / 2

y = 5.0  # float型
print y
print type(y)
print y / 2

z = 5 ** 2  # 幂运算5^2
print z

s = "hello world"
s1 = "hello"
s2 = "world"
s3 = 1994
s4 = " hahaha "
print s
print type(s)
print len(s)
print s1 + s2
print "s3=1994的类型为", type(s3)  # 类似gettype()
print "str(s3)的类型为", type(str(s3))  # 类似str()强制类型转换
print "去掉s4左右的空格", s4.strip()
print "替换s4内容", s4.replace('ha', 'ah')  # 类似str_replace
print "判断s3是否为纯数字", str(s3).isdigit()
print "截取s中的子串,2参数", s[1:4]  # ell 从左至右从0开始,从右至左从-1开始
print "截取s中的子串,3参数", s[0:6:2]  # hlo 从0开始到6截止,每两位取一个字符
# 格式化输出
num = 30
position = "classroom"
print "there are %d student in the %s" % (num, position)

print "s串以空格切分", s.split()  # 返回格式为列表 类似explode()

# Part2 容器
# list 类似php中的数组,里面的元素类型随意
list = ['hello', 'world', 3.14, 100]
print "list长度", len(list)  # 类似sizeof()
print "list切片2参数", list[1:3]
print "list切片3参数", list[0:3:2]
print "list能做的操作", dir(list)
print "判断元素是否在list中", 'hello' in list  # 类似array_search()

for item in list:  # 类似foreach($results as $value) $result=>list  $value->item
    print type(item)

index = 0
while index < 3:  # 类似while
    print list[index]
    index += 1

# list能做的操作
# 'append','count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
list.append("append")  # 添加一个
print "after append", list
list.extend([1, 2, 3])  # 批量添加
print "after extend", list
list.remove(3)
print "after remove", list

list1 = [4, 5, 7, 1, 9, 3, 6, 7, 2]
sorted(list1, reverse=True)  # 新建列表 并降序
print "after sorted", list1
list1.sort()  # 覆盖原列表 可以加reverse参数 默认升序
print "after sort", list1

list2 = ['a', 'Ccc', 'dddD', 'bB']
list2_soreted = sorted(list2, key=str.lower, reverse=True)  # 新建列表 并降序 lower不能有()
print "after sorted", list2
print "after sorted", list2_soreted
list2.sort(key=len)  # 覆盖原列表 可以加reverse参数 默认升序
print "after sort", list2

# list_comprehension 列表推导式 对列表中每个元素做相同的操作
list1_3 = [item ** 3 for item in list1]  # 原列表不变
print list1
print "list1_3", list1_3

# 字典Dict 类似json与二维数组,与list的区别是{}和键值对 可以自动排序,按照key的首字母
dict1 = {'a': 0, 'b': 2, 'c': 4}  # 只有定义时用{},处理用[]
print dict1
print dir(dict1)
# 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems',
# 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault',
# 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues'
print "由key找value", dict1['a']
print "判断key是否在字典中", 'a' in dict1
for item in dict1:  # item是键值对中的key dict1[item]是键值对中的value
    print dict1[item], ' ', item

print "只取出keys", dict1.keys()  # 二维变一维 返回列表
print "只取出values", dict1.values()
# 成对取出键值对
for (char, num) in dict1.items():
    print "key:", char, " value:", num

dict1['d'] = 5
print "dict1添加元素", dict1
del dict1['d']
print "after del", dict1

# dict comprehension 字典推导式 同list 常用于把列表变成字典
origin_list = [1, 2, 3, 4, 5]
new_dict = {item: item ** 2 for item in origin_list if item >= 3}  # 注意花括号 最后是item的判断条件
print "由list生成dict",new_dict


# 文件读写
words_count = {}  # 用字典处理
phrase = open('lesson0.txt').read()
words = phrase.split(",")

for word in words:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1
        # for word in words_count:
        # print word, words_count[word]


# 函数def 函数名(参数) :
def add_num(x, y):
    return x + y


z = add_num(3, 4)
print z
