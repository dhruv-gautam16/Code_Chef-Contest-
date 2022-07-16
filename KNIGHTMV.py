for _ in range(int(input())):
    s = input()
    if len(s) != 5:
        print('Error')
    elif 'a' <= s[0] <= 'h' and ord('1') <= ord(s[1]) <= ord('8') and s[2] == '-' and 'a' <= s[3] <= 'h' and ord('1') <= ord(s[4]) <= ord('8'):
        if (abs(ord(s[0])-ord(s[3])) == 2 and abs(int(s[1]) - int(s[4])) == 1) or (abs(ord(s[0])-ord(s[3])) == 1 and abs(int(s[1]) - int(s[4])) == 2):
            print('Yes')
        else:
            print('No')
    else:
        print('Error')