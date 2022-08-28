for _ in range(int(input())):
    r,g,b,m= map(int,input().split())
    rp=list(map(int,input().split()))
    gp=list(map(int,input().split()))
    bp=list(map(int,input().split()))
    rp.sort(reverse=True)
    bp.sort(reverse=True)
    gp.sort(reverse=True)
    main=[rp,bp,gp]
    main.sort(reverse=True)
    for i in range(m):
        for j in range(len(main[0])):
            main[0][j]//=2
        main.sort(reverse=True)
    print(main[0][0])
