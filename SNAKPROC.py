for r in range(int(input())):
    l = int(input())
    s = input()
    a = s.replace('.','')
    b = a.replace('HT','')
    if len(b)==0:
        print("Valid")
    else:
        print("Invalid")