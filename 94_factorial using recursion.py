# factorial of a number using recursion

def fact(num):
    if num == 1:
        return 1
    return num*fact(num-1)


print(fact(4))
