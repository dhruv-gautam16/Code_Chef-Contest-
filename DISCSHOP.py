# cook your dish here
t=int(input())
for _ in range(t):
    n=input()
    a=''
    i=0
    while(i<=len(n)-2):
        if n[i]>n[i+1]:
            break
        else:
            a+=n[i]
        i+=1 
    j=i+1 
    while(j<=len(n)-1):
        a+=n[j]
        j+=1
    print(int(a))