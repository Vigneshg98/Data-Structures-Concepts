#include<bits/stdc++.h>
using namespace std;

void nge(int arr[],int n)
{
    stack <int> s;
    int i,ele,next;

    s.push(arr[0]);

    for(i=1;i<n;i++)
    {
        next=arr[i];
        if(!s.empty())
        {
            ele=s.pop();

            while(ele<next)
            {
                cout<<ele<<"--"<<next;
                if(s.empty())
                  break;
                ele=s.pop();
            }
            if(ele>next)
              s.push(ele);
        }
        s.push(next);
    }
    while(!s.empty())
    {
        ele=s.pop();
        next=-1;
        cout<<ele<<"--"<<next;
    }
}

int main()
{
    int arr[]={11,13,21,3};
    int n = sizeof(arr)/sizeof(arr[0]);
    nge(arr, n);
    return 0;

}
