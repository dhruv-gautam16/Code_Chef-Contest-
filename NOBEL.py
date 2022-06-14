# cook your dish here
t = int(input())
while t>0:
    n_m = input().split()
    n = int(n_m[0])
    m = int(n_m[1])
    courses = list(map(int, input().split()))
    unique_courses =set()
    for course in courses:
        unique_courses.add(course)
    if len(unique_courses)<m:
        print('Yes')
    else:
        print('No')
    t -= 1
