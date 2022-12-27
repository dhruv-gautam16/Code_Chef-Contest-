n = int(input())
out = []
for i in range(n):
    x = int(input())
    s = input()
    mindistance = x
    for j in range(x):
        if(s[j]=='1'):
            for k in range(j+1,x):
                if(s[k]=='1'):
                    distance = k-j
                    
                    break
            if(distance>2):
                if(distance%2==0):
                    distance = 2
                else:
                    distance = 1
            if (distance<mindistance):
                mindistance = distance
    out+=[int(mindistance)]

for i in out:
    print(i)
