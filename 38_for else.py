# for else
# for loop execute fully without having break

# for i in range(10):
#     print(i)
# else:
#     print("i m else block")


# if break executed inside for loop then our else block #wont be execute
for i in range(10):
    if i==6:
        break
    print(i)
else:
    print("i m else block")