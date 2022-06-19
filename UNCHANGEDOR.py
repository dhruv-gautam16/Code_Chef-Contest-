def pow2(bits):
              # print(' 1 <<bits',1 <<bits)
              return 1 <<bits
def max_num(bits):
              # print('pow2(bits+1)-1',pow2(bits+1)-1)
              return pow2(bits+1)-1 
def solution():
              n=int(input())
              bit_count=0
              while n>>bit_count:
                            # print('n>>bit_count',n>>bit_count)
                            bit_count+=1 
              ans=0
              for i in range(1,bit_count):
                            ans+=min(n,max_num(i))-pow2(i)
                            # print('ans',ans)
              print(ans)
              
t=int(input())
while(t>0):
                           
               t-=1
               solution() 