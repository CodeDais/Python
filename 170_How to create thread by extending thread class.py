#creation of thread by extending thread class

from threading import * 

# class Test1(Thread):
#     def run(self):
#         for i in range(5):
#             print('surendra')

# class Test2(Thread):
#     def run(self):
#         for i in range(5):
#             print('priyanka')

# ob1=Test1()
# ob1.run()

# ob2=Test2()
# ob2.run()


#with multithredaing 

# class Test1(Thread):
#     def run(self):  # override run() method 
#         for i in range(5):
#             print('surendra')

# class Test2(Thread):
#     def run(self): # override run() method 
#         for i in range(5):
#             print('priyanka')

# ob1=Test1()
# ob1.start()

# ob2=Test2()
# ob2.start()




# ex : creation of thread by extending thread class with constructor
# passing argument 

class Test1(Thread):
    def __init__(self,name): # overridng thread class constructor 
        Thread.__init__(self) #calling parent clas constructor 
        self.name=name  

    def run(self):
        for i in range(5):
            print(self.name)


class Test2(Thread):
    def __init__(self,name): # overridng thread class constructor 
        Thread.__init__(self) #calling parent clas constructor 
        self.name=name  
    def run(self):
        for i in range(5):
            print(self.name)

ob1=Test1('surendra')
ob1.start()

ob2=Test2('priyanka')
ob2.start()

'''
Note: If a subclass overrides the constructor, it must make sure to invoke the base class constructor (Thread.__init__()) before doing anything else to the thread.
'''