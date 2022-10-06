# cook your dish here
t=int(input())
for _ in range(t):
    A,B=input().split()
    A=int(A)
    B=int(B)
    if (A%2!=0 and B%2!=0):
        print("Vanka")
    else:
        print("Tuzik")
    