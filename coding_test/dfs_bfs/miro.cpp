#include <iostream>
#include <vector>
#include <queue>

using namespace std;

queue<pair<int, int>> q;

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int nx = 0, ny = 0;
int n, m;
vector<int> graph[201];
int bfs(int x, int y)
{
    q.push({x, y});
    while (!q.empty())
    {
        x = q.front().first;
        y = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++)
        {
            nx = x + dx[i];
            ny = y + dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m)
            {
                continue;
            }
            if (graph[nx][ny] == 0)
            {
                continue;
            }
            if (graph[nx][ny] == 1)
            {
                graph[nx][ny] = graph[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }
}

int main()
{

    cin >> n >> m;
    // 입력
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            int s;
            cin >> s;
            graph[i].push_back(s);
        }
    }
    bfs(0, 0);
    cout << graph[n - 1][m - 1];
}