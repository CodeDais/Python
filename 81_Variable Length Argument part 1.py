# variable length argumnet (non-keyword)

# issues

# def fun(a, b, c, d, e):
#     print(a, b, c, d, e)


# fun(10, 20, 30, 40, 50, 60, 90, 89, 78)


# solution

# def fun(*a):
#     # print(type(a))
#     print(a)


# fun(10, 20)
# fun(10, 20, 30)
# fun(10, 20, 77, 89, 67)
# fun(10)
# fun()


# def fun(*args):
#     print(args)


# fun(10, 20, 33, 56)


# def fun(*args):
#     print(args)


# fun(10, 20, 33, 56, [88, 89, 78],
#     (10, 20, 33, 41, 23, 11, 67), True, False, 10+20j)


# variable length keyword argument + positional argumnet

# def fun(x, *a):
#     print('x is :', x)
#     print('a is :', a)


# fun(10, 20, 30, 40)


# def fun(*a, x):
#     print('x is :', x)
#     print('a is :', a)


# fun(10, 20, 30, 40)


# missing 1 required keyword-only argument: 'x'
# def fun(*a, x):
#     print('x is :', x)
#     print('a is :', a)


# fun(10, 20, 30, x=40)


# def fun(*a, x):
#     print('x is :', x)
#     print('a is :', a)


# fun(x=40,10, 20, 30)


# def fun(x, *a):
#     print('x is :', x)
#     print('a is :', a)


# fun(10, 20, 30, x=40)


# def fun(*a, x):
#     print('x is :', x)
#     print('a is :', a)


# fun(10, 20, 30, x=40)


# def fun(*a, x):
#     print('x is :', x)
#     print('a is :', a)


# fun(10,20,x=40)


# deafult argument + variable length argumnet

# def fun(*a,x=10):
#     print('a is ',a)
#     print('x is ',x)

# fun(99)


# def fun(*a, x=10):
#     print('a is ', a)
#     print('x is ', x)


# fun(99, 123, 44, 12, 78, 900, x=789)


# def fun(x=10, *a):
#     print('a is ', a)
#     print('x is ', x)


# fun(99, 123, 44, 12, 78, 900, x=789)


# def fun(x=10, *a):
#     print('a is ', a)
#     print('x is ', x)


# fun(99, 123, 44, 12, 78, 900)


# def fun(x=10, *a):
#     print('a is ', a)
#     print('x is ', x)


# fun(99, 123, 44, 12, 78, 900)


# keyword argument + positional argumnet + varible length argumnet


# def fun(a, b, *n, x=10):
#     print(a)
#     print(b)
#     print(n)
#     print(x)


# fun(10, 20)


# def fun(a, b, *n, x=10):
#     print(a)
#     print(b)
#     print(n)
#     print(x)


# fun(10, 20, 30, 40, 50, x=999)


# def fun(a, b, x=10, *n):
#     print(a)
#     print(b)
#     print(n)
#     print(x)


# fun(10, 20, 30, 40, 50, x=999)


# def fun(a, b, x=10, *n):
#     print(a)
#     print(b)
#     print(n)
#     print(x)


# fun(10, 20, 30, 40, 50)


# def fun(a, b, x=10, *n):
#     print(a)
#     print(b)
#     print(n)
#     print(x)


# fun(10, 20, x=30, 40, 50)


