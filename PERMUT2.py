n = int(input())
while(n != 0):
    li = [int(i) for i in input().split()]
    li1 = list('0' * len(li))
    for i in range(len(li)):
        li1[li[i] - 1] = i + 1
    if(li == li1):
        print("ambiguous")
    else:
        print("not ambiguous")
    n = int(input()) 