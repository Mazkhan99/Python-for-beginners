  # lets build a Calculator using python

first = input("First enter your no : ")
operator = input("Enter your opretor(+,-,*,%,/) : ")
second = input("Enter your second no : ")

first = int(first)
second = int(second)

if operator == "+":
    print(first + second)

elif operator == "-":
    print(first - second)

elif operator == "*":
    print(first * second)

elif operator == "%":
    print(first % second)

elif operator == "/":
    print(first / second)

else:
    print("Invalid opretion")

print("Thanks for coming...")
