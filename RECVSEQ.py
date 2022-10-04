# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().split(' ')
    a = [int(i) for i in s]
    d = {}
    if n>4:
        for i in range(1,n):
            if a[i]-a[i-1] in d:
                common_diff = a[i]-a[i-1]
                break
            else:
                d[a[i]-a[i-1]] = True
        point = -1
        flag = 0
        for i in range(1,n-1):
            if a[i]-a[i-1]!=common_diff and a[i+1]-a[i]!=common_diff:
                point = i
                flag = 1
                break
        if flag==1:
            a[point] = a[point+1] - common_diff
        else:
            if a[1]-a[0]!=common_diff:
                point = 0
                a[point] = a[1]-common_diff
            elif a[-1]-a[-2]!=common_diff:
                point = n-1
                a[point] = a[-2]+common_diff
            else:
                point = -1
        print(*a)
    else:
        flag = 0
        for i in range(1,n):
            if a[i]-a[i-1] in d:
                common_diff = a[i]-a[i-1]
                flag = 1
                break
            else:
                d[a[i]-a[i-1]] = True
        if flag==1:
            if a[1]-a[0]!=common_diff:
                point = 0
                a[point] = a[1]-common_diff
            elif a[-1]-a[-2]!=common_diff:
                point = n-1
                a[point] = a[point-1] + common_diff
            else:
                point = -1
        else:
            common_diff = int((a[-1]-a[0])/3)
            a[1] = a[0]+common_diff
            a[2] = a[-1]-common_diff
        print(*a)