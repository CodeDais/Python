#create thread in object oriented approach
from threading import *

#by using single thread
'''
class Test:
    def m1(self):
        for i in range(5):
            print('surendra')

    def m2(self):
        for i in range(5):
            print('priyanka')

ob=Test()
ob.m1()
ob.m2()
'''

# by using multithredaing 

'''
class Test:
    def m1(self):
        for i in range(5):
            print('surendra')

    def m2(self):
        for i in range(5):
            print('priyanka')

ob=Test()

t1=Thread(target=ob.m1)
t1.start()
t2=Thread(target=ob.m2)
t2.start()
'''


# pass argument 

class Test:
    def m1(self,name):
        for i in range(5):
            print(name)

    def m2(self,name):
        for i in range(5):
            print(name)

ob=Test()

t1=Thread(target=ob.m1,args=('surendra',))
t1.start()
t2=Thread(target=ob.m2,args=('priyanka',))
t2.start()