#ques 9
n=int(input("ENTER THE LIMIT: "))
def count_prime(n):
    n=n+1
    c=0
    for i in range(2,n):
        if(i==2):
            c=c+1
        if(i%2!=0):
            for j in range(2,i):
                if(i%j==0):
                    break
            else:
                c=c+1
    return c
print(count_prime(n))
