# cook your dish here
n=int(input())
while(n):
    n=n-1
    a,b = map(int,input().split())
    a = str(bin(a))
    b = str(bin(b))
    count = 0 
    for i in range(0,min(len(a),len(b))):
        if a[i]!=b[i]:
            break
        else:
            count+=1
    dist = len(a)+len(b)-2*count
    print(dist)