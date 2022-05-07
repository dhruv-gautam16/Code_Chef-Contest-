# cook your dish here
l=[]
for _ in range(int(input())):
    a1,b1,a2,b2,a3,b3=map(int,input().split())
    l.append(0.5*abs((a1*(b2-b3))+(a2*(b3-b1))+(a3*(b1-b2))))
print(len(l)-l[::-1].index(min(l)),len(l)-l[::-1].index(max(l)))