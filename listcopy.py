#cloning using slicing
a = [1, 2, 3, 4, 5]
print("a =", a)
print("b = a[:]")
b = a[:]
print("b =", b)
print("a is b ? :", a is b)
#cloning using list function
a = [1, 2, 3, 4, 5]
print("b = list(a)")
b = list(a)
print("b =", b)
print("a is b ? :", a is b)
print("a[0] = 100 ")
a[0] = 100
print("a =", a)
print("b =", b)
#cloning using copy method
a = [1, 2, 3, 4, 5]
print("a =", a)
print("b = a.copy()")
b = a.copy()
print("b =", b)
print("a is b ? :", a is b)

