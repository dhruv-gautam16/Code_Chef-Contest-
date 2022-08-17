
def min_count(L1,L2):
    
    n = len(L1)
    l1 = [float("inf")]*n
    l2 = [float("inf")]*n
    i = n-1
    j = n-1
    if L1[i]!="#":
        l1[i]=0
    if L2[j]!='#':
        l2[j]=0
    i-=1
    j-=1
        
    while i>=0 and j>=0:
        
        if L1[i]!="#":
            l1[i]=min(l1[i+1],1+l2[i+1])
        if L2[j]!="#":
            l2[j]=min(l2[j+1],1+l1[j+1])
        i-=1
        j-=1
        
    return min(l1[0],l2[0])
        
        

def read_out():
    
    T = int(input())
    
    
    for i in range(T):
        
        L1 = input()
        L2 = input()
        
        count = min_count(L1,L2)
        
        if count!=float("inf"):
            print("Yes")
            print(count)
            
        else:
            print("No")
            
            
read_out()


        
        
        
            
            
            
        
            
           
                    
                
        
        