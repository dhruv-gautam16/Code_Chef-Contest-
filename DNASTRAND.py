# cook your dish here
for i in range(int(input())):
    n = int(input())
    string = input()
    new_str = ''
    for i in range(n):
        if string[i]=='A':
            new_str = new_str + "T"
        elif string[i]=='T':
            new_str = new_str + "A"
        elif string[i]=='C':
            new_str = new_str + "G"
        elif string[i]=='G':
            new_str = new_str + "C"
    print(new_str)