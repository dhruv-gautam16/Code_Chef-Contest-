# cook your dish here
for tc in range(int(input())):
    n=int(input())
    s=input()
    l=["O"]
    for i in s:
        if(l[-1]!=i):
            l.append(i)
    l.remove("O")
    c1=l.copy()
    for i in range(1,len(l)):
        if((l[i-1]=="U" and l[i]=="D")or(l[i-1]=="D" and l[i]=="U"))or((l[i-1]=="R" and l[i]=="L")or(l[i-1]=="L" and l[i]=="R")):
            c1.remove(l[i])
    x=0
    y=0
    for i in c1:
        if(i=="L"):
            x-=1
        elif(i=="R"):
            x+=1
        elif(i=="U"):
            y+=1
        elif(i=="D"):
            y-=1
    print(x,y)