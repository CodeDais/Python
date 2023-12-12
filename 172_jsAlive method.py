#sleep()

import time

# for i in range(5):
#     print(i)
#     time.sleep(5)


#

# print('surendra')
# time.sleep(2)
# print('priyanka')
# time.sleep(3)
# print('rahul')
# time.sleep(5)
# print('zini')
# time.sleep(10)


#is_alive()  method 
# if it is alive then it will return Ture or else False 

from threading import * 

# def fun1():
#     print('surendra')
#     time.sleep(5)
#     print('priyanka')

# t1=Thread(target=fun1)
# print('before starting t1 thread ',t1.is_alive())
# t1.start()
# print('after starting t1 thread ',t1.is_alive())


#ex 2 

# def fun1():
#     time.sleep(5)
#     print('surendra')
    
# def fun2():
#     print('priyanka')

# t1=Thread(target=fun1)
# t2=Thread(target=fun2)

# print('before starting t1 thread ',t1.is_alive())
# print('before starting t2 thread ',t2.is_alive())

# t1.start()
# t2.start()

# print('after starting t1 thread ',t1.is_alive())
# print('after starting t2 thread ',t2.is_alive())


# ex 3

# def fun1():
#     time.sleep(5)
#     print('surendra')
    
# def fun2():
#     time.sleep(10)
#     print('priyanka')

# t1=Thread(target=fun1)
# t2=Thread(target=fun2)

# print('before starting t1 thread ',t1.is_alive())
# print('before starting t2 thread ',t2.is_alive())

# t1.start()
# t2.start()

# print('after starting t1 thread ',t1.is_alive())
# print('after starting t2 thread ',t2.is_alive())


#ex 4 

# def fun1():
#     time.sleep(5)
#     print('surendra')
    
# def fun2():
#     time.sleep(10)
#     print('priyanka')

# t1=Thread(target=fun1)
# t2=Thread(target=fun2)

# print('before starting t1 thread ',t1.is_alive())
# print('before starting t2 thread ',t2.is_alive())

# t1.start()
# t2.start()

# time.sleep(15)
# print('after starting t1 thread ',t1.is_alive())
# print('after starting t2 thread ',t2.is_alive())


#ex 5

# def fun1():
#     time.sleep(5)
#     print('surendra')
    
# def fun2():
#     time.sleep(2)
#     print('priyanka')

# t1=Thread(target=fun1)
# t2=Thread(target=fun2)

# print('before starting t1 thread ',t1.is_alive())
# print('before starting t2 thread ',t2.is_alive())

# t1.start()
# t2.start()

# time.sleep(3)
# print('after starting t1 thread ',t1.is_alive())
# print('after starting t2 thread ',t2.is_alive())


#ex 6
def fun1():
    print('surendra')
    time.sleep(15)
    print('thank you ')
    
def fun2():
    time.sleep(2)
    print('priyanka')

t1=Thread(target=fun1)
t2=Thread(target=fun2)

print('before starting t1 thread ',t1.is_alive())
print('before starting t2 thread ',t2.is_alive())

t1.start()
t2.start()

time.sleep(10)
print('after starting t1 thread ',t1.is_alive())
print('after starting t2 thread ',t2.is_alive())