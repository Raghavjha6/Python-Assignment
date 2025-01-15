class A:
    def fun1(self):
        print('This is within class A')
class B(A):
    def fun2(self):
        print('This is within class B')
ob1=A()
ob1.fun1()
ob2=B()
ob2.fun1()
ob2.fun2()
