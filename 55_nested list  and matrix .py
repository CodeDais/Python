# Nested Lits
# l = [10, 20, 30, [40, 41, 42], 50, 60, 70]
# print(l)
# print(l[2])
# print(l[3])
# print(l[3][1])
# print(l[3][0])
# print(l[3][-1])
# print(l[-4][-2])


# l = [10, 20, 30, [40, 41, 42], 50, [51, 52, 53], 60, 70]
# print(l[5])
# print(l[2:6])


# l = [10, 20, 30, [40, 41, [1, 2, 3], 42], 50, 60, 70]

# print(l[3])
# print(l[3][2])
# print(l[3][2][1])
# print(l[-4])
# print(l[-4][-2])
# print(l[-4][-2][-2])


# Nested List as a Matrix

# l = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]

# print in row wise
# print(l[0])
# print(l[1])
# print(l[2])


# # print row wise using loop
# l = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]

# for i in l:
#     print(i)


# print


# l = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]

# for i in l:
#     for j in i:
#         print(j, end=' ')
#     print(' ')

# reverse this list
# l = [10, 20, 30, [40, 41, 42], 50, [51, 52, 53], 60, 70]
# l.reverse()
# print(l)


# l = [[40, 41, 42], [51, 52, 53]]
# l.reverse()
# print(l)

l = [[40, 41, 42], [51, 52, 53]]
for i in l:
    i.reverse()
print(l)