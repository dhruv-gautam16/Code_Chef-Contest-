mod = 1000000007

t = int(input())
for tt in range (t) :
    n , m = map ( int , input().split() )

    L = [0] * m

    for i in range (m) :

        x , y = map ( int , input().split() )

        y-=x

        L[i] = y

        n -= x

    D = [ [ 0 for i in range( n+1 ) ] for j in range ( m ) ]

    for i in range ( n +1 ) :

        if L[0] >= i :

            D[0][i] = 1

            continue

        break

    for i in range ( 1 , m ) :

        for j in range ( n + 1 ) :

            for k in range ( L[i]+1 ) :

                if j-k >= 0:

                    D[i][j] = ( D[i][j] + D[i-1][j-k] ) % mod

                    continue

                break

    print(D[m-1][n]%mod)
                
