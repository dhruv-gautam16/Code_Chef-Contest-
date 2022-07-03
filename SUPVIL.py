# cook your dish here
for _ in range (int(input())):
    n=int(input())
    l=[]
    for _ in range(n):
        l.append(input().strip())
    sh=0
    v=0
    for i in l:
        if (i[-3:]=="man"):
            sh+=1
        else:
            v+=1
        if (sh-v>=2):
            print("superheroes")
            break
        elif(v-sh>=3):
            print("villains")
            break
    else:
        print("draw")