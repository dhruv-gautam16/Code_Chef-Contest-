t = int(input())
while(t>0):
     t-=1
     line = input()
     count = 0
     lineLength = len(line)
     for i in range (0,lineLength-3):
          
          if 'c' in line[i:i+4] and 'h' in line[i:i+4] and 'e' in line[i:i+4] and 'f' in line[i:i+4]:
               count += 1
               #print('value of i is {0} and splice is {1}'.format(i, line[i:i+4]))
               
     if count == 0:
          print('normal')
     else:
          print('lovely ',count)

