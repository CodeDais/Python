# list methods part
# keys()
# d = {23: 'surendra', 24: 'priyanka', 25: 'rahul', 26: 'zini'}

# print(d.keys())

# d = {23: 'surendra', 24: 'priyanka', 25: 'rahul', 26: 'zini'}

# for i in d.keys():
#     print(i)


# values()
# d = {23: 'surendra', 24: 'priyanka', 25: 'rahul', 26: 'zini'}

# print(d.values())


# d = {23: 'surendra', 24: 'priyanka', 25: 'rahul', 26: 'zini'}

# for i in d.values():
#     print(i)


# setdefault()
# d = {23: 'surendra', 24: 'priyanka', 25: 'rahul', 26: 'zini'}

# print(d)
# print(d.setdefault(999, 'anjali'))
# print(d)

# d = {23: 'surendra', 24: 'priyanka', 25: 'rahul', 26: 'zini'}

# print(d)
# print(d.setdefault(23, 'anjali'))
# print(d)


# d = {23: 'surendra', 24: 'priyanka', 25: 'rahul', 26: 'zini'}


# print(d.setdefault(23))

# d = {23: 'surendra', 24: 'priyanka', 25: 'rahul', 26: 'zini'}
# print(d)
# print(d.setdefault(999))
# print(d)


# update()
# d1 = {23: 'surendra', 24: 'priyanka', 25: 'rahul', 26: 'zini'}

# d2 = {1: 'collge', 2: 'university'}

# d1.update(d2)

# print(d1)
# print(d2)

# d1 = {23: 'surendra', 24: 'priyanka', 25: 'rahul', 26: 'zini'}

# d2 = {23: 'collge', 2: 'university'}

# d1.update(d2)

# print(d1)


# copy()
# d1 = {23: 'surendra', 24: 'priyanka', 25: 'rahul', 26: 'zini'}

# d2 = {}

# d2 = d1.copy()

# # print(d1)
# # print(d2)

# print(id(d1))
# print(id(d2))

# d1[24] = 'anjali'

# print(d1)
# print(d2)


# =

# d1 = {23: 'surendra', 24: 'priyanka', 25: 'rahul', 26: 'zini'}

# d2 = {}

# d2 = d1

# # print(d1)
# # print(d2)

# print(id(d1))
# print(id(d2))

# d1[24] = 'anjali'

# print(d1)
# print(d2)


# clear()
# d = {23: 'surendra', 24: 'priyanka', 25: 'rahul', 26: 'zini'}

# d.clear()
# print(d)


# formkeys()
# l = [23, 33, 43, 53, 63]
# d = dict.fromkeys(l)
# print(d)


# t = (23, 33, 43, 53, 63)
# d = dict.fromkeys(t)
# print(d)


# l = [23, 33, 43, 53, 63]
# d = dict.fromkeys(l, 'hello')
# print(d)


# d = dict.fromkeys(range(5), 1)
# print(d)


# d = dict.fromkeys(range(5), [1, 2, 3])
# print(d)

# d = dict.fromkeys([], [1, 2, 3])
# print(d)


# d = dict.fromkeys([], [])
# print(d)


# d = dict.fromkeys([1], [1])
# print(d)


# l = [23, 33, 43, 53, 63]
# d = {}.fromkeys(l)
# print(d)

