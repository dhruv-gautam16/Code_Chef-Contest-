# cook your dish here
import numpy as np

TH = 49

def get_best(comp_array):
    best_comp_till_i = np.zeros(TH)
    for fh in range(TH):
        comp_end_fh = comp_array[fh]
        max_comp = max(comp_end_fh + best_comp_till_i)
        best_comp_till_i[fh] = max_comp
    return int(best_comp_till_i[-1])
    
T = int(input())

for t in range(T):
    n = int(input())
    comp_array = np.zeros((TH,TH))
    for _ in range(n):
        sh, fh, comp = map(int,input().split())
        comp_array[fh, sh] = max(comp_array[fh, sh], comp)
    print(get_best(comp_array))
    