n=int(input())
for i in range(n):
    dict={}
    a=int(input())
    for l in range(a):
        j=int(input())
        if j in dict:
            dict[j]+=1
        else:
            dict[j]=1
    for k in dict:
        if (dict[k]%2==1):
            print(k)
        