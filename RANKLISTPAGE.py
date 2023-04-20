# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    if x%25!=0 :
        print((x//25) + 1)
    else :
        print(x//25)