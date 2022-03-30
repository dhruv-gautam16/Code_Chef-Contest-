# cook your dish here

T = int(input())
for t in range (T):
    finish, dist_bolt, tig_acc, bolt_sp = map(int,input().split())
    t_bolt = finish/bolt_sp
    t_tig = (2*(dist_bolt + finish)/tig_acc)**0.5
    if t_bolt == t_tig:
        print("Tiger")
    elif t_bolt < t_tig:
        print("Bolt")
    else:
        print("Tiger")
        
    
