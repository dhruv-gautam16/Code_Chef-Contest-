# cook your dish here

t=int(input())
for i in range(t):
    x=int(input())
    if x%3==1:
        print("HUGE")
    elif x%3==2:
        print("SMALL")
    else:
        print("NORMAL")