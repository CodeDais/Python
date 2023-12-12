from threading import *
import os
#process id 
'''
def fun1():
    print('hi i m fun1')

fun1()
print(os.getpid())
'''

#thread id 

def fun1():
    print('hi i m fun1')


t1=Thread(target=fun1)
print('t1 thread id is : ',t1.ident) #None 
t1.start()
print('t1 thread id is : ',t1.ident)

t2=Thread(target=fun1)
print('t2 thread id is : ',t2.ident)#None 
t2.start()
print('t2 thread id is : ',t2.ident) 
