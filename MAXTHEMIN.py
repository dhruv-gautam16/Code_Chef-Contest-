# cook your dish here
for _ in range(int(input())):
    a, b = map(int, input().split())
    li = list(map(int, input().split()))
    li.sort(reverse = True)
    if a-b>0:
        print(li[a-b-1])
    else:
        print(max(li))