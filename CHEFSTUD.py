# cook your dish here
for _ in range(int(input())):
    s=input()
    c=0
    for i in range(0,len(s)-1):
        if s[i]=='<' and s[i+1]=='>':
            c+=1 
    print(c)        
            