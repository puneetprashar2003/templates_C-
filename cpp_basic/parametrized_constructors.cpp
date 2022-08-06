#include <iostream>
using namespace std;
class Car
{ 
    public:
    int gear,speed;
    
    Car(int gear_no,int top_speed )
    {
        gear=gear_no;
        speed=top_speed;
    }
};
int main()
{
    Car i20(3,90);
    Car verna(4,89);
    cout<<verna.gear<<endl;
      cout<<verna.speed<<endl;
        cout<<i20.speed<<endl;
return 0;
}//constructor is called at the time of object creation
// if a class does not have a constructor then c++ compiler automatically 
// creates  a difault constructor to assign default values 