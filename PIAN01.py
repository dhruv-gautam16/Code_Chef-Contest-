for tc in range(int(input())):
    x=str(input())
    n= int(input())
    keyboardlen= 12*n
    a=list(x)
    r=a.count('T')*2 + a.count('S')
    l= keyboardlen//r
    ans= (keyboardlen*l) - ((l*r*(l+1))//2)
    print(ans)
