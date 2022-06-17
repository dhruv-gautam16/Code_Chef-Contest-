for _ in range(int(input())):
    n = int(input())
    a,b = 10**(n-1),10**n
    while a<b:
        if a%3==0 and a%9!=0 and a%2!=0:
            print(a)
            break
        a+=1