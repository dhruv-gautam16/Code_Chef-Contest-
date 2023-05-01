# cook your dish here
for i in range(int(input())):
        n,x,p=map(int,input().split())
        print("PASS") if (x*3-(n-x))>=p else print("FAIL")