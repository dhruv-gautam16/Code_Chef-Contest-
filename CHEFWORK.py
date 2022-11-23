# cook your dish here
# cook your dish here
test = int(input())

Listc = list(map(int,input().split()))
Listw = list(map(int,input().split()))
mini1 = mini2 = mini3 = 100000
for i in range(test):
    if(Listw[i] == 1):
        if(mini1 > Listc[i]):
            mini1 = Listc[i]
    elif(Listw[i] == 2):
        if(mini2 > Listc[i]):
            mini2 = Listc[i]    
    else:
        if(mini3 > Listc[i]):
            mini3 = Listc[i] 
if(mini1 + mini2 >= mini3):
    print(mini3)
else:
    print(mini2+mini1)
                
                
                
                
    