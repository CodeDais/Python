#join method 

from threading import *
import time


# normal multi threading program
'''
def fun1():
    for i in range(5):
        print('surendra')


t1=Thread(target=fun1)
t1.start()

for i in range(5):
    print('priyanka')
'''


#apply join() method 
'''
def fun1():
    for i in range(5):
        print('Surendra')


t1=Thread(target=fun1)
t1.start()

t1.join()

for i in range(5):
    print('Priyanka')
'''


# ex 

'''
def fun1():
    for i in range(3):
        print('surendra')

def fun2():
    t1.join() # this thraed will execute after execution of t1 thraed
    for i in range(3):
        print('priyanka')

def fun3():
    for i in range(3):
        print('rahul')


t1=Thread(target=fun1)
t2=Thread(target=fun2)
t3=Thread(target=fun3)

t1.start()
t2.start()
t3.start()

'''


#ex

'''
def fun1():
    for i in range(5):
        time.sleep(3)
        print('surendra')

t1=Thread(target=fun1)
t1.start()

t1.join(5) # main thread will wait 5 sec 

for i in range(5):
    print('priyanka')
'''


#ex 



def fun1():
    for i in range(5):
        time.sleep(3) # t1 tread wait 3 sec 
        print('surendra')

t1=Thread(target=fun1)
t1.start()

t1.join(5) # main thread will wait 5 sec 

for i in range(5):
    time.sleep(2) # main thraed will wait 2 sec 


















        