#ques 1
import string
st=input("ENTER THE STRING: ")
st=st.lower()
ch=''
def pan(st):
    for i in range(97,123):
        ch=chr(i)
        for j in st:
            if(ch==j):
                break
        else:
            print("STRING IS NOT PANGRAM")
            break
    else:
        print("STRING IS PANGRAM")
pan(st)
