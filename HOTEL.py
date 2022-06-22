def guestCounter():
    n = int(input())
    arrival = list(map(int, input().split()))
    departure = list(map(int, input().split()))
    time = []
    
    for arrivalTime in arrival:
        time.append((arrivalTime, 1))
    for departureTime in departure:
        time.append((departureTime, 0))
    time.sort()
    
    ans, noOfOccupants = 0, 0
    for eachTime in time:
        if eachTime[1] == 1:
            noOfOccupants += 1
        else:
            noOfOccupants -= 1
        ans = max(ans, noOfOccupants)
    
    print(ans)
    

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        guestCounter()
        
        