#include<iostream>
using namespace std;
void solve(){
   int  i, j, n,m=0, k=0, p=0, q=0;
   i=0,j=0;
  char ch;
  string str="";
  string str1="";
  cin>>n;
  
  cin>>str1;
  for(i=0;i<n;i++)
  {
   
  
    if (str1[i]=='1')
    j++;
    else
    k++;
  } 
  
  if(k>j)
  for(int i=0;i<k;i++)
  {str=str+"0";}
  else
  for(int i=0;i<j;i++)
  {str=str+"1";}

  cout<<str<<endl;
}
int main()
{ int t;
  cin>>t;
  while(t--)
  {
   solve();
  }
}