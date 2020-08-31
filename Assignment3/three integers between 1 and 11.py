#ques 6
a = int(input("ENTER a: "))
b = int(input("ENTER b: "))
c = int(input("ENTER c: "))
sum=a+b+c
if a in range(1, 12) and b in range(1, 12) and c in range(1, 12):
    if sum <= 21:
        print(sum)
    else:
        if(a == 11 or b==11 or c==11):
            print(sum-10)
        else:
            print("BUST")
else:
    print("NOT IN RANGE FROM 1-11")
