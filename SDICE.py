q=int(input())
for i in range(q):
    n=int(input())
    dic={0:0,1:20,2:36,3:51,4:60}
    if n<=4:
        print(dic[n])
    else:
        a=n%4
        b=n//4
        res=b*44+dic[a]+4*(4-a)
        print(res)