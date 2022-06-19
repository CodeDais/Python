# List
# empty list
# l = []
# print(l)
# print(type(l))

# l = list()
# print(l)
# print(type(l))


# l = [10, 20, 'Surendra', 12.7, 89.0]
# print(l)

# create list from range()

# l=list(range(10))
# print(l)


# l = list(range(10, 20, 2))
# print(l)


# l = list(range(10, 21, 2))
# print(l)

# create a list from str:

# msg = 'hello good morning and have a nice day'
# l = msg.split()
# print(l)


# msg = 'hel-lo go-od m-orning- and- have- a nic-e d-ay'
# l = msg.split('-')
# print(l)

# indexing
# l = [10, 20, 30, 40, 50]
# print(l[2])

# slicing
# l = [10, 20, 30, 40, 50]
# print(l[:2])


# l = [10, 20, 30, 40, 50]
# print(l[::2])


# Traversing a list  using for loop
# l=[10,20,30,40,50]

# for i in l:
#     print(i)

# traversing a list using while loop
# l=[10,20,30,40,50]

# for i in l:
#     print(i)


# Traversing a list using while loop
# l = [10, 20, 30, 40, 50]
# i = 0
# while i < len(l):
#     print(l[i])
#     i = i+1


# # print only even data
# l = [10, 11, 1, 55, 20, 46, 65, 30, 41, 40, 50]

# for i in l:
#     if i % 2 == 0:
#         print(i)


# print all the element whcih is divisible by either 3 or 5
# l = [10, 11, 1, 55, 20, 46, 65, 30, 41, 40, 50]

# for i in l:
#     if i % 3 == 0 or i % 5 == 0:
#         print(i)


# list methods

# len()
# l=[10,20,30,40,50]
# print(len(l))

# count()


# l = [10, 20, 10, 40, 20, 50, 20]
# print(l.count(10))
# print(l.count(123))


# index()
# l = [10, 20, 10, 40, 20, 50, 20]
# # print(l.index(40))
# print(l.index(10))


# append()

# l = [10, 20, 10, 40, 20, 50, 20]
# l.append('rahul')
# print(l)
# l.append('zini')
# print(l)


#  add all the element from 20 to 30 in a list
# l = []
# for i in range(20, 31):
#     l.append(i)

# print(l)


#  add all the element from 100 to 300 in a list which is divisible by 25
# l = []
# for i in range(100, 301):
#     if i % 25 == 0:
#         l.append(i)

# print(l)


# insert() --> add any specific location
# l = [10,20,30,40,50]
# l.insert(1,999)
# print(l)

# l = [10, 20, 30, 40, 50]
# l.insert(4, 999)
# print(l)


# l = [10, 20, 30, 40, 50]
# l.insert(44, 999)
# print(l)


# extend
# add all the item of one list into another list

# l1 = [10, 20, 30]
# l2 = [100, 200, 300]
# l1.extend(l2)
# print(l1)


# l1 = [10, 20, 30]
# l2 = [100, 200, 300]
# l2.extend(l1)
# print(l2)


# l1 = [10, 20, 30]

# l1.extend('surendra')
# print(l1)


# remove()
#  remove any specific value
# l = [10, 20, 30, 40, 50]
# l.remove(30)
# print(l)


# l = [10, 20, 30, 40, 50]
# l.remove(75)
# print(l)

# pop()
# remove the last element and it will return that
# l = [10, 20, 30, 40, 50, 'surendra']
# print(l.pop())

# remove by index
# l = [10, 20, 30, 40, 50, 'surendra']
# print(l.pop(3))
# print(l)
