t=int(input())
for i in range(t):
    s=input()
    c=0
    for j in range(0,len(s),2):
        if s[j]==s[j+1]:
            c=1
    if c==1:
        print("no")
    else:
        print("yes")