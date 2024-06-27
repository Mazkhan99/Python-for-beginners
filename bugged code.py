def test_prime(n):
    if (n==1):
        return 'false'
    elif (n==2):
        return 'true'
    else:
        for x in range(2,n):
            if(n%x==0):
                return 'false'
            else:
                return 'true'
a=int(input())
print(test_prime(a))    