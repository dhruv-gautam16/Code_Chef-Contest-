# cook your dish here
t = int(input())
h = []
m = []
for i in range(t):
    value = input()
    inputs = value.split(" ")
    h.append(int(inputs[0]))
    m.append(int(inputs[1]))



    
def dig(h,m):
    count = 0
    hou = ""
    mins = ""
    for i in range(0,h):
        hou = str(i)
        for j in range(0,m):
            mins = str(j)
            temp = hou + mins
            if(len(set(temp)) == 1):
                count += 1 
    return count
           
for i in range(t):
    print(dig(h[i],m[i]))     