//Daily challenge//
#include<iostream>
using namespace std;
int main()
{
  int a;
  cin >> a;
  int l[a];
  int b;
  for(int i=0;i<a;i++)
    {
      cin >> l[i];
    }
  int c=0;
  for(int i=0;i<b;i++)
    {
      for(int j=0;j<a;j++)
        {
          cout << l[c%a] << " ";
          c++;
        }
      cout << endl;
    }
}

//Daily test//
a,b,c=map(int,input().split())
l=list(map(int,input().split()))
for i in range(c):
    temp=0
    for j in range(i,b+i):
        temp+=l[j]
    l.append(temp)
    l.sort()
  
