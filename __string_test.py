# -*- encoding: utf-8 -*-
'''
@File    :   __string_test.py
@Time    :   2021/12/05 23:49:14
@Author  :   希瓦 


在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法
当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
__str__方法需要返回一个字符串，当做这个对象的描写

不知道大家再写程序是，打印一个实例化对象时，打印的其实时一个对象的地址。而通过__str__()函数就可以帮助我们打印对象中具体的属性值，或者你想得到的东西。

因为再python中调用print()打印实例化对象时会调用__str__()如果__str__()中有返回值，就会打印其中的返回值。
https://www.cnblogs.com/bao9687426/p/9812040.html
https://www.runoob.com/note/41154

'''
class ylb:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return '这里打印的是ylb实例的描述信息'

abc  = ylb('111','222')
print(abc)