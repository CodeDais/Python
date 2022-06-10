# l = [10, 20, 30, 40, 50]
# s = ['surendra', 'priyanka', 999, 888, 777]
# r = l+s
# print(r)


# l = [10, 20, 30, 40, 50]
# s = ['surendra', 'priyanka', 999, 888, 777]
# a = [12.3, 45.7, True, False]
# r = l+s+a
# print(r)


# l = [10, 20, 30, 40, 50]
# s=[100]
# r = l+s
# print(r)


# l = [10, 20, 30, 40, 50]
# r = l*5
# print(r)


# l = [10, 20, 30, 40, 50]
# r = l*5.7
# print(r)


# l = [10, 20, 30, 40, 50]
# r = l*l
# print(r)


# mmembership operator ( in , not in)

# l=[10,20,30,40,50]
# print(20 in l)
# print(20 not in l)
# print(999 in l)
# print(999 not in l)


# l = [1, 2, 3, 5, 6, 7, 9, 11, 12, 17, 18, 23, 24, 25, 67, 92, 99]
# choice = int(input("Enter your lucky number : "))

# if choice in l:
#     print("yes ur lucky number is available")
# else:
#     print("sry lucky number is not avaiable")


l = [1, 2, 3, 5, 6, 7, 9, 11, 12, 17, 18, 23, 24, 25, 67, 92, 99]

choice = int(input("Enter your lucky number : "))

while True:
    if choice in l:
        print("yes u r lucky number is present")
        break
    else:
        print("sry u r lucky number is not present")
        choice = int(input("Enter your lucky number again: "))
