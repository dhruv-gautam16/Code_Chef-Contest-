for i in range(int(input())):
    a=int(input())
    arr=list(map(int,input().split()))
    c=0
    if a==1:
        print(0)
    else:
        for i in range(a):
            for j in range(i+1,a):
                if arr[i]&arr[j]==arr[i]:
                    c+=1
        print(c)