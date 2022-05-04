for i in range(int(input())) :
    n,m=map(int,input().split())
    x,y=map(int,input().split())
    li=[]
    fin=[]
    for i in range(n):
        li.append(input())
    for i in range(len(li)):
        if li[i].count('F')>=x or(li[i].count('F')==x-1 and li[i].count('P')>=y) :
            fin.append(1)
        else :
            fin.append(0)
    print(''.join(map(str, fin))) 