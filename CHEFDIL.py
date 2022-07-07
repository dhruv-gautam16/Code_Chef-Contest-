t=int(input())
for k in range(t):
    s=str(input())
    cnt=0
    for m in range(0,len(s)):
        if s[m]=='1':
            cnt+=1 
    if(cnt%2==1):
        print("WIN")
    else:
        print("LOSE")
        