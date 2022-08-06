#include <iostream>
using namespace std;
int main()
{ int n ;
//cout<<"enter the value of n";
    cin>>n;
     int *ptr=new int[n];
     //cout<<"enter the elements of array";
     for(int i=0;i<n;i++)
     {
         cin>>*(ptr+i);
     }
     int largest=*ptr;
     for(int i=0;i<n;i++)
     {
         if(*(ptr+i)>largest)
        {
             largest=*(ptr+i);
        }

     }
     cout<<largest;
     return 0;
}