#include <iostream>
#include <vector>
using namespace std;

int main() {
	int tests,n,x,y,a,b;
	int inp;
	vector<int > vl={};
	cin>>tests;
	while(tests--)
	{
	    for(int i=0;i<5;i++)
	    {
	        cin>>inp;
	        vl.push_back(inp);
	    }
       if (static_cast<double>((vl.at(1)*1.0/vl.at(3))>(vl.at(2)*1.0/vl.at(4))))
        cout<<"DIESEL"<<endl;
        else if (static_cast<double>(vl.at(1)*1.0/vl.at(3)<((vl.at(2)*1.0/vl.at(4)))))
	    cout<<"PETROL"<<endl;
        else
        cout<<"ANY"<<endl;
        
        vl={};
    }
	
	return 0;
}
