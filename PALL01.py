for t in range(int(input())):
    n=str(input())
    if n==n[::-1]:
        print("wins")
    else:
        print("loses")