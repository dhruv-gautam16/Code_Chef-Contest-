from collections import Counter

for _ in range(int(input())):
    n = int(input())
    colors = input()
    hm = Counter(colors).most_common()
    print(len(colors) - hm[0][1])