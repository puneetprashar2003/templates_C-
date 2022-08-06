#include <iostream>
using namespace std;
class Car
{
    public:
    int gear,speed;
    Car():gear(4),speed(200)
    {

    }

};
int main()
{
    Car car1;
    cout<<car1.speed<<endl;
    cout<<car1.gear<<endl;

return 0;
}



