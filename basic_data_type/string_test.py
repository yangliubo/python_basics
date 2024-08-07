'''
增：  创建  合并  插入 
删：  单个元素  字符串
改：  替换 
查：  元素个数  元素坐标
过滤
占位符
大小写
分割
统计
'''
import string
import random
# 1、增
# 直接赋值
str_1 = 'gogogo'
str_2 = '2024'
str_3 = str_1+str_2
# print(str_3)
# string类获取
# ascii_letters:小写+大写 a-z  ascii_lowercase:小写a-z  ascii_uppercase:大写A-Z  digits: '0123456789'
str_4 = string.ascii_letters
str_5 = string.ascii_lowercase
str_6 = string.ascii_uppercase
str_7 = string.digits
print(str_4,str_5,str_6,str_7,type(str_7))

print('abc'.join(['e','f','g']))

# random.choice方法 随机获取一个元素
print(random.choice('abcd'))
# 随机生成一个8位的字符串
''.join(random.choice(string.ascii_letters)  for i in range(8))


# 3、查
# 查询某个元素（字符串）存在字符串中的个数 
str_1 = 'abcdabcdafabc'
str_2 = 'ab'
print(str_1.count(str_2))
# 查询某个元素是否是大写字母、小写字母、数字
str_1 = '4'
print(str_1.isupper())
print(str_1.islower())
print(str_1.isdigit())
print(ord('A')<=ord(str_1)<=ord('Z'))
print(ord('a')<=ord(str_1)<=ord('z'))
print(ord('0')<=ord(str_1)<=ord('9'))


# 4、改
str_3= str_1.replace('ab','mm')
print(str_3)


