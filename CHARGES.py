import math
t = int(input())
for case in range(t):
    vars = input().split()
    n = int(vars[0])#počet částic
    k = int(vars[1])#počet změn
    charges = list(input())
    flips = input().split()
    
    
    def create_distances(particlelist, destination):
        for i in range(n-1):
            if particlelist[i] == particlelist[i+1]:
                destination.append(1)
            else:
                destination.append(0)
    
    
    def flip(destination, index):
        index -= 1
        rollingcount = 0
        try:
            if destination[index] == 0:
                destination[index] = 1
                rollingcount += 1
            else:
                destination[index] = 0
                rollingcount -= 1
        except IndexError:
            pass
        index -= 1
        if index < 0:
            return rollingcount
        try:
            if destination[index] == 0:
                destination[index] = 1
                rollingcount += 1
            else:
                destination[index] = 0
                rollingcount -= 1
        except IndexError:
            pass
        return rollingcount
    
    
    
    
    distances = []
    
    create_distances(charges, distances)
    
    sumdist = sum(distances) + n - 1
    #print(sumdist)
    
    for tobeflipped in flips:
        tobeflipped = int(tobeflipped)
        sumdist += flip(distances, tobeflipped)
        print(sumdist)
    
    
    
    
    
    
    
    
    
    
    