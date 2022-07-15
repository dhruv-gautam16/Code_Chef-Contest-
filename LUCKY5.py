# cook your dish here
t = int(input())
for i in range(t):
    n = list(input().strip())
    count=0
    for ch in n:
        if ch != '4' and ch != '7':
            count+=1
    print(count)