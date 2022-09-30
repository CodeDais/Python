# Fibonacci Series using Recursion

# 0 1 1           2

# 0 1 1 2         3

# 0 1 1 2 3       5

# 0 1 1 2 3 5     8


def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num-1)+fib(num-2)


print(fib(6))
