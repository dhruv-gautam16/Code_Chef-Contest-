for _ in range(int(input())):
    n = int(input())
    s = input()
    string = ""
    ans = ""
    t = "abcdefghijklmnopqrstuvwxyz"
    for i in range(0 , n-1 , 2):
        string += s[i+1]
        string += s[i]
    if len(s) % 2 == 1:
        string += s[len(s)-1]
    for i in range(n):
        for j in range(26):
            if string[i] == t[j]:
                ans += t[25-j]
    print(ans)