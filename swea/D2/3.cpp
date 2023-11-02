#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    vector<int> s1[m];
    if (m < 1)

    {
        s1[0].push_back(1);
    }

    else if (m < 2)
    {
        s1[0].push_back(1);
        s1[1].push_back(1);
        s1[1].push_back(1);
    }
    else
    {
        s1[0].push_back(1);
        s1[1].push_back(1);
        s1[1].push_back(1);

        for (int i = 2; i < m; i++)
        {
            for (int j = 0; j <= i; j++)
            {
                if (j == 0 || j == i)
                {
                    s1[i].push_back(1);
                    continue;
                }
                else
                {
                    s1[i].push_back(s1[i - 1][j - 1] + s1[i - 1][j]);
                }
            }
        }
    }

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < s1[i].size(); j++)
        {
            cout << s1[i][j];
            ;
        }
        cout << "\n";
    }
}
