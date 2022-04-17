def fun(s):
    balance=0
    max_balance=0
    for i in range(len(s)):
        if(s[i]=="("):
            balance+=1
        else:
            balance-=1
        max_balance=max(balance,max_balance)
    return max_balance

for i in range(int(input())):
    s=input()
    x=fun(s)
    print(('('*x)+(')'*x))