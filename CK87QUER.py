import math
t = int(input())
for case in range(t):
    #vars = input().split()
    y = int(input())
    
    
    
    if y == 1:
        print(0)
        continue
    
    
    
    def baseoflargestsquarelessthan(num):
        return int(math.floor(math.sqrt(num)))
    
    
    def sumofsquaresupto(k):
        return (k * (k + 1) * (2*k + 1)) / 6
    
    
    b = baseoflargestsquarelessthan(y) 
    
    
    if y <= 701:
        print(int(b*y - sumofsquaresupto(b)))
        continue
    
    
    
    
    z = baseoflargestsquarelessthan(y - 701)
    
    
    #suma <= z
    suma = z*700
    
    
    print(int(suma + (b-z)*y - (sumofsquaresupto(b) - sumofsquaresupto(z))))
    
    
    
    
    
    