data1=input("data1: ")
data2=input("data2: ")
l1=data1.split(",")
l2=data2.split(",")
str1='{'
if len(l1)!=len(l2):
	print("lists are different lengths")
	exit()
else:
	for i in range(len(l1)):
		str1=str1+"'"+l1[i]+"'"+":"+"'"+l2[i]+"'"+","
print(str1[0:len(str1)-1]+"}")
