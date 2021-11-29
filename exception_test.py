# -*- encoding: utf-8 -*-
'''
@File    :   exception_test.py
@Time    :   2021/11/30 00:03:34
@Author  :   希瓦 
'''
#python 捕获异常

a = '123'


try :
    b = a + 1

except  Exception as err:
    print('a不是数字类型数据',err)

else:
    print('b顺利生成')



#抛出异常

