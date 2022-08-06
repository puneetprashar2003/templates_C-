#include <iostream>
#include<string>
using namespace std;
#include<vector>
int main(void) {
    int tests,x,y;
    int a1;
    string str1="";
    string str2="";
    int len;
    cin>>tests;
    while(tests--)
    {
        cin>>x>>y;
        len=x+y;
        
        if(x%2!=0 && y%2!=0 ||(x==1 ||y==1))
        cout<<"-1"<<endl;
        else if(x%2==0 && y%2!=0)
        {
            for(int i=0;i<len;i++)
            {   a1=y/2;
                if(i>(a1-1) && i<(len-a1) && i!=(x+y-1)/2)
                str1=str1+"a";
                else
                str1=str1+"b";
            }
         for (int j=0;j<len;j++)
         { a1=x/2;
           if(j>(a1-1) && j<(len-a1))
           str2=str2+"b";
           else 
           str2=str2+"a";

         }
         cout<<str1<<endl;
         cout<<str2<<endl;
        }
        else if(x%2!=0 && y%2==0 &&(x!=1 ||y!=1 ))
        {
            for(int i=0;i<len;i++)
            {  a1=x/2;
           if(i>(a1-1) && i<(len-a1) && i!=(len-1)/2)
           str1=str1+"b";
           else 
           str1=str1+"a";
            }
         for (int j=0;j<len;j++)
         { a1=y/2;
           if(j>(a1-1) && j<(len-a1))
           str2=str2+"a";
           else 
           str2=str2+"b";

         }
         cout<<str1<<endl;
         cout<<str2<<endl;
        }
        else if(x%2==0 && y%2==0 &&(x!=1 ||y!=1 ))
        {
            for(int i=0;i<len;i++)
            {   a1=x/2;
           if(i>(a1-1) && i<(len-a1))
           str1=str1+"b";
           else 
           str1=str1+"a";}
         for (int j=0;j<len;j++)
         { a1=y/2;
           if(j>(a1-1) && j<(len-a1))
           str2=str2+"a";
           else 
           str2=str2+"b";

         }
         cout<<str1<<endl;
         cout<<str2<<endl;
        }
        str1="";
        str2="";
        x=0,y=0;

    }
    return 0;
}