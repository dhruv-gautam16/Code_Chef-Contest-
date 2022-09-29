# cook your dish here
for i in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    flag=0
    for j in range(n-2):
        if a[j]>a[j+1] and  a[j]>a[j+2]:
            print("NO")
            flag =1
            break
    if flag==0:
        print('YES')