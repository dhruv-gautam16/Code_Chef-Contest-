# cook your dish here
def Solve(s,n):
    one_count,zero_count=0,0;
    one,zero=[],[]
    for i in range(2*n):
        if(s[i]=='1'):
            one_count+=1;
            one.append(i+1);
        else:
            zero.append(i+1);
            zero_count+=1;
    if(one_count==0 or zero_count==0):
        return [-1];
    elif(one_count==zero_count):
        return one;
    elif(one_count>zero_count):
        return one[:n];
    else:
        return zero[:n];



for _ in range(int(input())):
    n=int(input());
    s=input();
    print(*Solve(s,n));