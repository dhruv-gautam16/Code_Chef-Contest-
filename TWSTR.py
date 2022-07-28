# cook your dish here
############################# Definitions #############################
import sys
input = sys.stdin.readline

def rii():
	return range(int(input().strip()))

def ii():
	return int(input().strip())

def mii():
	return map(int, (input().strip()).split(' '))

def lmii():
	return list(map(int, (input().strip()).split(' ')))

def si():
	return str(input().strip())
#######################################################################

from operator import itemgetter

failure = "NO"

class Recipe(dict):
	def starts_with(self, start_of_key):
		return sorted([(key, self[key]) for key in self if key.startswith(start_of_key)], reverse=True, key = itemgetter(1))

def solve(*args):
	r, starts = args
	for s in starts:
		ss = r.starts_with(s)
		if len(ss) > 0:
			print(ss[0][0])
		else:
			print(failure)

def do_codechef():
	n = ii()
	r = Recipe()
	for _ in range(n):
		x, y = input().split(' ')
		r[x] = int(y.strip())
	q = ii()
	starts = [input().strip() for x in range(q)]
	solve(r, starts)

if __name__ == "__main__":
	do_codechef()
	exit()
