# set : 集合  无序！ 不重复！ 交集！ 并集！差集！

# 1、创建
set_1 = set(['a','b','c','d'])
set_2 = {'a','b','c'}
print(set_1,set_2)

# 2、增
# add方法只能添加一个str元素
set_1.add('e')
print(set_1)
# update 方法  str的可迭代对象
set_1.update(['f','a',1,2,4])
set_1.update(('d','g','w'))
print(set_1)

# 删
# 单次删除一个str,如果不存在会报错
set_1.remove(1)
print(set_1)

# set_1.remove(1)

# 集合间操作
set_2 = {'a','b','c'}
set_3 = {'c','d','e'}
# 列出集合set_2中set_3没有的元素
print(set_2-set_3)
# 交集
print(set_2|set_3)
# 并集
print(set_2&set_3)

