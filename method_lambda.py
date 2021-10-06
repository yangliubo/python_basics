# -*- encoding: utf-8 -*-
'''
@File    :   method_lambda.py
@Time    :   2021/10/07 04:50:58
@Author  :   希瓦 
'''

'''
匿名函数 
python 使用 lambda 来创建匿名函数。
lambda只是一个表达式

lambda函数的语法只包含一个语句，如下：lambda [arg1 [,arg2,.....argn]]:expression
'''

y = lambda a,b : a+b
print(y(1,2))