# cook your dish here
for _ in range(int(input())):
    n=int(input())
    box1=list(map(int,input().split()))
    box2=list(map(int,input().split()))
    box3=list(map(int,input().split()))
    counter1,counter2=0,0
    counter1=sum([box1[1]+box1[2]+box2[2]])
    counter2=sum([box2[0]+box3[0]+box3[1]])
    print(max(counter1,counter2))