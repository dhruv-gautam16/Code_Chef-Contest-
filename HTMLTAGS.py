# cook your dish here
for _ in range(int(input())):
    a=str(input())
    output="Success"
    if len(a)<=3:
        output="Error"
    elif a[0]!="<" or a[1]!="/" :
        output="Error"
    elif a[len(a)-1]!=">":
        output="Error"
    else:
        for i in range(2,len(a)-1):
            if not ((a[i]>="a" and a[i]<="z") or (a[i]>="0" and a[i]<="9")):
                output="Error"
    
    print(output)