#ques 7
lst=[]
n=int(input("ENTER THE NUMBER OF ELEMENTS:"))
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
def summer_69(lst):
    flag=1
    sum=0
    for i in lst:
        if(i==6):
            flag=0
        if(flag):
            sum=sum+i
        if(i==9):
            flag=1
    return sum
print("SUM IS:")
print(summer_69(lst))
