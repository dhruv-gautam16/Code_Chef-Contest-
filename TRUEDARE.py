tests = int(input())
for test in range(tests):
    truth_by_ram = int(input())
    ram_truths = set(map(int, input().split()))
    dare_by_ram = int(input())
    ram_dare = set(map(int, input().split()))

    truth_task = int(input())
    shyam_truth_tasks = set(map(int, input().split()))
    dare_task = int(input())
    shyam_dare_tasks = set(map(int, input().split()))

    if shyam_dare_tasks.issubset(ram_dare) and shyam_truth_tasks.issubset(ram_truths):
        print("yes")
    else:
        print("no")

