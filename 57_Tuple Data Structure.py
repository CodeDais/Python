# creation of tuple in different way
# creation of empty tuple
# t = ()
# print(t)
# print(type(t))

# creation of tuple with single value

# t = (23,)
# print(t)
# print(type(t))


# creation of tuple with differet data items
# t = (23, 'surendra', 455.78, False)
# print(t)

# creation of tuple without using ()

# t = 10, 20, 30, 'surendra', 455, False
# print(t)
# print(type(t))

# creation of tuple using tuple()

# l = [10, 20, 30, 40, 50]
# t = tuple(l)  # list to tuple
# print(t)
# print(l)


# t = tuple(range(10))
# print(t)


# t = tuple('surendra')
# print(t)


# t=(10,23,45,67)
# t[1]=999
# print(t)


# t = (10, 23, 45, 67, 10, 10, 67)
# print(t[-1])

# t = (23, 33, 43, 53, 63)
# print(t[::])
# print(t[:2])
# print(t[::2])


# t = (23, 33, 43, 53, 63)
# l = (24, 34, 44, 54, 64)
# s = (25, 35, 45, 55, 65)
# p = t+l+s
# print(p)


# t = (23, 33, 43, 53, 63)
# l = t*3
# print(l)

# traverse using for loop
# t = (23, 33, 43, 53, 63)
# for i in t:
#     print(i)

# traverse using while loop
# t = (23, 33, 43, 53, 63)
# i = 0
# while i < len(t):
#     print(t[i])
#     i = i+1

# t1=(10,11)
# t2=(10,1)
# t3=(10,1)
# print(cmp(t1,t2)) # 1
# print(cmp(t2,t1)) #-1
# print(cmp(t2,t3)) # 0


# tuple packing and unpacking

# packing


# a = 23
# b = 33
# c = 43
# d = 'surendra'
# e = 'rahul'
# t = a, b, c, d, e  # packing
# print(t)
# print(type(t))

# unpacking
# t = (23, 33, 43, 'surendra', 'rahul')
# a, b, c, d, e = t
# print(a, b, c, d, e)


# def fun():
#     l = [10, 20, 30, 40, 50]
#     return (l[0], l[2], l[4])

# t=fun()
# print(t)


# nested tuple
# t = ((23, 'surendra', 79.8), (23, 'priyanka', 76.8))
# # print(t[0])
# # print(t[0][1])

# for i in t:
#     print(i)

# t = ((23, 'surendra', 79.8), [23, 'priyanka', 76.8])
# t[1][1] = 'ajanli'
# print(t)

# t = (i for i in range(10))
# print(t)
# t = (i for i in range(10))
# print(type(t))
