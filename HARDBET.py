for _ in range(int(input())):
    submissions = list(map(int,input().split()))
    hardest = min(submissions)
    if hardest is submissions[2]:
        print("Alice")
    elif hardest is submissions[1]:
        print("Bob")
    else:
        print("Draw")
    