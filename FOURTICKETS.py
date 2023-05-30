# cook your dish here
t=int(input())
for i in range(t):
    tic_cost=int(input())
    four_cost=4*tic_cost
    if four_cost<=1000:
        print("YES")
    else:
        print("NO")