#include  <iostream>
using namespace std;
class Students

{
    public:
    static int subject_code;
    void static display_code()
    {
        cout<<subject_code<<endl;
    }
};
int Students::subject_code;

int main()
{
    Students::subject_code=13;
    Students::display_code();
    return 0;
}
/*static variables can be declared outside only outside class and 
static functions are declared inside class only .inside static functions 
only static variables can be used 
*/