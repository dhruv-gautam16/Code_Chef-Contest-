for _ in range(int(input())):
    n = input()
    st = set()
    for i in range(1,len(n)):
        sub = n[i-1]+n[i]
        st.add(sub)
    print(len(st))