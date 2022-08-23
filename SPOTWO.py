import math
t = int(input())
for case in range(t):
    n = int(input())
    
    
    def N_bin(n):
        return int(bin(n)[2:])
    
    
    
    
    def fastpowmod(thenum):
        guide = str(N_bin(2*N_bin(thenum)))
        tempans = 2
        for l in range(1,len(guide)):
            tempans = tempans**2 % 1000000007
            if guide[l] == "1":
                tempans = tempans*2 % 1000000007
        return tempans

    print(fastpowmod(n))