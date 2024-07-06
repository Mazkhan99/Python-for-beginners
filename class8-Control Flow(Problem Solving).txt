for i in range(5):
    for j in range(5):
        print(i,end=" ")
    print()

n=int(input())
for i in range(n):
    for j in range(n):
        print(max(max(i+1,j+1),max(n-j,n-i)),end=" ")
    print()
