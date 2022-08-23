# cook your dish here
def solve():
    #code here
    n = int(input())
    arr = list(map(int,input().split()))
    s = set(arr)
    
    m = {}
    for i,a in enumerate(arr):
        if a not in m:
            m[a] = []
        m[a].append(i+1)
        
    for a in m:
        count = 0
        for i in m[a]:
            if i in s:
                count+=1
            if count == 2:
                return "Truly Happy"
    
    return "Poor Chef"
            
tc = int(input())
for t in range(tc):
    print(solve())
    