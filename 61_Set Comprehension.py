# Set comprehensions
# without set comprehensions

# create a set from list
# l = [23, 33, 43, 53, 63]
# s = set()

# for i in l:
#     s.add(i)

# print(s)

# with set comprehensions
# create a set from list

# l = [23, 33, 43, 53, 63]

# s = {i for i in l}
# print(s)


# ex

# l = [23, 33, 43, 53, 63]

# s = {i*2 for i in l}
# print(s)


# work with range


# s = {i for i in range(100, 111)}
# print(s)


# s = {i**2 for i in range(11)}
# print(s)


# craete a set by adding all the elemenet from 20 to 40 which is divisible by 4

# s = {i for i in range(20, 41) if i % 4 == 0}
# print(s)


# create a set from list called as names by adding the first char of each element
# names = ['surendra', 'priyanka', 'rahul', 'zini']

# s = {i[0] for i in names}
# print(s)


# names = ['surendra', 'priyanka', 'rahul', 'zini']

# s = {i[0].upper() for i in names}
# print(s)


# craete a set from a list (names) by adding all the elements but if the elmenet is priyanka then instread of priyanka add anjali

# names = ['surendra', 'priyanka', 'rahul', 'zini']

# s = {i if i != 'priyanka' else 'anjali' for i in names}
# print(s)
