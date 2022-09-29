# cook your dish here
T = int(input())
for _ in range(T):
    N = int(input())
    songs = []
    for _ in range(N):
        songs.append(list(map(int,input().split())))
    sweetness = 0
    played = set()
    play_later = []
    songs.sort(key=lambda x: x[1])
    
    for i in songs:
        if i[0] not in played:
            played.add(i[0])
            sweetness += len(played) * i[1]
        else:
            play_later.append(i)
    for i in play_later:
        sweetness += len(played) * i[1]
    print(sweetness)