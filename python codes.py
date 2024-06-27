a = input('enter first num : ')
o = input('enter operator (+,-,*,/) : ')
b = input('enter second num : ')
# for sum
if o == "+" :
    print(int(a)+int(b))
# for substraction
elif o == "-" :
    print(int(a)-int(b))
# for multiplication
elif o == "*" :
    print(int(a)*int(b))
# for divide
elif o == "/" :
    print(int(a)/int(b))
else :
    print('invalid operator')g