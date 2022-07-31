# cook your dish here
def prob(p, nodes_info, nodes):
    arr = [0 for i in range(nodes+1)]
    
    for i in range(1, nodes+1):
        gate_typ = nodes_info[i-1][0]
        
        if gate_typ == 0:
            arr[i] = p
        elif gate_typ == 1:
            input_1 = nodes_info[i-1][1]
            input_2 = nodes_info[i-1][2]
            
            arr[i] = 1 - (1-arr[input_1])*(1-arr[input_2])
        elif gate_typ == 2:
            input_1 = nodes_info[i-1][1]
            input_2 = nodes_info[i-1][2]
            
            arr[i] = (arr[input_1])*(arr[input_2])
    return arr[-1]
    
t = int(input())
for _ in range(t):
    space = input()
    nodes = int(input())
    nodes_info = []
    for _ in range(nodes):
        nodes_info.append(list(map(int, input().strip().split())))
    
    # print(nodes, nodes_info)
    if nodes > 2:
        low = 0
        high = 1
        
        ans = None
        while low < high:
            mid = (low+high)/2
            
            prob_ = prob(mid, nodes_info, nodes)
            # print(prob_, mid, low, high)
            if round(prob_, 7) == 0.5:
                ans = round(mid, 5)
                break
            elif prob_ < 0.5:
                low = mid
            elif prob_ > 0.5:
                high = mid
                
        print("{0:.5f}".format(ans))
    else:
        print("{0:.5f}".format(0.5))