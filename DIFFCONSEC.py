t=int(input())
for i in range(0,t):
    n=int(input())
    s=input()
    count=0
    for i in range(0,n-1):
        if(s[i]==s[i+1]):
            count=count+1
    print(count)