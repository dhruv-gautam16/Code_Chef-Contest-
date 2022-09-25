# cook your dish here
def main():    
    T = int(input())
    for counter in range(T):
        n,r = map(int,input().split())
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        bestsum = 0
        currsum = 0
        for i in range(n):
            currsum = max(0,currsum+b[i])
            bestsum = max(currsum,bestsum)
            
            if i < n-1:
                currsum = max(0,currsum-(a[i+1]-a[i])*r)
                bestsum = max(currsum,bestsum)
                
        print(bestsum)
    
if __name__ == '__main__':
    main()