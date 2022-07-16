# cook your dish here
for _ in range(int(input())):
    l = [i for i in input().split()]
    arr = [int(i) for i in input().split()]
    if l[0] == '1' and arr[0]%2 == 0 and l[-1] == 'Dee':
        print('Dee')
    else:
        print('Dum')