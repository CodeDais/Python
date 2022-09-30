def star(num):
    print('*'*num)
    if num == 5:
        return
    star(num+1)


star(1)
