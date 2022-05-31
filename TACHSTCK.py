# cook your dish here
N, D = map(int, input().split())
list=[]
for j in range(N):
    list.append(int(input()))
list.sort()
count=0
i =0
while(i<len(list)-1):
    if list[i+1]-list[i]<=D:
        i =i+1
        count+=1
    i=i+1
print(count)




