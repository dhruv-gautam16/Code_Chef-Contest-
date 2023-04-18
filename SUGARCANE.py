# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    total=n*50
    sug=20/100*total
    mint=20/100*total
    rent=30/100*total
    print(int(total-sug-mint-rent))