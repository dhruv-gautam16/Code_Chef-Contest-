# cook your dish here
for i in range(int(input())):
    pile1, pile2, m= map(int,input().split(' '))
    
    #find minimum no. of stones 
    min_= min(pile1,pile2)
    
    #maximum no. of stones that can be removed
    #from each pile
    max_= (m*(m+1))//2
    
    #check if no. of minimum no. of stones
    #is less than or equal to m
    if min_<=max_:
        print(pile1+pile2-2*min_)
    else:
        print(pile1+pile2-2*max_)
            