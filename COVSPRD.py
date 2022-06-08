# cook your dish here
#idea1: spread pattern 2 4 8 16 32 is powers of 2, if speculated spread is greater than population print population
# import time
noOfTestCases = int(input())
#global hashMap for all test cases
hashMap = {}
hitCounter=0
daySpread=[]
#for idea3
for iter in range(21):
    if iter+1 <= 10:
        daySpread.append(2**(iter+1))
    else:
        daySpread.append(1024*(3**(iter+1-10)))
        
for _ in range(noOfTestCases):
    P, D = map(int, input().split())
    #idea1
    """
    if D <= 10:
        val=2**D
        print(val) if P >= val else print(P)
    else:
        #debug code to find TLE; 10^7 get sigterm error
        # D=10000000
        # a=time.time()
        val = (2**10)*(3**(D-10))
        print(val) if P >= val else print(P)
        # print(time.time()-a)
        
    #status: TLE
    """
    #idea2: have to speed up execution, use hashMap, hit hashMap for each query and return answer for powers if it already has
    # a=time.time()
    """
    prod=1
    if D <= 10:
        val='2**'+str(D)
        if val in hashMap:
            print(hashMap[val]) if P >= hashMap[val] else print(P)
        else:
            for _ in range(D):
                prod*=2 
            hashMap[val] = prod
            # hitCounter+=1
            print(hashMap[val]) if P >= hashMap[val] else print(P)
    else:
        val = '(1024)*(3**('+str(D-10)+'))'
        if val in hashMap:        
            print(hashMap[val]) if P >= hashMap[val] else print(P)
        else:
            for _ in range(D-10):
                prod*=3
            hashMap[val] = 1024*prod
            # hitCounter+=1
            print(hashMap[val]) if P >= hashMap[val] else print(P)
    # print(time.time()-a)
    # print(hashMap)
    # print(hitCounter)
    """
    
    #idea3: help from codechef support, create array of spread upto 35days, so that access is constant time
    #conflict in idea3 since, d<=10^8
    #idea4: help from codechef support, N<=10^8, hence the spread population will also be <=10^8, hence d<=21
    if D > 21:
        print(P)
    elif D == 0:
        print(1)
    else:
        print(daySpread[D-1]) if daySpread[D-1] < P else print(P)
        
# print(daySpread)