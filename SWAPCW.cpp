#include <iostream>
#include <bits/stdc++.h>
using namespace std;


int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        string nu;
        cin>>nu;
        string temp =nu;
        sort(temp.begin(),temp.end());
        for(int i=0; i<n/2; i++){
            if(temp[i]!=nu[i]) swap(nu[i],nu[n-i-1]);
            
            
            
        }
        if(nu==temp)  cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}

