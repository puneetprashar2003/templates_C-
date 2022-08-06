#include  <iostream>
#include <cstring>
using namespace std;
int main(){
    string str1="hello";
    string str2="welcome ";
    cout<<str1.length()<<endl;
    cout<<str1.append(str2)<<endl;
    string str;
    //INPUT OF A STRING 
    cout<<"enter a string";
    //getline(cin,str);
    cout<<"the string is "+ str<<endl;
    str1.swap(str2);
    cout<<str1; 
    //c strings - in c we take strings as a an array of characters
    char str3[]="c++programming";
    cout<< strlen(str3)<<endl;
     char str4[]="hmm";
     char str5[]="hola";
     strcat(str4,str5);
     strcpy(str4,str5);
     /*function to convert string to uppercase
     toupper(str[i])
     to convert to lowercase
     tolower(str[i]) */
}