class A:
    def _init_(self,character):
        self.character=character

    def char(self):
        print(character.lower())
        

class B(A):
    def _init_(self,character):
        self.character=character

    def char(self):
        print(ord(character))

    def char1(self):
        print(character.upper())

character=input()
obj1=A
obj2=B
if len(character)==1 and character.isalpha()==True:
    obj1.char(character)
    obj2.char(character)
    obj2.char1(character)
elif character.isalpha()==False:
    print("Invalid")
    obj2.char(character)
else:
    print("Invalid")