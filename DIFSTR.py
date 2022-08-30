for i in range(int(input())):
    n=int(input())
    index=[]
    bstrings=[]
    for i in range(n):
        bstrings+=[int(input(),2)]
    for i in range(2**n):
        if(i not in bstrings):
            bina=(bin(i))[2::]
            break
    print("0"*(n-len(bina)),end="")
    print(bina)