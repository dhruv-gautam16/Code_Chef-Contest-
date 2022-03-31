for t in range(int(input())):
    n=int(input())
    length=[int(i)for i in input().split()]
    width=[int(i)for i in input().split()]
    length.sort()
    width.sort()
    sum=0
    for j in range(n):
        sum=sum+min(length[j],width[j])
    print(sum)    