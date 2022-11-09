# cook your dish here
for i in range(int(input())):
    k=int(input())
    p=0 
    if k < 21:
        print("NO")
    else:
        for l in range(2,k):
            p=p+l
            if p >= k:
                print("YES")
                break
            
            
            
        