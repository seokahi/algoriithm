#include <bits/stdc++.h>

using namespace std;

int main()
{
    set<int> s;
    vector<int> targets;
    int n, m;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        s.insert(x);
    }
    cin >> m;
    for (int i = 0; i < m; i++)
    {
        int target;
        cin >> target;
        targets.push_back(target);
    }
    for (int i = 0; i < m; i++)
    {
        if (s.find(targets[i]) != s.end())
        {
            cout << "yes ";
        }
        else
        {
            cout << "no ";
        }
    }
}