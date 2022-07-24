# cook your dish here
# cook your dish here
def trange():
	return range(int(input()))

def splitMap():
	return map(int,input().split())

def listOfNumbers():
	return list(map(int,input().split()))

def number():
	return int(input())


def binary(x):
	return bin(x).replace("0b","")
import math 
from collections import Counter  
import functools 
import numpy as np 

# Helper Function 

def preComputeMatrix(maxN):
	rows = [False] * 1001
	cols = [False] * 1001
	diag = [False] * 2001
	matrix = [[False for _ in range(1001) ]for _ in range(1001)]
	# Set Origin as Win 
	rows[0] = True 
	cols[0] = True
	diag[0] = True 
	for i in range(1,maxN+1):
		for j in range(1,maxN+1):
			if i == j:
				continue
			if not rows[i] and not cols[j]:
				if j >= i :
					if not diag[j-i]:
						rows[i] = True 
						cols[j] = True 
						diag[j-i] = True 
						matrix[i][j] = True 
				else:
					if not diag[1000 + i - j ] :
						rows[i] = True
						cols[j] = True 
						diag[maxN + i - j] = True 
						matrix[i][j] = True 
	return matrix 

def main():
	# Loss Position Matrix
	matrix = preComputeMatrix(1000)
	for i in trange():
		m,n,p,q = splitMap()
		m = m - p 
		n = n - q 
		print("Bob" if matrix[m][n] else "Alice")
    
try :

    if __name__ == '__main__':
    	main()
    	exit()
except EOFError:
	print("Input Not Given")
