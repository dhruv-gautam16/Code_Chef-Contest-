
import math 
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    sol = 0
    while b % a != 0:
	    a //= 2
	    sol += 1
    while a != b:
	    a *= 2
	    sol += 1
    print(sol)# cook your dish here
