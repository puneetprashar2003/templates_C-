#include <iostream>
using namespace std;
class Car
{
    public:
   
    int gear=6;
    void drive()
    {
        cout<<"pressing Accelerator";
    }
    //class is a blue print of objects 
};
int main()
{
    Car hyundai; //creating an object of car
    //we can also create multiple objects
Car creta , merc;
cout<<"gear "<<hyundai.gear<<endl;//accessing gear data member
hyundai.drive();//accessing function 
}
/*constructors 
a constructor has same name as that of class and does not have any return 
type for exmaple Car(). when we create an object a constructor is already created 
hence in the above code instead of using void display() we can use 
car() and the message will automatically get printed */
/* static key word
in the code whenever a  object is created it will have seperate copy of all
variables and functions for eg in
class Students{
    public:
    int subject_code;
}
now for every object created from this class will have separate copy of
subject_code . We can use static keyword in order to create only 1 copy 


 
*/
