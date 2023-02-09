# cook your dish here
# cook your dish here
for tc in range(int(input())):
    N = int(input())
    a = list(map(int, input().split()))
    Count = {}
    for item in a:
        Count[item] = a.count(item)
    no = []
    for i in Count:
        no.append(Count[i])
    no.sort()
    max = no[-1]
    elem = []
    for i in Count:
        if Count[i] == max:
            elem.append(i)
    elem.sort()
    print(elem[0], " ", max)