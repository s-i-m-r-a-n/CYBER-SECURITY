#ques 3
s=str(input("ENTER THE STRING: "))
def rev(s):
    st= s.split()
    st.reverse()
    strev = ' '.join(st)
    return strev
print(rev(s))
