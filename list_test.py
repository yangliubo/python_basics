# -*- encoding: utf-8 -*-
'''
@File    :   list_test.py
@Time    :   2021/10/07 04:00:52
@Author  :   希瓦 
'''

# 创建list
# 1、直接定义
list_1 =  [1,'m',(1,2)]
# 2、列表推导式
list_2 = [x**3 for x in range(3)]
print(list_2) 
list_3 = list(map(lambda x:x*3, range(3)))
print(list_3)