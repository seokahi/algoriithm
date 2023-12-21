#include <iostream>

using namespace std;
int arr[1001][1001] = {
    0,
};
int n, m;
bool dfs(int x, int y)
{
    if (x <= -1 || x >= n || y <= -1 || y >= m)
    {
        return false;
    }
    if (arr[x][y] == 0)
    {
        arr[x][y] = 1;
        dfs(x, y - 1);
        dfs(x, y + 1);
        dfs(x - 1, y);
        dfs(x + 1, y);
        return true;
    }
    return false;
}

int main()
{
    int result = 0;
    cin >> n >> m;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%1d", &arr[i][j]);
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (dfs(i, j) == true)
            {
                result += 1;
            }
        }
    }

    cout << result;
}