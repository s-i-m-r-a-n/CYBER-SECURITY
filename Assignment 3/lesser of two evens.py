#ques 2
import math
a=int(input("ENTER THE VALUE OF a: "))
b=int(input("ENTER THE VALUE OF b: "))
def num(a,b):
    if(a%2==0 and b%2==0):
        return True
    else:
        return False
if(num(a,b)==True):
    print(min(a,b))
else:
    print(max(a,b))
