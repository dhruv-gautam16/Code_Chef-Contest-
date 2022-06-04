t = int(input())
while t:
    n = int(input())
    a = [i for i in range(1,n+1)]
    for i in range(0,n-1,2):
        temp = a[i]
        a[i]=a[i+1]
        a[i+1]=temp
    if n%2 != 0:
        temp = a[n-2]
        a[n-2]=a[n-1]
        a[n-1]=temp
    for val in a:
        print(val,end=" ")
    print()
    t-=1