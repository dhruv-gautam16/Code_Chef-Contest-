# cook your dish here
# cook your dish here
# cook your dish here
for _ in range(int(input())):
    first = input().split()
    second = input().split()
    count = 0
    for i in first:
        if i in second:
            count += 1
    if count >= 2:
        print("similar")
    else:
        print("dissimilar")