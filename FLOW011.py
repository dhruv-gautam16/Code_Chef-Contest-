T = int(input())
for i in range(0,T):
    salary = int(input())
    if(salary < 1500):
        hra = (salary * 10) / 100
        da = (salary * 90) / 100
    else:
        hra = 500
        da = (salary * 98) / 100
    gross = salary + hra + da
    print("{:.2f}".format(gross))