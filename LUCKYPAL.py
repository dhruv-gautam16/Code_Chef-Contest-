def inBounds(index, l , r):
    if index>=l and index <= r:
        return True 
    return False
    
for _ in range(int(input())):
    s = input().strip()
    l = len(s) 
    if l<9:
        print('unlucky')
        continue
    
    count = 0 
    minimum = 10000000000
    answer = "" 
    
    for index in range(l-5+1):
        copyStr = list(s)
        count = 0 
        if copyStr[index] != 'l':
            copyStr[index] = 'l'
            count+=1 
        if copyStr[index+1] != 'u':
            copyStr[index+1] = 'u'
            count+=1 
        if copyStr[index+2] != 'c':
            copyStr[index+2] = 'c'
            count+=1 
        if copyStr[index+3] != 'k':
            copyStr[index+3] = 'k'
            count+=1 
        if copyStr[index+4] != 'y':
            copyStr[index+4] = 'y'
            count+=1 
        i = 0 
        j = len(copyStr)-1 
        l = index 
        r = index + 4 
        found = True
        while i<=j:
            if copyStr[i] != copyStr[j]:
                if (i < l or i > r) and (j < l or j > r):
                    if copyStr[i] < copyStr[j]:
                        copyStr[j] = copyStr[i]
                        count+=1 
                    else:
                        copyStr[i] = copyStr[j]
                        count+=1 
                        
                elif inBounds(i, l, r):
                    if j < l or j > r:
                        copyStr[j] = copyStr[i]
                        count+=1
                    else:
                        found = False
                        break 
                elif inBounds(j,l,r):
                    if i < l or i > r:
                        copyStr[i] = copyStr[j] 
                        count+=1 
                    else:
                        found = False
                        break
                else:
                    found = False
                    break
            i+=1 
            j-=1
        if found:
            if count < minimum:
                minimum = count 
                answer = ''.join(copyStr) 
            elif minimum == count:
                string = ''.join(copyStr)
                answer = min(answer, string)
       
    if minimum == 10000000000:
            print('unlucky')
    else:
            print(answer, minimum)
