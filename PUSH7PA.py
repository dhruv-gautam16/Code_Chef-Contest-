for _ in range(int(input())):
    n=int(input())
    list1=list(map(int,input().split()))
    counts={}
    for count in list1:
        counts[count] = counts.get(count,0)+1
    flipped = {}
    for key, value in counts.items():
            flipped[key]=key+value-1
    maximum1=max(flipped.values())
    print(maximum1)
    