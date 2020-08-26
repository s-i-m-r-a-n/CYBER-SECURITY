n=int(input("INPUT:"))
fr=0
nx=1
sm=0
for i in range(0,n):
    sm=fr+nx
    print(nx,end=" ")
    fr=nx
    nx=sm
