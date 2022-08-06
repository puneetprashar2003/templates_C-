#include <iostream>
using namespace std;
int main()
{
    int num[5]={1,2,3,4,5};
    int *ptr;
    for(ptr=num;ptr<=&num[4];ptr++)
    {
cout<<*ptr<<endl;}
return 0;
    }