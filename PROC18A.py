# cook your dish here
for i in range(int(input())):
    (a,b)=map(int,input().split())
    t=[int(a)for a in input().split()]
    sum1=[]
    for j in range(0,len(t)-1):
            sum1.append(sum(t[j:j+b]))
    print(max(sum1))
            