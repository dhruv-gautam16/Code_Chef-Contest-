# cook your dish here
jacketCost,sockCost,money=map(int,input().split())
b=(money-jacketCost)//sockCost
if(b%2!=0):
    print("Unlucky Chef")
else:
    print("Lucky Chef")