#include <iostream>
using namespace std;
int main(){
    int num1=10;
    int num2=12;
    int*ptr1=&num1; 
    int*ptr2=&num2;
    int*temp;
    temp=ptr1;
    ptr1=ptr2;
    ptr2=temp;
    cout<<"num1 "<<*ptr1<<endl;
    cout<<"num2 "<<*ptr2<<endl;


return 0;
}
