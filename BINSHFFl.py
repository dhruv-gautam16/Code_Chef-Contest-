# cook your dish here
for z in range(int(input())):
    a,b=(int(x) for x in input().split())
    if(a==b):
        print('0')
    elif(b==1 and a==0):
        print('1')
    elif(b==1 or b==0):
        print('-1')
    else:
        c1=b-1
        bib=bin(c1)[2:]
        bia=bin(a)[2:]
        a1=bia.count('1')
        b1=bib.count('1')
        if(a1==b1):
            print('1')
        elif(a1<b1):
            print(b1-a1+1)
        else:
            print("2")