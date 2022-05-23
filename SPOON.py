"""
Cases:

"""
def checkRow(s:list):
    for i in s:
        if('spoon' in i):
            return True
        # print(i)
    return False
def checkColumn(s:list,a:int,b:int):
    j = 0
    l = []
    s1 = ''
    for i in range(b):
        s1= ''
        j = 0
        while(j<a):
            s1+=s[j][i]
            j+=1
        l.append(s1)
    # print(l)
    return checkRow(l)
        
        
for t in range(int(input())):
    # n = int(input())
    # l = list(map(int,input().split()))
    a,b = map(int,input().split())
    l = []
    for i in range(a):
        l.append(input().lower())
    if(a<5 and b<5):
        print('There is indeed no spoon!')
    else:
        if(checkColumn(l,a,b) or checkRow(l)):
            print('There is a spoon!')
        else:
            print('There is indeed no spoon!')
        
    
