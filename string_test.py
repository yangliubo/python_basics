import string
# 生成26个英文字母
str_1 = string.ascii_lowercase
str_2 = string.ascii_uppercase
# print(str_1)
# print(str_2)

# 判断字符是在 A-Z
x = ord('A')
print(x)

# 判断某个字符（字符串）是否有重复  按字符串分割，列表个数大于2就是有重复
y = 'aabc'
x= y.split('a')
print(x)
print(len(x))

# 判断字符串中是否有数字， 	
# 如果 string 只包含数字则返回 True 否则返回 False.
x = 'abc123'
y = '123'
if x.isdigit():
    print('x是数字')
if y.isdigit():
    print('y是数字')

# 增删改查
# 改--替换 replace 
x = 'abbc123'
y = x.replace('b','m')
print(y)

    
# 去重
A = 'nihaooo'
l = list(set(A))
l.sort(key=A.index)
s1 = ''.join(l)