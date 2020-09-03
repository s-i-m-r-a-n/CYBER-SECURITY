#ques 8
lst=[]
n=int(input("ENTER THE NUMBER OF ELEMENTS:"))
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
def spy_game(lst):
    for i in range(0,n):
        if(lst[i]==0):
            a=i
            for j in range(a,n):
                if(lst[j]==0):
                    b=j
                    for k in range(b,n):
                        if(lst[k]==7):
                            return True
    return False
if(spy_game(lst)==True):
    print("True")
else:
    print("False")
