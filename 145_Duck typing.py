#duck typing

# a=23
# print(a)
# print(type(a))

# a=23.45
# print(a)
# print(type(a))

# a="surendra"
# print(a)
# print(type(a))


# object ( methods )

# class A:
#     def mt1(self):
#         print('A-mt1')

# class B:
#     def mt1(self):
#         print('B-mt1')

# class C:
#     def mt1(self):
#         print('C-mt1')

# def display(x):
#     x.mt1()

# a=A()
# display(a)
# b=B()
# display(b)
# c=C()
# display(c)



#-------------

class A:
    def mt1(self):
        print('A-mt1')

class B:
    def mt1(self):
        print('B-mt1')

class C:
    pass

def display(x):
    x.mt1()


c=C()
display(c)