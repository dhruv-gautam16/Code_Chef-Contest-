n = int(input())

for i in range(n):
    D = int(input())
    S = input()
    count = 0
    countA = S.count('A')
    countP = S.count('P')
    if D <=4 and (countP <= countA):
        print(-1)
    elif (countP/D)>= 0.75:
        print(count)
    else:
        f = 0
        for i1 in range(2,len(S)-2):
            if S[i1] == 'A' and ((S[i1-2]=='P') or (S[i1-1]=='P')) and ((S[i1+1]=='P') or (S[i1+2]=='P')):
                count += 1
                countP += 1
                if (countP/D)>= 0.75:
                    f = 1
                    break
        if f == 1:
            print(count)
        else:
            print(-1)