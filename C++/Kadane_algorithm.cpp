#include <bits/stdc++.h>
using namespace std;
int main(){
int t=1;
cin>>t;
while(t--){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
        cin>>arr[i];
    int maximum=0,current=0;
    for(int i=0;i<n;i++)
    {
        current=current+arr[i];
        if(current>maximum)
        maximum=current;
        if(current<0)
        current=0;
    }
    cout<<maximum<<endl;
}
return 0;
}
