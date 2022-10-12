# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    if s=='10':
        print(s)
    else:
        one=s.count('1')
        zero=s.count('0')
        print('0'*zero+'1'*one)
        