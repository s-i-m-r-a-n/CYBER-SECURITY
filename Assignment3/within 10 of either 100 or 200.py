#ques 4
import math
n=int(input("ENTER THE NUMBER: "))
def almost_there(n):
    if (abs(100 - n) or abs(200 - n)) <= 10:
        return True
    else:
        return False
if(almost_there(n)==True):
    print("TRUE")
else:
    print("FALSE")
