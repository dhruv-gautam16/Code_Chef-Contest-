# cook your dish here
# cook your dish here
T = int(input())
for _ in range(T):
    
    A,B,C = map(int, input().split(' '))
    #A dollars and B cents and C cents to put in machine 
    cur_max = A*100 + B 
    pos_max = 0 
    
    count  = 0
    while A*100 + B >C and count<10000:
        if B<C:
            A -= 1 
            B += 100 
        B -= C 
        A,B = B,A 
        count += 1 
        
        if A*100 + B > cur_max:
            cur_max = A*100 + B 
            pos_max = count 
            
    print(pos_max)