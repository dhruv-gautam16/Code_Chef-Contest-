N = int(input())
count = 0
for i in range(N):
  l = list(map(int, input().split()))
  A = ((l[2] - l[0]) ** 2) + ((l[3] - l[1]) ** 2)
  B = ((l[4] - l[2]) ** 2) + ((l[5] - l[3]) ** 2)
  C = ((l[4] - l[0]) ** 2) + ((l[5] - l[1]) ** 2)
  if A + B == C:
    count += 1
  elif B + C == A:
    count +=1
  elif C + A == B:
    count += 1
print(count)