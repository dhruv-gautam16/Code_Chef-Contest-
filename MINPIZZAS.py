# cook your dish here
t =int(input())
for k in range(t):
    n,k = map(int,input().split(" "))
    k_dublicate =k
    n_dublicate =n
    lcm =1
    gcd =1
    while(k):
        n,k=k,n%k
    gcd =n
    lcm = (n_dublicate)//gcd
    
    print(lcm)
        