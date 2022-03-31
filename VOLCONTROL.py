Cases = int(input())
for i in range(Cases):
    volume = input()
    print(abs(eval(volume.replace(' ', '-'))))
    