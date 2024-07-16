#object
a=5
isinstance(a,object) # ---> True
a+4
isinstance(a,int) # ---> True

def func(): # ---> This statement creates a value and store it in the variable func
    pass
isinstance(func,object) # ---> True

class A:
    name="jatin"
    marks=50

type(A) # ---> Datatype is type for this variable
A=5
type(A) # ---> int  

class A:
    def __call__(self):
        print("You called me")

a=A()
type(a) # __main__.A
a() # You called me

b=A.__call__()
b=A()

def func():
    print("Hello") # ---> Hello
func()
func.__call__() # ---> Hello

def say_hi(self):
    print(self.name)
    self.name="anonymous"

for i in range(5):
    print(i)
#Even for for loop there is dunders

a={"name":"Jatin"}
# a{"name"} --->'Jatin'
a.__getitem__("name") # --->'Jatin'

class Exponent:
    def __init__(self,n):
        self.n=n
    def __getitem__(self,x):
        return x**self.n
e=Exponent(3)
e[6] # --->216

class A:
    name="Jatin"
    def __init__(self,n):
        self.n=n
a=A(2)
a.name # --->"Jatin"
a.n # ---> 2


class Dog:
    kind='canine'
    def __init__(self,name):
        self.name=name
a=Dog("Maxx")
a.name # ---> 'Maxx'
a.kind # ---> 'canine'


class Dog:
    tricks=[]
    def __init__(self,name):
        self.name=name
    def add_tricks(self,trick):
        self.tricks.append(trick)
d1=Dog("Maxx")

d1.add_tricks("fetch")
d1.add_tricks("talk")
d1.tricks # ['fetch','talk']
d2=Dog("Bella")
d2.tricks # ['fetch','talk']

# a=[]
# b=a
# b.append(1)
#Ultimately we are appending on a
