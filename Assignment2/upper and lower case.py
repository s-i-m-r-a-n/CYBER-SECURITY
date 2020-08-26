s=input("ENTER THE STRING:")
l,u=0,0
for i in s:
    if(i.isupper()):
        u=u+1
    elif(i.islower()):
        l=l+1
print("NUMBER OF UPPER CHARACTERS IS %d"%(u))
print("NUMBER OF LOWER CHARACTERS IS %d"%(l))
