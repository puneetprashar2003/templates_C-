#include<iostream>
using namespace std;
class Complex{
    public:double sum_r=0.0;
    double sum_i=0.0;
    Complex(double real,double imaginary)
    {
        double r=real;
        double i=imaginary;
       void sumation()
       {
    sum_r=sum_r+r;
    sum_i=sum_i+i;
    cout<<sum_i;
    }
   
    
};
int main()
{
    Complex n1(1.45,9.36);
    Complex n2(1.0,9.36);

}
