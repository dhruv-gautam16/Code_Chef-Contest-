# cook your dish here
A,B = map(int,input().split(" "))
if A==0 and (B== 0 or B==1):
    print("https://www.codechef.com/practice")
elif (A==0 or A==1) and B==0:
    print("https://www.codechef.com/contests")
else:
    print("https://discuss.codechef.com")