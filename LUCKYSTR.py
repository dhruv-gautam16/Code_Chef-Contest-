# cook your dish here
import re


lucky, found = map(int,input().split(" "))
arr_luck = []

for i in range(lucky):
    
    arr_luck.append(str(input()))
    
    
for j in range(found):
    flag = 0
    check = str(input())
    for x in arr_luck:
            if re.search(x, check) or len(check) >= 47:
                flag = 1
                print("Good")
                break
    if flag == 0:
            print("Bad")