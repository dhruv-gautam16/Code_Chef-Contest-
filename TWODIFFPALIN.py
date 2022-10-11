# cook your dish here
#dos impares no pincha
#dos pares pincha
#par con 1 no pincha
#par con impar pincha
import sys
from math import ceil, gcd, sqrt, log ,lcm 
import bisect


# IMPORT PRACTICE AND CONCENTRATION
 
mod = 1000000007

def createDic(nums):
    dic=dict()
    for i in nums:
        if not (i in dic):
            dic[i]=1
        else:
            dic[i]+=1
    return dic
def subarray_sum_max(nums):
    array=[]
    suma_parcial=0
    max_sum=0
    index=0
    se_refresco=True
    for i in range(len(nums)):
        suma_parcial+=nums[i]
        if(max_sum<suma_parcial):
            if(se_refresco):
                array=[]
                se_refresco=False
                index=i
            max_sum=suma_parcial
        if (suma_parcial < 0): 
            suma_parcial = 0
            se_refresco=True
        elif(not se_refresco):
            array.append(nums[i])
    return(array,index,max_sum)


def solve():
    #n=int(input())
    a,b=map(int,input().split())
    #nums=list(map(int, input().split()))
    #m=int(input())
    #b=list(map(int, input().split()))
    #s=input()
    
    if(a%2==0 and b%2==0):
        print("Yes")
    elif(a%2!=0 and b%2!=0):
        print("No")
    elif(a!=1 and b!=1):
        print("Yes")
    else:
        print("No")














test=int(input())
while test!=0:
    solve()
    test-=1

    
        

   