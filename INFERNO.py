# cook your dish here
k, n = map(int, input().split())
l = []
for i in range(k):
    l.append(input())

for j in range(n):
    c = 0
    s = input()
    if len(s) >= 47:
        print("Good")
        c = 1 
    else : 
        for i in l:
            if i in s:
                print("Good")
                c = 1
                break
    if (c == 0):
        print("Bad")