# -*- encoding: utf-8 -*-
'''
@File    :   list_test.py
@Time    :   2021/10/07 04:00:52
@Author  :   希瓦 
'''

# 一、创建list
# 1、直接定义
list_1 =  [1,'m',(1,2)]
# 2、列表推导式
list_2 = [x**3 for x in range(3)]
print(list_2) 
list_3 = list(map(lambda x:x*3, range(3)))
print(list_3)

# 二、列表与string互转
# 1、str to list
str_1 = 'abcde'
list_1 = list(str_1)
print(list_1)

str_2 = '8548775'
list_2 = list(str_2)
print(list_2)

# 2、list to str
# 方法1：''.join(list) 注意 该方法中list的元素必须是str类型，非str类型的如Int类型必须先转为str类型

list_1 = ['a','b','c','d','e']
str_1 = ''.join(list_1)
print(str_1)


list_2 = [1,2,3,4,5]
str_2 = ''.join([str(x) for x in list_2])
print(str_2)

# 三、list相关操作
list_1 = ['a','b','c']
print('------',list_1[-8:])

list_1 = ['a','a','b','c']
x  = set(list_1)
print(x)

# 四、list的一些方法