# cook your dish here
for _ in range(int(input())):
    x=list(map(str,input().split()))
    
    c=1
    for i in range(len(x)-1):
        
        if x[i]=="1" and x[i+1]=="1":
            c+=1
        else:
            c=1
        
        if c>=6:
            print("#coderlifematters")
            break
      
        
    else:
        print("#allcodersarefun")