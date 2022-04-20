def get_factorial(num):
    num = int(num)
    if num==1 or num==0:
        return 1
    return num*get_factorial(num-1)

no_of_peoples,cars = map(int,input().split())
possible_ways = 0
for i in range(cars):
    car = input()
    for compartment in range(1,10):
        s1 = ((compartment - 1)*4)
        s2 = s1 + ((9-compartment)*4) + (2*(9-compartment)) + 4 
        seats = car[s1:s1+4] + car[s2:s2+2]
        available_seats = seats.count("0")
        if no_of_peoples <= available_seats:
            possible_ways += get_factorial(available_seats) // (get_factorial(no_of_peoples)*get_factorial(available_seats-no_of_peoples))
print(possible_ways)