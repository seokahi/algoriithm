#include <iostream>
#include <string>
using namespace std;

int main()
{
    int result = 0;
    int dx[] = {-2, -2, 2, 2, -1, 1, -1, 1};
    int dy[] = {-1, 1, -1, 1, -2, -2, 2, 2};
    string w;
    cin >> w;
    int row = w[0] - 'a' + 1;
    int column = w[1] - '0';
    for (int i = 0; i < 8; i++)
    {
        int x = row + dx[i];
        int y = column + dy[i];
        if (x >= 1 && x <= 8 && y >= 1 && y <= 8)
        {
            result += 1;
        }
    }
    cout << result;
}