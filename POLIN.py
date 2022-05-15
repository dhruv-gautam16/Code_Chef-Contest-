for _ in range(int(input())):
     n = int(input())
     x = []
     y = []
     for i in range(n):
          a, b = map(int, input().split())
          x.append(a)
          y.append(b)
     x = list(set(x))
     y = list(set(y))
     print(len(x)+len(y))