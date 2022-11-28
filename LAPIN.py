# cook your dish here
test = int(input())
for i in range(test):
    string = input()
    # print(len(string) // 2)
    # string1 = []
    # string2 = []
    string1 = list(string[:len(string)//2])
    string2 = list(string[len(string) // 2: ])
    if(len(string)%2 != 0):
        string2 = list(string[len(string) // 2+ 1: ])
    string1.sort()
    string2.sort()
    if(string1 == string2):
        print("YES")
    else:
        print("NO")