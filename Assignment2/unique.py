lst=[]
n=int(input("ENTER NUMBER OF ELEMENTS: "))
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
new=list(set(lst))
print(new)
