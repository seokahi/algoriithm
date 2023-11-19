#include <iostream>
#include <queue>
using namespace std;

vector<int> v1[9];
bool visited[9];

void bfs(int x)
{
    queue<int> q;
    q.push(x);
    visited[x] = true;
    while (!q.empty())
    {
        int x = q.front();
        q.pop();
        cout << x << " ";
        for (int i = 0; i < v1[x].size(); i++)
        {
            int y = v1[x][i];
            if (!visited[y])
            {
                q.push(y);
                visited[y] = true;
            }
        }
    }
}

int main()
{
    v1[1].push_back(2);
    v1[1].push_back(3);
    v1[1].push_back(8);

    v1[2].push_back(1);
    v1[2].push_back(7);

    v1[3].push_back(1);
    v1[3].push_back(4);
    v1[3].push_back(5);

    v1[4].push_back(3);
    v1[4].push_back(5);

    v1[5].push_back(3);
    v1[5].push_back(4);

    v1[6].push_back(7);

    v1[7].push_back(2);
    v1[7].push_back(6);
    v1[7].push_back(8);

    v1[8].push_back(1);
    v1[8].push_back(7);
    bfs(1);
}