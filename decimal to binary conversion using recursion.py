x=int(input())
def Bin(x):
    if x==0:
        return 0
    else:
        return x%2 + 10*Bin(x//2)
print(Bin(x))
