# cook your dish here
for _ in range(int(input())):
    n = int(input())
    emp = []
    count = 0
    for i in range(n):
        emp.append(list(map(int, input().split())))
    while n>1:
        if emp[0][n-1]!=n:
            count+=1
            for i in range(n):
                for k in range(i+1, n):
                    emp[i][k], emp[k][i] = emp[k][i], emp[i][k]
        n-=1
    print(count)