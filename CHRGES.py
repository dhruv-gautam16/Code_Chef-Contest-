t=int(input())
for i in range(t):
    n=int(input())
    a=input()
    if a=="0"*n:                    #no charge
        print(n)
    elif "+" in a and "-" in a:     #both type of charges present
        l=[]
        c=0
        for j in range(n):
            if a[j] in "+-":
                if l==[] or l[0]==a[j]:  
                    l=[a[j],j]
                else:                #when they are diff charges    
                    c+=(j-l[1]+1)%2  
                    l=[a[j],j]
        print(c)
    else:                            #exactly one type
        print("0")