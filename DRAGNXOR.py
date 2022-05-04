for _ in range(int(input())):
    n,a,b = map(int,input().split())
    a_one = bin(a).replace('0b','').count('1')
    b_one = bin(b).replace('0b','').count('1')
    max_num = (n-abs(a_one+b_one-n))*'1'+ abs(n-a_one-b_one)*'0'
    print(int(max_num,2))