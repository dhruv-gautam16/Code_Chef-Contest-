# cook your dish here
for _ in range(int(input())):
    S,SG,FG,D,T=map(int,input().split())
    Sother=S+(180*D)/T
    # print(Sother)
    if abs(SG-Sother)<abs(FG-Sother):
        print("SEBI")
    elif abs(SG-Sother)==abs(FG-Sother):
        print("DRAW")
    else:
        print("FATHER")
