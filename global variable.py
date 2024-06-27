def sum():
    print("inside scope of function")
s="outside function call"
sum()
print(s)
################################################################
def sum():
    global s 
    s = "outside function call"
    print(s)
sum()
################################################################
