# cook your dish here
for i in range(int(input())):
    s=list(input())
    k=["A","D","O","P","Q","R"]
    p=['B']
    count=0
    for i in s:
        if i in k:
            count+=1
        elif i in p:
            count+=2
    print(count)
