vowels=['a','e','i','o','u']
for i in range(int(input())):
    count=0
    a=int(input())
    s=list(input())
    i=0
    for j in range(a-1):
        if s[j] not in vowels and s[j+1] in vowels:
            count+=1 
        else:
            pass
    print(count)