#include <bits/stdc++.h>
using namespace std;

vector<pair<string, int>> v1;

bool compare(pair<string, int> a, pair<string, int> b)
{
    return a.second > b.second;
}

int main()
{
    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        string name;
        int score;
        cin >> name >> score;
        v1.push_back({name, score});
    }

    sort(v1.begin(), v1.end(), compare);
    for (int i = 0; i < N; i++)
    {
        cout << v1[i].first;
    }
}