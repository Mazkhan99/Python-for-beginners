a,b,c,d=0,0,0,0
str1=input()
cap='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small='abcdefghijklmnopqrstuvwxyz'
num='0123456789'
sp='@$_'
for i in str1:
    if i in small:
        a+=1
    elif i in cap:
        b+=1
    elif i in num:
        c+=1
    elif i in sp:
        d+=1
if a>=0 and b>=0 and c>=0 and d>=0:
    print("Strong Password")
else:
    print("Not a strong Password")
    