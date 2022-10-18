t=int(input())
while(t>0):
    t-=1 
    n=int(input())
    s=str(input())
    maximum= max(s.count('1'),s.count('0'))
    value=''
    if s.count('1')>=s.count('0'):
        value+='1'
    else:
        value+='0'
    answer=''
    while maximum>0:
        maximum-=1 
        answer+=value 
    print(answer)
    
    
        
        
    
            
    
        
        
        