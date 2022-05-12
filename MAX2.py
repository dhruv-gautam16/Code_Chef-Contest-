# cook your dish here
n = int(input())
bit = input()
for i in range(1,33):
    if (int(bit,2) % 2**i) == 0:
        power = i
print(power)