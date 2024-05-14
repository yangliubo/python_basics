# l = [1,1,2,3,5,8,13,21]

def fib(num):
    l = [0] * (num+1)
    l[0] = 1
    l[1] = 1
    for n in range(2,num+1):
        l[n] = l[n-1] + l[n-2]
    return l[num]

print(fib(10))


