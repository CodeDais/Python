from threading import *
import time

#ex1 
#check Main Thread is a daemon thread or not 
# print('Main Thread is daemon : ',current_thread().daemon)



#ex2 

# def fun1():
#     for i in range(5):
#         print(i)
#         time.sleep(1)

# t1=Thread(target=fun1)
# print('t1 thread is daemon : ',t1.daemon)
# t1.start()


# #ex3 

# #set t1 thread as daemon thread

# def fun1():
#     for i in range(5):
#         print(i)
#         time.sleep(1)

# t1=Thread(target=fun1,daemon=True)
# print('t1 thread is daemon : ',t1.daemon)
# t1.start()
# print('End of Main Thread Execution')


#ex4


# def fun1():
#     for i in range(5):
#         print(i)
#         time.sleep(1)

# t1=Thread(target=fun1,daemon=True)
# print('t1 thread is daemon : ',t1.daemon)
# t1.start()
# time.sleep(2)
# print('End of Main Thread Execution')


#ex 5 
# def fun1():
#     for i in range(5):
#         print(i)
#         time.sleep(1)

# t1=Thread(target=fun1)
# print('t1 thread is daemon : ',t1.daemon)
# t1.start()
# time.sleep(2)
# print('End of Main Thread Execution')



#ex 6

# def fun1():
#     for i in range(5):
#         print('hi')
#         time.sleep(1)
#     t2=Thread(target=fun2)
#     t2.start()


# def fun2():
#     for i in range(5):
#         print('hello')
#         time.sleep(1)

# t1=Thread(target=fun1,daemon=True)
# print('t1 thread is daemon : ',t1.daemon)
# t1.start()
# time.sleep(10)
# print('End of Main Thread Execution')



#ex 7 

# def fun1():
#     for i in range(5):
#         print('hi')
#         time.sleep(1)
#     t2=Thread(target=fun2)
#     t2.start()


# def fun2():
#     for i in range(5):
#         print('hello')
#         time.sleep(1)

# t1=Thread(target=fun1,daemon=True)
# print('t1 thread is daemon : ',t1.daemon)
# t1.start()
# time.sleep(5)
# print('End of Main Thread Execution')



#ex 8

# def fun1():
#     for i in range(5):
#         print('hi')
#         time.sleep(1)
#     t2=Thread(target=fun2)
#     t2.start()


# def fun2():
#     for i in range(5):
#         print('hello')
#         time.sleep(1)

# t1=Thread(target=fun1,daemon=True)
# print('t1 thread is daemon : ',t1.daemon)
# t1.start()
# time.sleep(7)
# print('End of Main Thread Execution')

#ex 9

# def fun1():
#     for i in range(5):
#         print('hi')
#         time.sleep(1)
#     t2=Thread(target=fun2)
#     t2.start()


# def fun2():
#     for i in range(5):
#         print('hello')
#         time.sleep(1)

# t1=Thread(target=fun1,daemon=True)
# print('t1 thread is daemon : ',t1.daemon)
# t1.start()
# time.sleep(3)
# print('End of Main Thread Execution')


#ex 10 

# def fun1():
#     for i in range(5):
#         print('hi')
#         time.sleep(1)
#     t2=Thread(target=fun2)
#     t2.start()
#     print('t2 thread is daemon : ',t2.daemon)

# def fun2():
#     for i in range(5):
#         print('hello')
#         time.sleep(1)

# t1=Thread(target=fun1,daemon=True)
# print('t1 thread is daemon : ',t1.daemon)
# t1.start()
# time.sleep(10)
# print('End of Main Thread Execution')


#ex 11

# def fun1():
#     for i in range(5):
#         print('hi')
#         time.sleep(1)
#     t2=Thread(target=fun2,daemon=False)
#     t2.start()
#     print('t2 thread is daemon : ',t2.daemon)

# def fun2():
#     for i in range(5):
#         print('hello')
#         time.sleep(1)

# t1=Thread(target=fun1,daemon=True)
# print('t1 thread is daemon : ',t1.daemon)
# t1.start()
# time.sleep(7)
# print('End of Main Thread Execution')


# some more example 
#ex 12
# ask name to the user and check how much time user 
# taken to give his/her name 

# def sec_count():
#     sec=0
#     while True:
#         time.sleep(5)
#         sec=sec+5
#         print(f'i m waiting since {sec} sec ')

# t1=Thread(target=sec_count,daemon=True)
# t1.start()

# name=input('enter your name : \n')



#ex 13 

# tradition apporach 
#isDaemon() -> used to check a thread is daemon thred or not

# print("Main Thread is daemon : ",current_thread().isDaemon())
#This method is deprecated, use the daemon attribute instead


#setDaemon()

# def fun1():
#     for i in range(5):
#         print('hi')
#         time.sleep(1)

# t1=Thread(target=fun1)
# t1.setDaemon(True) #DeprecationWarning: setDaemon() is deprecated, set the daemon attribute instead
# t1.start()


# note : once a thread started, then we cant change it nature 


# def fun1():
#     for i in range(5):
#         print('hello')
#         time.sleep(1)

# t1=Thread(target=fun1)
# t1.start()
#t1.daemon=True # t1 thread already started now i m trying to chnage its nature 

# note : RuntimeError: cannot set daemon status of active thread


# we know main thread deafult nature is non daemon 
# can we change its nature 
# ans : no

current_thread().daemon=True #cannot set daemon status of active thread
