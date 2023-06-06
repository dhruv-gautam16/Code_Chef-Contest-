# cook your dish here
n=int(input())
for i in range(1,n+1):
    a=int(input())
    z=""
    h=str(input())
    for j in range(0,a,2):
        if(h[j]+h[j+1]=="00"):
            z=z+"A"
        elif(h[j]+h[j+1]=="01"):
            z=z+"T"
        elif(h[j]+h[j+1]=="10"):
            z=z+"C"
        else:
            z=z+"G"
    print(z)