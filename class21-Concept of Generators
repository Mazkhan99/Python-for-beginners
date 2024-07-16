""" Generators """
# a=[]
#     for i in range(1,100):
#         a.append(i==2)
#     for x in a:
#         print(x)

def generate_squares(n):
    return [i**2 for i in range(1,n)]
for x in generate_squares(100):
    print(x)
"""
The thing is that it is doing eager loading
first calculating then storing
"""

#Lazy Loading
'''
We use yeild keyword for lazy loading
'''

def generate_squares(n):
    for i in range(1,n):
        yield i**2

""" whatever value is infront of it , it will give away the control to the parent toexecute the code of its own"""

for i in generate_squares(100000000000):
    print(i)
#calculating single square at a time and giving away the control to the for loop
#yield uses iteration protocol
#iteration protocol is such a beautiful API

def func():
    print("start")
    yield 1
    print("yielded 1")
    yield 2
    print("yielded 2")
it=iter(func())
next(it)

print("Hello")
for i in range(100000000000):
    pass
print("World")

def func():
    for i in range(10000000000000):
        pass
    print("ended")

from time import sleep
def func():
    print("start")
    yield
    sleep(5)
    print("ended")

print("hello")
it=iter(func())
next(it)
print("world")
next(it)


def generate_squares(n):
    for i in range(1,n):
        yield i**2
a=generate_squares(10)
print(type(a)) #generator

########################################################################
a=(i**2 for i in range(10)) #It is a generator which returns a generator
'''
There is no tuple comprehension in python
'''
for i in a:
    print(i)
'''Generator is nothing but an iterator'''

a=generate_squares(10)
next(a)

a=(i**2 for i in range(10))
print(iter(a))
print(a)

a=(i**2 for i in range(10))
print(next(a))
print(next(a))
