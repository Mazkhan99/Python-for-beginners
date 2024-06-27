a=int(input())
x=""
for i in range(1,a+1):
    x=i*"* "
    print(x)
for i in range(1,a+1):
    x="* "*(a-i)
    print(x)