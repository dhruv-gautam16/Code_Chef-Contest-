# cook your dish here
test_cases = int(input())
for i in range(test_cases):
    U, V, A, S = map(int, (input().split()))
    if U == V:
        print("Yes")
    else:
        k = (U**2-2*A*S)
        if k<=V**2:
            print("Yes")
        else:
            print("No")

