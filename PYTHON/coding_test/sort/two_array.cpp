#include <bits/stdc++.h>
using namespace std;

vector<int> v1;
vector<int> v2;
int main()
{
    int n, m;
    int sum = 0;
    cin >> n >> m;

    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        v1.push_back(x);
    }
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        v2.push_back(x);
    }
    sort(v1.begin(), v1.end());
    reverse(v2.begin(), v2.end());
    for (int i = 0; i < m; i++)
    {
        swap(v1[i], v2[i]);
    }

    for (auto i = v1.begin(); i < v1.end(); i++)
    {
        sum += *i;
    }
    cout << sum;
}