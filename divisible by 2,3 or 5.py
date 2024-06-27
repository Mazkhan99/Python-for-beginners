sum=0
for i in range(1,20):
    if i%2==0 or i%3==0 or i%5==0:
        print("")
    else:
        print(i)
        sum+=i
print("sum",sum)