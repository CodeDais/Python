# l = [10, 20, 30, 40, 50]
# for i in l:
#     print(i)


# l = [10, 20, 30, 40, 50]
# i = 0
# while i < len(l):
#     print(l[i])
#     i = i+1


l = [10, 20, 30, 16, 8, 24, 40, 64, 50]
for i in l:
    if i % 4 == 0 and i % 8 == 0:
        print(i)
