# cook your dish here
for _ in range(int(input())):
    DS,DT,D=map(int,input().split())
    print(float(max(0,D-DS-DT,DS-D-DT,DT-DS-D)))