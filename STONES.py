n=int(input())
for j in range(n):
    str1=input()
    str2=input()
    c=0
    for g in str2:
        if g in str1:
            c+=1
    print(c)