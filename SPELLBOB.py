for _ in range(int(input())):
       a=list(input())
       b=list(input())
       
       flag=False
       for i in range(3):
              if a[i]=='o' or b[i]=='o':
                     b_count=0
                     for j in range(3):
                            
                            if i!=j and (a[j]=='b' or b[j]=='b'):
                                   b_count+=1
                            
                     if b_count==2:
                            flag=True

       print("yes" if flag else "no")              
                                   





