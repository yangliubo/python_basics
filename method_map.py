# -*- encoding: utf-8 -*-
'''
@File    :   method_map.py
@Time    :   2021/10/07 04:16:42
@Author  :   希瓦 
'''

'''
map() 会根据提供的函数对指定序列做映射。

第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
map() 函数语法：map(function, iterable, ...) 
function -- 函数
iterable -- 一个或多个序列
Python 2.x 返回列表。
Python 3.x 返回迭代器。
'''

x = map(abs,[-1,-2])
print(list(x))

y = map(lambda x:x**2,(1,2))
print(list(y))

