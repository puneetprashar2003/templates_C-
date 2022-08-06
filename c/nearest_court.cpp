#include <iostream>
using namespace std;
#include<vector>
int main(void) {
    	int tests,n,x,y,a,b;
	int inp;
	int mean=0;
	vector<int > vl={};
	cin>>tests;
	while(tests--)
	{
	    for(int i=0;i<2;i++)
	  {cin>>inp;
	  vl.push_back(inp);}
	  mean=(vl.at(0)+vl.at(1))/2;
	  if((abs(vl.at(0)-mean))>(abs(vl.at(1)-mean)))
	  cout<<abs(vl.at(0)-mean)<<endl;
	  else
	  cout<<abs(vl.at(1)-mean)<<endl;
	  vl={};}
	  
	return 0;
}