#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
	    long long n,x;
	    cin>>n>>x;
	    long long a=0, b=0, c=0;
	    if(x%3==0){
	        a+=(x/3);
	    }
	    else if(x%3==1){
	        a+=(x/3)+1;
	        b+=2;
	        
	    }
	    else if(x%3==2){
	        a+=(x/3)+1;
	        b++;
	    }
	    
	    if(a+b<=n){
	        cout<<"YES"<<endl;
	        cout<<a<<" "<<b<<" "<<n-a-b<<endl;
	    }
	    else{
	        cout<<"NO"<<endl;
	    }
	}
	return 0;
}
