#include <bits/stdc++.h>

using namespace std;
vector<int> v1;
int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        v1.push_back(x);
    }
    sort(v1.begin(), v1.end(), greater<>());
    for (int i = 0; i < n; i++)
    {
        cout << v1[i] << " ";
    }
}