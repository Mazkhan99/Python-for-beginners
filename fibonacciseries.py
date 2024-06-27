num1=int(input(""))
num2=int(input(""))
last_num=int(input(""))
for i in range(last_num+1):
    sum=num1+num2
    num1=num2
    num2=sum
    print(sum)