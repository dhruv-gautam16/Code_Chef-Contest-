# cook your dish here
# cook your dish here
n=int(input())
v="party"
for i in range(n):
    l=input()
    if v in l:
        r=l.replace('party','pawri')
        print(r)
    else:
        print(l)