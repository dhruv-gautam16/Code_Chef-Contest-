# cook your dish here
# t = int(input())
# for i in range(t):
#     n = int(input())
#     prime = True
#     if n==1:
#         print("yes")
#     for i in range(2,n):
#         if(n%i==0):
#             prime = False
#             break
        
    # if prime :
    #     print("yes")
    # else:
    #     print("no")
        
for i in range(int(input())):
    a=int(input())
    m=0
    for i in range(1,a+1):
        if (a%i)==0:
            m=m+1
     
    if m==2:
        print("yes")
    else:
        print("no")
