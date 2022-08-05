# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if(n==2):
        print("0")
    else:
        if(n%2!=0):
            k = n//2 
            p = k+1 
            print(k*p - 1)
        else:
            k = n//2 - 1 
            p = k + 2
            if(k%2!=0 and p%2!=0):
                print(k*p - 1)
            else:
                k = k - 1 
                p = p + 1 
                print(k*p - 1)