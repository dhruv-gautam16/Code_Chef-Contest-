t=lambda x,y:0if x<y else(x-y)//4+int((x-y)%4!=0)
for _ in[I:=input]*int(I()):x,y=map(int,I().split());print(t(x,y))