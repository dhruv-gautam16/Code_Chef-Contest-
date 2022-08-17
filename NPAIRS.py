# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = str(input())
    c=0
    for i in range(n):
        j = i+1
        while j <= min(i+9,n-1):
            if j-i == abs(int(s[j])-int(s[i])):
                c+=1
            j+=1
    
    print(c)