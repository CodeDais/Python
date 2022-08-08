# # function alishing
# def calculations(a, b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)
#     print(a % b)


# calculations(10, 2)
# cal = calculations
# print('after alishing')
# cal(50, 10)


# ex 2:
# def calculations(a, b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)
#     print(a % b)


# calculations(10, 2)
# cal = calculations
# del calculations
# cal(50, 10)
# calculations(100,3)


# def calculations(a, b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)
#     print(a % b)


# cal = calculations
# print(id(calculations))
# print(id(cal))


def calculations(a, b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a % b)


cal = calculations
cl = calculations
c = cl
print(id(calculations))
print(id(cal))
print(id(cl))
print(id(c))
c(100, 2)
