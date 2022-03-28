def main():
    testcases=int(input())
    for testcase in range(testcases): 
        X,Y,A,B= map(int,input().strip().split(' '))
        rival=[A,B]
        chef=[X,Y]
        gold=2
        for i in chef:
            if i in rival:
                gold-=1
        print(gold)

main()