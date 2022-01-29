import math
p1=0
p2=0
win = 1
max_lead=0
for i in range(int(input())):
    (a,b) = map(int,input().split())
    p1+=a 
    p2+=b 
    if(abs(p1-p2)>max_lead):
        max_lead = abs(p1-p2)
        win = 1 if p1>p2 else 2
print(f"{win} {max_lead}")