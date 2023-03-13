# cook your dish here
for _ in range(int(input())):
    a, b, c = map(int,input().split())
    if a == b == c:
        print(0)
    elif a%2 == b%2 == c%2:
        tog = sorted([a,b,c])
        delt =(tog[2]-tog[0])//2 + (tog[1]-tog[0])//2
        print(delt)
        #print(abs(a-b)+abs(b-c))
    else:
        print(-1)