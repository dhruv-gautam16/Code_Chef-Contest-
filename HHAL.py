# cook your dish here
tc = int(input())

for _ in range(tc):
    string = input()
    
    if string == string[::-1]:
        print(1)
    else:
        print(2)