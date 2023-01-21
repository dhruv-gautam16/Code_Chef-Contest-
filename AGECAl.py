def days_since_birth(n, months, y_b, m_b, d_b, y_c, m_c, d_c):
    if y_c==y_b and m_c==m_b and d_c==d_b: return 1
    elif y_c==y_b and m_c==m_b: return d_c-d_b+1
    elif y_c==y_b: return months[m_b-1] - d_b + 1 + d_c + sum(months[m_b:m_c-1])
    result = (y_c - y_b - 1) * sum(months)
    result += sum(months[m_b:])
    result += sum(months[:m_c-1])
    result += months[m_b-1]-d_b+1
    result += d_c
    for i in range(y_b,y_c):
        if i%4==0:
            result+=1
    return result
for _ in range(int(input())):
    print(days_since_birth(int(input()),list(map(int,input().split())),*map(int,input().split()),*map(int,input().split())))