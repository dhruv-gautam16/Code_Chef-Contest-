for t in range(int(input())):
    s=input()
    q=[]
    for i in list(s):
        q.append(s.count(i))
    if max(q)>1:
        print("yes")
    else:
        print("no")
