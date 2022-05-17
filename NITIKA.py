# cook your dish here
for i in range(int(input())):
     s=input()
     if s.count(' ')==0:
          print(s.capitalize())
     else:
          str1=''
          list1=s.split()
          for k in list1[0:len(list1)-1]:
               str1+=k[0].upper()+". "
          str1+=list1[len(list1)-1].capitalize()
          print(str1)