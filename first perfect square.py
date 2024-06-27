a=int(input())
b=int(input())
for i in range(a,b+1):
    if ( i ** 0.5 == int(i**0.5) and i%2==0 ):
        break
    
    print(i,end=" ")