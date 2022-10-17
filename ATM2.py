# cook your dish here
for _ in range ( int(input ())):
    n,k=map(int, input ().split())
    l=list(map(int, input ().split()))
    s=''
    for i in l:
        if k>i or k==i:
            k=k-i
            s+='1'
        else:
            s+='0'
    print (s)