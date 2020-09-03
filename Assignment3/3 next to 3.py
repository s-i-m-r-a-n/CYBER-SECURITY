#ques 5
lst=[]
n=int(input("ENTER THE NUMBER OF ELEMENTS:"))
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
def has_33(lst):
    for i in range(0,n):
        if(lst[i]==3 and lst[i+1]==3):
            return True
            break
    return False
if(has_33(lst)==True):
    print("True")
else:
    print("False")
