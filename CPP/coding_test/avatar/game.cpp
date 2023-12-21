#include <iostream>
#include <vector>
using namespace std;
int left_turn(int dirc)
{
    dirc -= 1;
    if (dirc == -1)
    {
        dirc = 3;
    }
    return dirc;
}

int main()
{
    int n, m, num, nx, ny;
    int x, y, dirc;
    int count = 1;
    int time_turn = 0;
    int arr[50][50];
    int d[50][50] = {
        0,
    };
    int dx[4] = {-1, 0, 1, 0};
    int dy[4] = {0, 1, 0, -1};

    cin >> n >> m;
    cin >> x >> y >> dirc;
    d[x][y] = 1;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> num;
            arr[i][j] = num;
        }
    }

    while (1)
    {
        dirc = left_turn(dirc);
        nx = x + dx[dirc];
        ny = y + dy[dirc];
        if (arr[nx][ny] == 0 && d[nx][ny] == 0)
        {
            x = nx;
            y = ny;
            count += 1;
            time_turn = 0;
            d[nx][ny] = 1;
        }
        else
        {
            time_turn += 1;
        }
        if (time_turn == 4)
        {
            nx = x - dx[dirc];
            ny = y - dy[dirc];
            if (arr[nx][ny] == 0)
            {
                x = nx;
                y = ny;
            }
            else
            {
                break;
            }
            time_turn = 0;
        }
    }
    cout << count;
}
