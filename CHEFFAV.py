for _ in range(int(input())):
    n = int(input())
    s = input()

    code = s.find("code")
    if s.find("chef") >= code+4:
        print("AC")
    else:
        print("WA")

