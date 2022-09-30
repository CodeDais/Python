# find out sum of n natural number

def sumofallno(n):
    if n == 1:
        return n
    return n+sumofallno(n-1)


print(sumofallno(5))
