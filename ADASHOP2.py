# cook your dish here
# cook your dish here
for _ in range(int(input())):
    r0,c0=map(int,input().split())
    l=[]
    
    if r0==c0 and r0!=1:
        l.append((1,1))
    elif r0 != c0 :
        q=(r0+c0)//2
        l.append((q,q))
        l.append((1,1))

    l.append((2,2))
    l.append((1,3))
    l.append((3,1))
    l.append((4,2))
    l.append((1,5))
    l.append((5,1))
    l.append((6,2))
    l.append((1,7))
    l.append((7,1))
    l.append((4,4))
    l.append((5,5))
    l.append((2,8))
    l.append((8,2))
    l.append((7,3))
    l.append((8,4))
    l.append((4,8))
    l.append((5,7))
    l.append((6,8))
    l.append((8,6))
    l.append((7,7))
    l.append((8,8))
    print(len(l))
    for ele in l:
        print(ele[0],ele[1])
