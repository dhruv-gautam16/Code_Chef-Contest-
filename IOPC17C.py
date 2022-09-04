# cook your dish here
for _ in range(int(input())):
    n=int(input())
    nli=list(map(int,input().split()))
    mx=max(nli)
    min=0
    for a in nli:
        if(a%mx>min):
            min=a%mx
    print(min)