#active_count() function 

from threading import *
import time

#ex 1

'''
def fun1():
    print('i m fun1')

def fun2():
    print('i m fun2')


t1=Thread(target=fun1)
t2=Thread(target=fun2)

print('no. of active thread : ',active_count())

t1.start()
t2.start()

'''


#ex 2 

'''
def fun1():
    time.sleep(5)
    print('i m fun1')

def fun2():
    print('i m fun2')


t1=Thread(target=fun1)
t2=Thread(target=fun2)

t1.start()
t2.start()

time.sleep(3)

print('no. of active thread : ',active_count())
'''

# ex 3 

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

time.sleep(3)

print('no. of active thread : ',active_count())
'''


# ex 4 

'''
def fun1():
    time.sleep(5)
    print('i m fun1')

def fun2():
    time.sleep(7)
    print('i m fun2')


t1=Thread(target=fun1)
t2=Thread(target=fun2)

t1.start()
t2.start()

time.sleep(3)

print('no. of active thread : ',active_count())
'''

#ex 5 

'''
def fun1():
    print('start-fun1')
    time.sleep(2)
    print('stop-fun1')

def fun2():
    print('start-fun2')
    time.sleep(2)
    print('stop-fun2')


t1=Thread(target=fun1)
t2=Thread(target=fun2)

t1.start()
t2.start()

print('no. of active thread : ',active_count())

'''

# ex 6

def fun1():
    print('start-fun1')
    time.sleep(2)
    print('stop-fun1')

def fun2():
    print('start-fun2')
    time.sleep(2)
    print('stop-fun2')


t1=Thread(target=fun1)
t2=Thread(target=fun2)

t1.start()
t2.start()

print('no. of active thread : ',active_count())
time.sleep(5)
print('no. of active thread : ',active_count())

