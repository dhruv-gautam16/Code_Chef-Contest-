def isPrime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True
SoE = [True for i in range(1001)]
SoE[0], SoE[1] = False, False
for n in range(4, 1001, 2):
    SoE[n] = False
p = 3
while p*p <= 1000:
    if SoE[p] == True:
        for n in range(p*2, 1001, p):
            SoE[n] = False
    p += 2
p_sqrs = [p*p for p in range(1000) if SoE[p]]
p_cubs = [p*p*p for p in range(100) if SoE[p]]
while 1:
    num = int(input())
    if num == 0:
        break
    fin = False
    for ps in p_sqrs:
        for pc in p_cubs:
            if isPrime(num - ps - pc):
                print(num - ps - pc, round(ps**0.5), round(pc**(1/3)))
                fin = True
                break
        if fin:
            break
    if not fin:
        print(0, 0, 0)
