#include <iostream>
#include <bits/stdc++.h>
using namespace std;


int main() {
	int t;
	cin>>t;
	while(t--){
	    int n;
	    double k;
	    cin>>n>>k;
	    double arr[n], sum=0, cnt=0;
	    for(int i=0;i<n;i++) cin>>arr[i];
	    sort(arr,arr+n);
	    for(int i=0;i<n;i++){
	        sum+=arr[i];
	        if(sum<=k) cnt++;
	        else{
	            sum-=arr[i];
	            arr[i]/=2;
	            double x = ceil(arr[i]);
	            sum+=x;
	            if(sum<=k) cnt++;
	            break;
	        }
	    }
	    cout<<cnt;
	    
	    cout<<'\n';
	}
	return 0;
}
