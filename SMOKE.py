import math

# cook your dish here
for _ in range(int(input())):
    n , x , y = map(int , input().split())
    
    total_smoke = 0
    
    bus = n // 100
    car = bus * 25
    bus_smoke = bus * x
    car_smoke = car * y
    
    total_smoke = min(bus_smoke , car_smoke)
    
    n = n % 100
    
    if n > 0:
        bus_smoke = x
        car = math.ceil(n / 4)
        car_smoke = car * y
        total_smoke += min(bus_smoke , car_smoke)
    
    print(total_smoke)
    
    