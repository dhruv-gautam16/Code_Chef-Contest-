# cook your dish here
n,m = map(int,input().split())
cd = {}
pd = {}
c = {}
for i in range(n):
    chef,country = input().split()
    cd[chef] = country 
for i in range(m):
    name = input()
    pd[name] = pd.get(name,0) + 1 
    co = cd[name]
    c[co] = c.get(co,0) + 1  
c = sorted(c.items(),key = lambda x:(-x[1],x[0]))
pd = sorted(pd.items(),key = lambda x:(-x[1],x[0]))
print(c[0][0])
print(pd[0][0])

