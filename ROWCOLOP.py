
n, q = map(int,(input().split()))
if(n<1 or n>314159 or q<1 or q>314159): exit()
rows = [0 for i in range(n)]
cols = [0 for i in range(n)]
for i in range(q):
    ins = input().split()
    p = int(ins[2])
    s= int(ins[1])
    if(p<1 or p>3141 or s<1 or s>n):exit()
    if(ins[0]=='RowAdd'):
            rows[s-1] += p
    else:
            cols[s-1] += p
    #print(arr)
print(max(rows)+max(cols))