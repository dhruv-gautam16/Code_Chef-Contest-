for _ in range(int(input())):
    N= int(input())
    pare = True
    arr1 = input().split()
    for i in range(N-1):
        if arr1[i]=="cookie":
            if arr1[i+1]=="cookie":pare = False;break;
    if arr1[-1]=="cookie":pare=False;
    if pare:
        print("YES")
    else:
        print("NO");