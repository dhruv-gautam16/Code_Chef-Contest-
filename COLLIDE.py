# cook your dish here
import io, sys, os
input = io.BytesIO(os.read(0, \
         os.fstat(0).st_size)).readline
T = int(input().decode());
d = {"U":0.5, "D":-0.5, "L":-0.5, "R":0.5}
for _ in range(T):
    Xe,Ye,dire = input().decode().split();
    Xe, Ye = int(Xe), int(Ye)
    N=int(input().decode())
    ast = []
    for i in range(N):
        Xa,Ya,dira = input().decode().split();
        Xa, Ya = int(Xa), int(Ya)
        ast.append([Xa,Ya,dira])
    breakouter = False
    for t in range(1,401):
        if(dire=="L" or dire=="R"):
            Xe = Xe + d[dire]
        else:
            Ye = Ye + d[dire]
        for i in ast:
            if(i[2]=="R"):
                i[0]=i[0]+0.5
            elif(i[2]=="L"):
                i[0]=i[0]-0.5
            elif(i[2]=="U"):
                i[1]=i[1]+0.5
            elif(i[2]=="D"):
                i[1]=i[1]-0.5
            if(Xe==i[0] and Ye==i[1]):
                sys.stdout.write(str(t/2)+"\n")
                breakouter = True
                break
        if(breakouter):
            break
    if(breakouter==False):
        sys.stdout.write("SAFE"+"\n")
    