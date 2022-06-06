def isStable(l):
    for i in range(r):
        for j in range(c):
            cnt=0
            if i+1 < r:
                cnt+=1
            if i-1 >=0:
                cnt+=1
            if j+1 < c:
                cnt+=1
            if j-1 >= 0:
                cnt+=1
            if l[i][j]>=cnt: return False
    return True

t = int(input())
while t:
    r,c = [int(i) for i in input().split()]
    l =[]
    for j in range(r):
        l.append([int(i) for i in input().split()])
    print("Stable") if isStable(l) else print("Unstable")
    #print(isStable(l))
    t-=1