# cook your dish here
for i in range(int(input())):
     status=0
     count=0
     a,b,c=map(int,input().split())
     s=list(map(int,input().split()))
     s2=list(map(int,input().split()))
     s3=[]
     for j in range(len(s)):
          #s3.append(str(s[j])+" - "+str(s2[j])+" = "+str(abs(s[j]-s2[j])))
          if abs(s[j]-s2[j])>c:
               status=1
          else:
               count+=1
     if status==0 or count>=b:
          print("YES")
     else:
          print("NO")