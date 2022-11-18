# cook your dish here
def fun(s1,s2):
    l=list(s1)
    x=1
    for i in s2:
        if i not in l:
            return False
    return True

s1=input()
for _ in range(int(input())):
    s2=input()
    if fun(s1,s2)==True:
        print("Yes")
    else:
        print("No")
    