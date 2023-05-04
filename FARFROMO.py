
for t in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    alex = pow(x1, 2) + pow(y1, 2)
    bob = pow(x2, 2) + pow(y2, 2)
        
    if(alex > bob):
        print("Alex")
    elif(bob > alex):
        print("Bob")
    elif(alex == bob):
        print("Equal")