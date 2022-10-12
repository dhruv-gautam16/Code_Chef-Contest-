
def con(d,c):
    l1= [0]*100001
    for i in d:
        l1[i]=1
    return l1


a = int(input())
for a in range(a):
    b =int(input())
    l = list(map(int,input().split(" ")))
    c = int(input())
    d = list(map(int,input().split(" ")))
    l1 = con(d,c)
    for j in range(b):
        if(not l1[l[j]]):
            print(l[j],end=" ")
    print()



















