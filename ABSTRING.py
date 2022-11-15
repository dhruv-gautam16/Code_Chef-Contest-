t = int(input())
for i in range(0, t):

    l=int(input())
    str=input()
    arr=[]
    for i in range(0,l):
        arr.append(str[i])
    
    arr.sort()
    
    arr2=[]
    arr3=[]
    for i in range(0,l):
        if(i%2==0):
            arr2.append(arr[i])
        else:
            arr3.append(arr[i])
    if(arr2==arr3):
        print("yes")
    else:
        print("no")
