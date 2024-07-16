class A:
    def __init__(self,x):
        self.x=x
class B(A):
    def __init__(self,x,y):
        print("B init executed")

abc=B()

#Python doesn't have a concept of overloading
class A:
    def __init__(self):
        print("A init executed")
class B(A):
    def __init__(self,x,y):
        print("B init executed")
#By design python doesn't have polymorphic functions
#It will replace it by attributes
#init is not a constructor

'''
If we want to call parent class we use super()
'''
class A:
    def __init__(self):
        print("A init executed")
class B(A):
    def __init__(self,x,y):
        print("B init executed")
        super().__init__()
abc=B()

""" MRO  - Method Resolution Order """
class A:
    pass
class B(A): #class B extend from A
    pass
class C(B):
    x=5
class D(A):
    x=10
class E(C,D): #class B extend from C and D
    pass
e=E()
print(e.x) #5

class A:
    x=5
class B(A): #class B extend from A
    pass
class C(B):
    x=5
class D(A):
    x=10
class E(C,D): #class B extend from C and D
    pass
e=E()
print(e.x) #10

# E.mro() --->[__main__.E,__main__.C,__main__.B,__main__.D,__main__.A,object]

"""
RULES:
    DFS---> If there is a loop, solve branches differently
"""

""" ITERATION PROTOCAL """
'''
For any object to be an iterable, it should have 2 dunders
__iter__ ---> return an iterators which helps me iterate over this iterator
__next__ 
'''
a=range(5)
it=a.__iter__()
it.__next__() #0
it.__next__() #1
it.__next__() #2
it.__next__() #3
it.__next__() #4
'''
Stop the iteration
'''

class myrange:
    def __init__(self,n):
        self.n=n
    def __iter__(self):
        return myrange_iterator(self)
class myrange_iterator:
    def __init__(self,myrange):
        self.myrange=myrange
        self.i=0
    def __next__(self):
        ret=self.i
        self.i+=1
        if ret>=self.myrange.n:
            raise StopIteration
        return ret

a=myrange(5)
it=iter(a)
next(it)
