# cook your dish here
T=int(input())
for i in range (T):
    N=int(input())
    A=list(map(int,input().split()))
    odd_places=0
    even_places=0
    if N%2==0:
        odd_places+=N//2
        even_places+=N//2
    else:
        odd_places+=(N//2)+1
        even_places+=(N//2)
    odd_nos=0
    even_nos=0
    for j in range (N):
        if A[j]%2==0:
            even_nos+=1
        else:
            odd_nos+=1
    print((min(even_nos,odd_places))+(min(odd_nos,even_places)))