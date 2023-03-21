for _ in range(int(input())):
    nums = list(map(int, input().split()))
    nums.remove(max(nums))
    print(max(nums))