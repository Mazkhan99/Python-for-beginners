b=int(input())
e=int(input())
def pow(b,e):
    if e==0:
        return 1
    else:
        return b*pow(b,e-1)
print(pow(b,e))
