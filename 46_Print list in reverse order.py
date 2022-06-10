# print list in revrese order using positive index

l = [10, 20, 30, 40, 50]
n = len(l)-1

while n >= 0:
    print(l[n])
    n = n-1


# print list in revrese order using negative index

l = [10, 20, 30, 40, 50]

i = -1

while i >= -len(l):
    print(l[i])
    i = i-1
