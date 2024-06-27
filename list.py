  # List datatype -- Collection of datatypes...

marks = [ 97 , 78 , 98 ]
print(marks)


marks = [ 97 , 78 , 98 ]
print(marks[0])  # if we have to print indivisual marks...


marks = [ 97 , 78 , 98 ]
print(marks[2])


marks = [ 97 , 78 , 98 ]
print(marks[0:2])

for score in marks:
    print(score)  # use of for lopp  in list datatype

  # List opretions--

 # 1 - append opretions-- its meaning is adding something extra we want to add

marks.append(99)
print(marks)  # we have  to add 99 in marks 

 # innsert opretion -- ager hme khi bich me ane marks ko add kerna hai

marks.insert(0, 99)
print(marks)
print(99 in marks) # in opretion used for checking the existence 
print(len (marks)) # lenth opretion is used for checking the lenth of something

# use of while loop in list

i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1

marks.clear()  # clear opretion is used for clear the list
print(marks)



