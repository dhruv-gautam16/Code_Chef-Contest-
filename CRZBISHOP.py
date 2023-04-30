# cook your dish here
testcase_no=int(input())
for testcases in range(testcase_no):
    n = int(input())
    # a = map(int,input().split())
    # l = list(map(int,input().split()))
    if n!=1:
        print( ((n-1)//2-1) + (n-1) )
    else:
        print(0)