# cook your dish here
# cook your dish here
for _ in range(int(input())):
    n,q = map(int,input().split())
    s = input()
    d ={}
    for i in s:
       d[i] = d.get(i,0)+1  
    for i in range(q):
        c = int(input())
        sum=0
        for k,v in d.items():
            if v > c:
                  sum += v-c
        
        print(sum)
