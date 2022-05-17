output=[]
for _ in range(int(input(""))):
    n=int(input(""))
    list1=list(map(int,input("").split(" ")))
    avg=sum(list1)/n
    flag=1
    count = 0
    if 4.0>avg:
        flag=0
    for a in list1:
        if a<=2:
            flag=0
        if a>=5:
            count+=1
    if count<=0:
        flag=0
    if flag==1:
        output.append("Yes")
    else:
        output.append("No")
for _ in output:
    print(_)