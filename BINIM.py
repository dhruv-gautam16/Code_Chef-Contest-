
# cook your dish here
t = int(input())
for _ in range(t):
    (n,s) = map(str,input().split())
    stacks = []
    for _ in range(int(n)):
        b = str(input())
        stacks.append(b)
    ones = 0
    zeros = 0
    for nim in stacks:
        if nim[0]=='0':
            zeros+=nim.count('0')
        elif nim[0]=='1':
            ones+=nim.count('1')
    #print(ones,zeros)
    if ones>zeros: print("Dum")
    elif zeros>ones: print("Dee")
    elif ones==zeros:
        if s=="Dum":print("Dee")
        elif s=='Dee':print("Dum")