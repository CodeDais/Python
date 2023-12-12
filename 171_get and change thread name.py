#how get thread name 

from threading import * 

'''
def fun1():
    print(current_thread().name) #Thread-1
    for i in range(5):
        print('surendra')

def fun2():
    print(current_thread().name) #Thread-2
    for i in range(5):
        print('priyanka')

t1=Thread(target=fun1)
t1.start()

print(t1.name) #Thread-1


t2=Thread(target=fun2)
t2.start()

print(t2.name) #Thread-2
print(current_thread().name) # to get thread name #MainThread
'''




#how set thread name (approach - 1)
'''
def fun1():
    for i in range(5):
        print('surendra')

def fun2():
    for i in range(5):
        print('priyanka')

t1=Thread(target=fun1,name='mythread1')
t1.start()

print(t1.name) #mythread1

t2=Thread(target=fun2,name='mythread2')
t2.start()

print(t2.name) #mythread2
'''


#how set thread name (approach - 2)

def fun1():
    for i in range(5):
        print('surendra')

def fun2():
    for i in range(5):
        print('priyanka')

t1=Thread(target=fun1)
t1.name='mythread1' #set thread name 
t1.start()
print(t1.name) #mythread1

t2=Thread(target=fun2)
t2.name='mythread2'  #set thread name 
t2.start()

print(t2.name) #mythread2


