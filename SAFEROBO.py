t=int(input())
for i in range(t):
    s=input()
    sa,sb=map(int,input().split())
    posa=s[0]
    posb=s[0]
    for j in range(len(s)):
        if s[j]=='A':
            posa=j
        if s[j]=='B':
            posb=j
    disAB=posb-posa
    if(disAB%(sa+sb)==0):
        print("unsafe")
    else:
        print("safe")
    
        
            
