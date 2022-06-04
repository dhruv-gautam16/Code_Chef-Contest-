score_list=[]
wick_list=[]
flag=0
n=int(input(""))
for _ in range(n):
    r,w=map(int, input("").split())
    score_list.append(r)
    wick_list.append(w)
    

for i in range(n-1):
    if(score_list[i]>score_list[i+1]) or (wick_list[i]>wick_list[i+1]):
        flag=1
        break
    elif wick_list[i]==wick_list[i+1]==10 and score_list[i]!=score_list[i+1]:
        flag=1
        break
    else:
        flag=0
if flag==1:
    print("NO")
else:
    print("YES")