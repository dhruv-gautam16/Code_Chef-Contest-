#include <bits/stdc++.h>
#define ll long long int
#define ull unsigned long long int
using namespace std;

void solve()
{
    string s;
    cin >> s;
    ll n = s.size();
    if (n == 1 || n == 2)
    {
        cout << -1 << "\n";
    }
    else
    {
        char first = s[0], last = s[n - 1];
        ll ans = 0, temp = 0;
        for (ll i = 1; i < n; i++)
        {
            if (s[i] != first && s[i] != last)
            {
                temp++;
            }
            else
            {
                ans = max(ans, temp);
                temp = 0;
            }
        }
        if (ans == 0)
        {
            cout << -1 << "\n";
        }
        else
        {
            cout << ans << "\n";
        }
    }
}

int main()
{
    ll t;
    cin >> t;
    while (t--)
    {
        solve();
    }
}
