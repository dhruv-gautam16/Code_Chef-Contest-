#include <iostream>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        
        string s;
        cin>>s;
        int x=0,y=0;
        for(int i=0;i<n;i++)
        {
            if(s[i]=='0')
            {
                x++;
            }
            else
            {
                y++;
            }
        }
        if(n%2==0){
            if(x==y){
                cout<<"YES"<<endl;
            }
            else if(x%2==0 && y%2==0){
                cout<<"YES"<<endl;
            }
            else{
                cout<<"NO"<<endl;
            }
            
        }
        else{
            cout<<"YES"<<endl;
        }
    	
}
return 0;
}
