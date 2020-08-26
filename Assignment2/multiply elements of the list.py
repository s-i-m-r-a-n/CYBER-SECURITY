lst = []
n = int(input("ENTER NUMBER OF ELEMENTS: ")) 
def mul(lst):
    result=1
    for i in lst: 
        result = result * i 
    return result
for i in range(0, n): 
    lst.append(int(input()))
print("MULTIPLICATION OF ELEMENTS OF LIST IS:")
print(mul(lst)) 
