# -*- encoding: utf-8 -*-
'''
@File    :   exception_test.py
@Time    :   2021/11/30 00:03:34
@Author  :   希瓦 
'''
#python 捕获异常
'''
https://www.cnblogs.com/beile/p/10789333.html
当发生异常时，我们就需要对异常进行捕获，然后进行相应的处理。python的异常捕获常用try...except...结构，
把可能发生错误的语句放在try模块里，用except来处理异常，每一个try，都必须至少对应一个except。此外，与python异常相关的关键字主要有：
try/except : 捕获并处理异常
pass : 忽略异常
as : 定义异常实例 except myerror as e
else : 如果try中的语句没有发生异常，则执行else中的语句
finally : 无论是否出现异常都会执行的代码
raise : 抛出/引发异常

'''



a = '123'


try :
    b = a + 1

except  Exception as err:
    print('a不是数字类型数据',err)

else :
    print('b顺利生成')

finally :
    print('最后执行finally')


#主动抛出异常

i = 1
if i == 1 :
    raise Exception('这是我抛出的异常')

#自定义异常
class  ylberror(Exception):
    def __init__(self,msg):
        self.msg =  msg

    def __string__(self):
        return self.msg

try :
   raise ylberror('错误信息')

except  ylberror as a:
    print('a不是数字类型数据',a)

else :
    print('这里是else')

finally : 
    print('这里是finally')
