def solve():
    n,k= map(int, input().split())
    string = input()
    c_a=c_b=ab=0
    for i in string:
        if i=='a':
            c_a+=1 
        elif i=='b':
            c_b+=1 
            ab+=c_a             
    print(ab*k + k*(k-1)*c_a*c_b//2)
for _ in range(int(input())):
    solve()