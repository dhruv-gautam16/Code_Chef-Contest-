# cook your dish here
def transformIndex (k, index):
    i = k
    new_index = 0
    while (i > 0):
        res = index % 2
        index= index//2 
        new_index = (new_index << 1) | res
        i -= 1
        
    return new_index


def solution (k, message):
    k = int(k)
    ans = ""
    
    for i in range(len(message)):
        ans += message[transformIndex(k, i)]
    return ans
    
if __name__ == "__main__":
     n = int(input ())
     tests = []
     for i in range (n):
         tests.append(input().split(' '))
         
     for test in tests:
         print(solution (int(test[0]), test[1]))
     
 
