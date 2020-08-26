n=int(input("ENTER THE LIMIT:"))
l=[]
s=" "
for i in range(2,n+1):
    for j in range(2,i):
        if(i%j==0):
            l.append((i,"NOT PRIME"))
            break
    else:
        l.append((i,"PRIME"))
print(l)
