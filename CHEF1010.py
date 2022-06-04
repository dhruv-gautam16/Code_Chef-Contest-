t = int(input())
while t:
    n = int(input())
    s = input()
    cnt=0
    mp={'1':0,'0':0}
    for ch in s:
        mp[ch]+=1
    ans = min(mp['1'],mp['0'])
    if ans <2:
        print(0)
    else:
        print(ans-1)
    t-=1
