# cook your dish here
for t in range(int(input())):
    S=input()
    max_pairs=0
    prev=True
    for i in range(1,len(S)):
        if(S[i]!=S[i-1] and prev):
            prev=False
            max_pairs+=1
        else:
            prev=True
    print(max_pairs)        