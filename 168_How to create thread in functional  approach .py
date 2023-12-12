#With out multi thredaing program ( single thread )
'''
def fun1():
    for i in range(5):
        print('surendra')

def fun2():
    for i in range(5):
        print('priyanka')

fun1()
fun2()
'''

# with multithreading 
'''
from threading import * 

def fun1():
    for i in range(5):
        print('surendra')

def fun2():
    for i in range(5):
        print('priyanka')

#create a thread 
t1=Thread(target=fun1)
t1.start()

t2=Thread(target=fun2)
t2.start()
'''

#thread information 
'''
from threading import * 
print('line-38 : ',current_thread().name)
def fun1():
    print('line-40 : ',current_thread().name)
    for i in range(5):
        print('surendra')

def fun2():
    print('line-45 : ',current_thread().name)
    for i in range(5):
        print('priyanka')

#create a thread 
print('line-50 : ',current_thread().name)
t1=Thread(target=fun1)
print('line-52 : ',current_thread().name)
t1.start()
print('line-54 : ',current_thread().name)
t2=Thread(target=fun2)
print('line-56 : ',current_thread().name)
t2.start()
print('line-57 : ',current_thread().name)
'''


#count number of thread

'''
from threading import * 
print('line -65 ',active_count())
def fun1():
    for i in range(5):
        print('surendra')

def fun2():
    for i in range(5):
        print('priyanka')

#create a thread 

t1=Thread(target=fun1)
t1.start()
print('line -78 ',active_count())
t2=Thread(target=fun2)
t2.start()
print('line -81 ',active_count())
'''


# ex 
'''
from  threading import * 

def fun1():
    for i in range(5):
        print('i ',i)

def fun2():
    for j in range(5):
        print('j ',j)


t1=Thread(target=fun1)
t1.start()

fun2()
'''


#thread information 

'''
from  threading import * 

print('line 110 : ',current_thread().name)
def fun1():
    print('line 112 : ',current_thread().name)
    for i in range(5):
        print('i ',i)

def fun2():
    print('line 117 : ',current_thread().name)
    for j in range(5):
        print('j ',j)


t1=Thread(target=fun1)
t1.start()
print('line 124 : ',current_thread().name)
fun2()
'''


#ex 
# pass argument 
'''
from threading import *

def fun1(name):
    for i in range(5):
        print(name)
    
def fun2(name):
    for i in range(5):
        print(name)

t1=Thread(target=fun1,args=('surendra',))
t1.start()

fun2('priyanka')

'''


#ex 
# pass argument 
from threading import *

def fun1(name,addr):
    for i in range(5):
        print(f'{name } {addr}')
    
def fun2(name,addr):
    for i in range(5):
        print(f'{name } {addr}')
        

t1=Thread(target=fun1,kwargs={'name':'surendra','addr':'bbsr'})
t1.start()

fun2('priyanka','ctc')

