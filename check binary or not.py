bin=str(input())
a='01'
def checkbin(bin):
    for i in bin:
        if i in a:
            return True
        elif i not in a:
            return False 
            break
        else:
            return 
print(checkbin(bin))