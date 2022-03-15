for i in range(int(input())):
    a=str(input())
    b=str(input())
    m=[]
    c=''
    for j in range(len(a)):
        if a[j]==b[j]:
            m.append('G') 
        else:
            m.append('B')
    print(c.join(m))