# list methods part 2
# split()

# s = 'surendra kumar panda'
# print(s.split())

# s = 'surendra kumar panda'
# print(s.split('a'))

# s = 'surendra kumar panda'
# print(s.split('u'))

# s = 'surendra kumar pandau'
# print(s.split('u'))

# dob = '1-1-2000'
# print(dob.split('-'))


# dob = '1-1-2000'
# print(dob.split('*'))

# join()

# l = ['surendra', 'priyanka', 'rahul', 'zini']
# s = '+'.join(l)
# print(s)


# l = ['surendra', 'priyanka', 'rahul', 'zini']
# s = '*'.join(l)
# print(s)


# l = ['surendra', 'priyanka', 'rahul', 'zini']
# s = ''.join(l)
# print(s)


# l = ['surendra', 'priyanka', 'rahul', 'zini']
# s = ' '.join(l)
# print(s)

# l = ('surendra', 'priyanka', 'rahul', 'zini')
# s = '.'.join(l)
# print(s)


# removing space from the string
# rstrip()
# s = 'surendra       '
# print(len(s))
# print(len(s.rstrip()))

# #lstrip()
# s = '       surendra       '
# print(len(s))
# print(len(s.rstrip()))


# # strip()
# s = '       surendra       '
# print(len(s))
# print(len(s.strip()))

# fill char
# zfill()
# s = 'surendra'
# print(s.zfill(15))


# s = 'surendra'
# print(s.zfill(50))


# s = 'surendra'
# print(s.zfill(9))

# rjust()

# s = 'hello'
# print(s.rjust(10))


# s = 'surendra'
# print(s.rjust(50))


# s = 'surendra'
# print(s.rjust(10, '*'))


# # ljust()
# s = 'surendra'
# print(s.ljust(10, '*'))


# center()

# s = 'surendra'
# print(s.center(20))


# s = 'surendra'
# print(s.center(20, '*'))


# s = 'surendra'
# print(s.center(21, '*'))


# min()
# s = 'surendra'
# print(min(s))

# s = 'surendra'
# print(max(s))


# s = 'surendra'
# print(sorted(s))


# s = 'surendra'
# print(sorted(s,reverse=True))


# isidentifier()

# s = '123abc'
# print(s.isidentifier())


# s = 'abc123'
# print(s.isidentifier())


# s = 'True'
# print(s.isidentifier())


# s = '***aaa'
# print(s.isidentifier())

# s = 'surendra'
# for i in enumerate(s):
#     print(i)


s = 'surendra'
for i, j in enumerate(s):
    print(i, j)
