for i in range(int(input())):
    a=int(input())
    list_a=list(map(int, input().split()))
    set_a=set(list_a)
    if len(set_a)==len(list_a) and len(set_a)%2!=0:
        print("NO")
    else:
        print("YES")