# cook your dish here
# import sys
# sys.stdin = open('/home/puneet/Documents/Cpp Programs/input.txt', 'r')
# sys.stdout = open('/home/puneet/Documents/Cpp Programs/output.txt', 'w')

angle = dict()
def genAngle():
	

	for i in range(0,12):
		for j in range(0,60):
			ang = abs((60*i - 11*j)/2)
			if(ang>180):
				ang=360-ang

			
			if(i<10 and j<10):
				angle[f"0{i}:0{j}"] = ang
			elif(i<10 and j>9):
				angle[f"0{i}:{j}"] = ang

			elif(i>9 and j>9):
				angle[f"{i}:{j}"] = ang

			elif(i>9 and j<10):
				angle[f"{i}:0{j}"] = ang


	# for key,value in angle.items():
	# 	print(key,value)


genAngle()

def solve(n):
	x=1/120
	for key,value in angle.items():
		if(abs(value-n)<(1/120)):
			print(key)

if __name__ == '__main__':
	
	for _ in range(int(input())):
		n = float(input())

		solve(n)


