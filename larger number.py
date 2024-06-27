num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())
sum=num1+num2+num3+num4
for i in range(sum):
    if i==num1 or i==num2 or i==num3 or i==num4:
        Large=i
print(Large)