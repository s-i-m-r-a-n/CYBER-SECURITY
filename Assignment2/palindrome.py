s=input("ENTER THE STRING:")
def pal(str):
    if(str==str[::-1]):
        return True
    else:
        return False
if(pal(s)):
    print("STRING IS PALINDROME")
else:
    print("STRING IS NOT PALINDROME")
