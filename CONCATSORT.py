
for _ in range(int(input())):
    num = int(input())
    array_1 = list(map(int,input().split()))[:num]
    array_2 = sorted(array_1)
    array_3 = [array_1.index(array_2[0]),0]
    null_array_1 = [0]*num
    # loop:
    for i in range(2):
        array_3[0] = 0
       
        while array_3[0] < num:
      
            if not null_array_1[array_3[0]] and array_1[array_3[0]] == array_2[array_3[1]]:
                null_array_1[array_3[0]] = 1
                array_3[0] += 1
                array_3[1] += 1
            else:
                array_3[0] += 1
  
    if array_3[0] == array_3[1]:
        print("YES")
    else:
        print("NO")