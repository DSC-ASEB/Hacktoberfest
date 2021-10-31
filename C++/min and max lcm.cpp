You are given two positive integers X and K.

You have to output the minimum and maximum value of LCM(i,j) where X≤i<j≤X⋅K.

We define LCM(i,j) for two positive integers i and j as the minimum positive integer y such that both i and j divide y without remainder.
  
  INPUT FORMAT
  first line contains no of test cases
  next line conatains two spaced integrs x and k
  
  OUTPUT FORMAT
  For each testcase, output two space separated integers - the minimum and maximum possible value respectively of LCM(i,j) where X≤i<j≤X⋅K.
  
  Code is given below
  #include <bits/stdc++.h>
using namespace std;
int main(){
int t=1;
cout<<"Enter the number of test cases";
cin>>t;
while(t--){
    int a,k,b;
    cout<<"Enter the value of n and k respectively";
    cin>>a>>k;
    int min=0;
    b=a*k;
    int max=b*(b-1);
    if(a*2<=a*k){ 
    min=a*2; 
} 
else if(a%2!=0){ 
    min=a*(a+1); 
} 
else{ 
    min=a*(a+2); 
}
cout<<"min is:";
cout<<min<<endl;
cout<<"maximum is : "<<max<<endl;
}
return 0;
}
