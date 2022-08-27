def solve(s):
    curr_score_a,curr_score_b = 0, 0
    shots_left_a,shots_left_b = 5,5
    res = 0
    for i in range(10):
        res +=1
        if i&1:
            curr_score_b+= 1 if s[i] == "1" else 0
            shots_left_b-=1
        else:
            curr_score_a+= 1 if s[i] == "1" else 0
            shots_left_a-=1
        if curr_score_b > curr_score_a + shots_left_a:
                print("TEAM-B", res)
                break
        if curr_score_a > curr_score_b + shots_left_b:
                print("TEAM-A", res)
                break
    if curr_score_a == curr_score_b:
        tie_flg = True
        for i in range(10,20,2):
            if s[i] == s[i+1]:
                res +=2
            else:
                tie_flg = False
                res += 2
                if s[i] == "1":
                    print("TEAM-A",res)
                else:
                    print("TEAM-B",res)
                break
        if tie_flg:
            print("TIE")
try:
    s = input()
    while len(s) > 0:
        solve(s)
        s = input()
except:
    pass