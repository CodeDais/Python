from threading import *
import time
#enumerate() 
# ex1 

# print(enumerate())


#ex2 

'''
def fun1():
    time.sleep(5)
    print('i m fun1')

t1=Thread(target=fun1)
t1.start()

print(enumerate())
'''


#ex 3

'''
def fun1():
    time.sleep(5)
    print('i m fun1')

def fun2():
    time.sleep(5)
    print('i m fun2')

t1=Thread(target=fun1)
t2=Thread(target=fun2)
t1.start()
t2.start()

print(enumerate())
'''


# ex 4 

'''
def fun1():
    time.sleep(5)
    print('i m fun1')

def fun2():
    time.sleep(5)
    print('i m fun2')

t1=Thread(target=fun1)
t2=Thread(target=fun2)
t1.start()
t2.start()

l=enumerate()

for i in l:
    print(i.name)

'''

#
# ex 5 

def fun1():
    time.sleep(5)
    print('i m fun1')

def fun2():
    time.sleep(5)
    print('i m fun2')

t1=Thread(target=fun1)
t2=Thread(target=fun2)
t1.start()
t2.start()

print(enumerate())

time.sleep(7)

print(enumerate())