# cook your dish here
a,b,c,d=map(int,input().split())
if a/b==c/d or a/b==d/c or a/c==b/d or a/c==d/b or a/d ==b/c or a/d == c/b:print('Possible')
else:print('Impossible')