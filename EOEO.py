for t in range(int(input())):
    ts = int(input())
    num_of_twos = 0
    tsc = ts
    while tsc%2==0:
        tsc = tsc//2
        num_of_twos += 1
    print(ts//pow(2,num_of_twos+1))
    
