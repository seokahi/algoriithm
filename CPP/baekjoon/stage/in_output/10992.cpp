#include <iostream>

using namespace std;
int main()
{
    int N;
    cin >> N;
    for (int i = 1; i <= N; i++)
    {
        if (i == N)
        {
            for (int j = 1; j <= 2 * N - 1; j++)
            {
                cout << "*";
            }
            return 0;
        }
        for (int j = N - i; j > 0; j--)
        {
            cout << " ";
        }
        cout << "*";
        if (i != 1)
        {
            for (int j = 0; j < 2 * i - 3; j++)
            {
                cout << " ";
            }
            cout << "*";
        }
        cout << "\n";
    }

    return 0;
}