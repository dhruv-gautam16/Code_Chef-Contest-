# cook your dish here
def solution(num):
    if not num.startswith("1"):
        return "1" + num
    else:
        return num[:1] + "0" + num[1:]
        
for i in range(0, int(input())):
    print(solution(input()))