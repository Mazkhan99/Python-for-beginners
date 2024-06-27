a=int(input("Enter starting range: "))
b=int(input("Enter ending range: "))
prime = 0
composite = 0
if a>=0 and a<b:
    for number in range(a,b+1):
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime += 1
        else:
            composite += 1 
    if a==1:
        prime-=1
        composite+=1
    elif a==0:
        prime-=2
        composite+=2
    print("There are",prime,"prime and",composite,"composite numbers in given range")
else:
    print("Enter Valid Range")