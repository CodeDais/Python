# tail recursion
# def fun(num):
#     if num == 4:
#         return
#     else:
#         print(num)
#         fun(num+1)


# fun(1)


# non - tail recursion

def fun(num):
    if num == 4:
        return
    else:
        fun(num+1)
        print(num)


fun(0)
