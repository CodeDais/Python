# Indirect Recursion

def fun1(num):
    if num <= 6:
        print(f'fun1 = {num*2}')
        fun2(num+1)
    return


def fun2(num):
    if num <= 6:
        print(f'fun2 = {num*100}')
        fun1(num+1)
    return


fun1(1)
