a=int(input())
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
for i in range(1,a+1):
    for k in range(1,a+1-i):
        print(k,end="")
    print()