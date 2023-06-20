# cook your dish here
# function to count number of holidays in a given month
def count_holidays(n, festivals):
    holidays = set()  # set to store all holidays
    for i in range(1, 31):
        if i % 7 == 6 or i % 7 == 0:  # check if day is a Saturday or Sunday
            holidays.add(i)
    for festival in festivals:
        if festival % 7 != 0 and festival % 7 != 6:  # check if festival is not on a weekend
            holidays.add(festival)
    return len(holidays)

# main program
t = int(input())  # number of test cases
for i in range(t):
    n = int(input())  # number of festival days
    festivals = list(map(int, input().split()))  # list of festival days
    print(count_holidays(n, festivals))  # print number of holidays
