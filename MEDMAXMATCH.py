# cook your dish here
for i in range(int(input())):
    n = int(input())
    A = sorted(list(map(int,input().split())))
    B = sorted(list(map(int,input().split())))
    #the first n//2 couples should be as unhappy as possible
    # top n-n//2 couples should be as homogenous as possible so mix the least happy boy with most happy girl etc to form a list. sort the list and the least happy in the list will be the number.
    C = []
    for i in range(n//2,n):
        j = n-(i-n//2)-1
        C.append(A[i]+B[j])
    C = sorted(C)
    print(C[0])
    