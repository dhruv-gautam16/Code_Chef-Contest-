# cook your dish here
def solve(days_list,pro_list,di,ri):
    ans=0
    n=len(days_list)
    for i in range(n):
        if di<days_list[i]:
            break
        else:
            ans+=pro_list[i]
    if ans>=ri:
        print("Go Camp")
    else:
        print("Go Sleep")
    
    
for _ in range(int(input(""))):
    days_list=[]
    pro_list=[]
    for a in range(int(input(""))):
        d,p=map(int,input("").split())
        days_list.append(d)
        pro_list.append(p)
    for b in range(int(input(""))):
        di,ri=map(int,input("").split())
        solve(days_list,pro_list,di,ri)
