a=int(input("enter first number: "))
b=int(input("enter second number: "))
o=int(input("enter operator number: "))
if o==1:
    print("sum=",a+b)
elif o==2:
    print("subtraction=",a-b)
elif o==3:
    print("multiplication=",a*b)
elif o==4:
    print("division=",a/b)
else:
    print("unexpected operator")
