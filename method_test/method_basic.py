# 默认参数放后面，
def  basic_fun(x:int,n=2):
    i = 0
    y = 1
    while i < n:
        y = y * x
        i += 1
    return y

print(basic_fun(100))
print(basic_fun(100,n=3))

# 默认参数不能是可变对象，多次调用后结果是['a', 'a', 'a', 'a']，因为定义函数的时候变量a已经被赋值[]了，所以a每次都会指向[]对象
def  fun_list(a=[]):
    a.append('a')
    return a

fun_list()
fun_list()
print(fun_list())

def fun_list1(a=None):
    a = []
    a.append('a')
    return a 
fun_list1()
fun_list1()
print(fun_list1())




