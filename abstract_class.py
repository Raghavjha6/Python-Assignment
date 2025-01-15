from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def func1(self):
        pass
class B(A):
    def func1(self):
        print('Body of the func1')
    def func2(self):
        print('Body of the func2')
ob1=B()
ob1.func1()
ob1.func2()
