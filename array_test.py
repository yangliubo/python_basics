# -*- encoding: utf-8 -*-
'''
@File    :   array_test.py
@Time    :   2021/10/07 00:45:09
@Author  :   希瓦 
'''
# 创建一个list,Python 没有内置对数组的支持，但可以使用 Python 列表代替。


# 创建一个二维数组
# 循环创建
array_two_dimension = []
for j in range(3):
    row_list = []
    for x in range(3):
        row_list.append(x**2)
    array_two_dimension.append(row_list) 
print(array_two_dimension)

# li列表推导式
array_two_dimension_concision = [[x**2 for x in range(3)] for i in range(3)]
print(array_two_dimension_concision)