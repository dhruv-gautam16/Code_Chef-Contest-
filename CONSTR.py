
for _ in range(int(input())):
    N = int(input())
    In = input()
    res,count = "",1
    for i in range(1,N):
        if In[i] == In[i-1]:
            count += 1
        else:
            if(count%2 == 1):
                res += In[i-1]
            else:
                res = res+(In[i-1]*2)
            count = 1
    if count%2 == 1:
        res += In[N-1]
    else:
        res += (In[N-1]*2)
    print(res)