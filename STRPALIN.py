n=int(input())
for i in range(n):
    str1,str2=(input(),input())
    x=0
    for j in str1:
        if j in str2:
            x+=1
            print('Yes')
            break
    if x==0:
        print('No')