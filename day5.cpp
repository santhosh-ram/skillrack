//Daily challenge//
#include<iostream>
#include<vector>
#include<numeric>
#include<algorithm>
using namespace std;
int main()
{
  int n;
  cin >> n;
  vector<int> l(n);
  for(int i=0;i<n;i++)
    {
      cin >> l[i];
    }
  for(int i=0;i<n/6;i++)
    {
      vector<int> z(l.begin()+i*6,l.begin()+(i+1)*6);
      rotate(z.begin(),z.begin()+3,z.end());
      for(int j=0;j<3;j++)
        {
          cout << accumulate(z.begin()+j*2,z.begin()+(j+1)*2,0) << " ";
        }
    }
  return 0;
}
//Daily Test//
#include<iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    int l[n];
    for(int i=0;i<n;i++)
    {
        cin >> l[i];
    }
    int count=0,a,b;
    for(int i=0;i<n-1;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            if(l[i]>l[j])
            {
                count++;
                a=l[i];
                b=l[j];
            }
        }
    }
    cout << count << endl;
    cout << a << " " << b;
}













