# cook your dish here
for _ in range(int(input())):
    str=input()
    l1=[]
    for ele in str:
        if ele in l1:
            pass
        else:
            l1.append(ele)
    print(len(l1))