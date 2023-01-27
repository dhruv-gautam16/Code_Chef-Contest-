# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    patients = []
    for i in range(n):
        patients.append((a[i],n-i))
    #print(patients)
    patients.sort(reverse=True)
    #print(patients)
    wait = [0 for i in range(n)]
    for j in range(n):
        p = patients[j]
        wait[n-p[1]] = j+1
    print(*wait)
        