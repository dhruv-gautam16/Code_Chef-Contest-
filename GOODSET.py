tests = int(input())
for test in range(tests):
    required_integers = int(input())
    initial = 1
    required_set = {str(initial)}
    if required_integers > 1:
        for integer in range(required_integers-1):
            required_set.add(str(initial + 2))
            initial += 2
    print(' '.join(required_set))