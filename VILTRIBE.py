import sys
# from functools import lru_cache
# @lru_cache(maxsize=None)

def _input():
    return sys.stdin.readline().strip()

def main():
    for _ in range(int(_input())):
        s = str(_input())
        a=0
        b=0
        temp=0
        ctr=0
        for i in range(len(s)):
            if(temp>0 and s[i]=='.'):
                ctr+=1
            if(s[i]=='A'):
                a+=1
                if(temp==1):
                    a+=ctr
                    ctr=0
                elif(temp==2):
                    ctr=0
                temp=1
            if(s[i]=='B'):
                b+=1
                if(temp==2):
                    b+=ctr
                    ctr=0
                elif(temp==1):
                    ctr=0
                temp=2
        print(a,b)
main()