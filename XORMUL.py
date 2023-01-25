for _ in range(int(input())):
    N, A, B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        a = bool(A & 1<<i)
        b = bool(B & 1<<i)
        if b == a == True: continue;
        elif b == a == False: ans += pow(2, i)
        elif B > A:
            if B - int(not a)*pow(2, i) != 0:
                if abs(B - int(not a)*pow(2, i) - (A + int(not a)*pow(2, i))) < abs(B - A):
                    ans += int(not a)*pow(2, i); B -= int(not a)*pow(2, i); A += int(not a)*pow(2, i)
        else:
            if A - int(not b)*pow(2, i) != 0:
                if abs(A - int(not b) * pow(2, i) - (B + int(not b) * pow(2, i))) < abs(B - A):
                    ans += int(not b)*pow(2, i); B += int(not b)*pow(2, i); A -= int(not b)*pow(2, i)
    print(ans)