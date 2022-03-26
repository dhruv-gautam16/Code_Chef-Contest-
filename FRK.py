count = 0
l1 = ['ch','ef','he']
for i in range(int(input())):
	s1 = input()
	for j in range(0,len(l1)):
		if l1[j] in s1:
			count = count + 1
			break
print(count)