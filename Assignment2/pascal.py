import math
n=int(input("INPUT: "))
res=0
for i in range(0,n):
    for k in range(0,n-i):
        print(end=" ")
    for j in range(0,i+1):
        res=int((math.factorial(i))/(math.factorial(i-j)*math.factorial(j)))
        print(res,end=" ")
    print("\n")
