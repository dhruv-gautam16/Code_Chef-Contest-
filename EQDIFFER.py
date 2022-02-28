def minimum(arr, length):
    if length <= 2:
        return 0
    else:
        set_ = set(arr)
        dictionary = {

        }
        for y in set_:
            dictionary[str(y)] = 0
        for y in arr:
            dictionary[str(y)] += 1
        return min(length - 2, length - max(dictionary.values()))


test_cases = int(input())
while test_cases != 0:
    data1 = int(input())
    data = list(map(int, input().split()))
    print(minimum(data, data1))
    data.clear()
    test_cases -= 1
