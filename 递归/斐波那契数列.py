def Fibonacci(n):
    if n == 2 or n == 1:
        return 1
    
    return Fibonacci(n-1)+Fibonacci(n-2)
# 1,1,2,3,5,8,13,21,34
print(Fibonacci(7))