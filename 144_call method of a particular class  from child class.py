# class A:
#     def mt1(self):
#         print('A-mt1')

# class B(A):
#     def mt1(self):
#         print('B-mt1')

# class C(A):
#     def mt1(self):
#         print('C-mt1')
#         A.mt1(self)

# class D(B,C):
#     def mt1(self):
#         print('D-mt1')
#         #B.mt1(self) # calling mt1() of  B class
#         #A.mt1(self)

# # d=D()
# # d.mt1()

# c=C()
# c.mt1()


# another
class A:
    def mt1(self):
        print('A-mt1')

class B(A):
    def mt1(self):
        print('B-mt1')

class C(A):
    def mt1(self):
        print('C-mt1')
        super().mt1()

class D(B,C):
    def mt1(self):
        print('D-mt1')
        super().mt1()

d=D()
d.mt1()

c=C()
c.mt1()

