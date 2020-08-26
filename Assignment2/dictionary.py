def isPrime(num):
    for i in range(2,num):  
       if (num % i) == 0:  
           return False
    else:
       return True

limit = int(input("Enter limit: "))
numbers = {}
for i in range(2,limit+1):
    if(isPrime(i)):
        numbers.update({i:"Prime"})
    else:
        numbers.update({i:"NonPrime"})

numbers ={key:val for key,val in numbers.items() if val == 'Prime'}

print("Count of primes in limit:",len(numbers))
