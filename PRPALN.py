import sys
# from functools import lru_cache
# @lru_cache(maxsize=None)

def chk(s,i,j):
    while(i<j):
        if(s[i]!=s[j]):
            return 0
        i+=1
        j-=1
    return 1

def _input():
    return sys.stdin.readline().strip()

def main():
    for _ in range(int(_input())):
        s = str(_input())
        i = 0
        j = len(s)-1
        temp = 0
        # x=True
        while(i<j):
            if s[i]==s[j]:
                i+=1 
                j-=1 
            else:
                x = chk(s,i+1,j) or chk(s,i,j-1)
                temp = 1 
                break
        if temp==0:
            print("YES")
        else:
            if x==True:
                print("YES")
            else:
                print("NO")

main()