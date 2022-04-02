# cook your dish here
t = int(input())
for i in range(t):
    s = input()
    x = s.upper()
    
    if x == "B":
        print("BattleShip")
    elif x == "C":
        print("Cruiser")
    elif x == "D":
        print("Destroyer")
    elif x == "F":
        print("Frigate")
    