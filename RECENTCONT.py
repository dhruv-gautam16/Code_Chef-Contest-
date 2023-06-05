# cook your dish here
for i in range(int(input())):
        n=int(input())
        l=list(input().split())
        a=0
        b=0
        for i in l:
                if i=="START38":
                       a+=1
                else:
                        b+=1
        print(a,b)