def ibc(a):         #ibc= in the board checker
    if a[0]>0 and a[0]<9 and a[1]>0 and a[1]<9:
        return True
    else:
        return False

def kmove(ll):      #knight moving coordinates
    empty = []
    for L in ll:
        x = [[(L[0]+2), (L[1]+1)],
        [(L[0]+2), (L[1]-1)],
        [(L[0]-2), (L[1]+1)],
        [(L[0]-2), (L[1]-1)],
        [(L[0]+1), (L[1]+2)],
        [(L[0]+1), (L[1]-2)],
        [(L[0]-1), (L[1]+2)],
        [(L[0]-1), (L[1]-2)]]
        empty = empty + x
    final = []
    for i in empty:
        if ibc(i):
            y = [i]
            final = final + y
    return final
    
for _ in range(int(input())):
    ri, ci, rf, cf = map(int, input().split())
    ini, fin =  [[ri, ci]], [rf, cf]
    counter = 1
    for i in range(6):
        check = False
        stage = kmove(ini)
        for j in stage:
            if j==fin:
                check = True
                break
            else:
                continue

        if check:
            break
        else:
            ini = stage
            counter+=1
    if counter%2==0:
        print("YES")
    else:
        print("NO")