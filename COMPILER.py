# cook your dish here
for _ in range(int(input())):
    s=input()
    m=0
    c=0
    for i in range(len(s)):
        if s[i]=="<":
            m+=1 
        else:
            m-=1 
        if m==0:
            c=i+1 
        elif m<0:
            break
    print(c)