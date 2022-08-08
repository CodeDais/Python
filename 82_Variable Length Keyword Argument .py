# variable length keyword argument

# def fun(**a):
#     print(a)


# fun(x=10, y=20, z=[10, 20, 30])


# def fun(**a):
#     print(a)


# fun(x=10, y=20, z=[10, 20, 30], z1={1: 2, 2: 3, 3: 4})


# def fun(x, **a):
#     print(a)
#     print(x)


# fun(x=99, a=10, b=20, c=30)


# def fun(x, **a):
#     print(a)
#     print(x)


# fun(a=10, b=20, c=30, x=99)


# def fun(x, *z, ** a):
#     print(a)
#     print(x)
#     print(z)


# fun(99, a=10, b=20, c=30)


# def fun(x, *z, ** a):
#     print(a)
#     print(x)
#     print(z)


# fun(99, 88, 67, a=10, b=20, c=30)


# def fun(x, **a, *z):
#     print(a)
#     print(x)
#     print(z)


# fun(99, 88, 67, a=10, b=20, c=30)


# def fun(**a):
#     print(a)


# fun()

# def fun(**a):
#     print(a)


# fun(a={})


# def fun(*a, **b):
#     print(a)
#     print(b)


# fun()


def fun(*a, **b):
    print(a)
    print(b)


fun(x=99, y=89)
