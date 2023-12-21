#include <iostream>
#include <vector>

using namespace std;
vector<int> a[15];
int cnt = 0;
int ni = 0;
int result = 0;
int main()
{
    int test_case;
    cin >> test_case;
    for (int t = 0; t < test_case; t++)
    {
        int n, m;
        cin >> n >> m;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                int x;
                cin >> x;
                v1[i].push_back(x);
            }
        }
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
            }
        }
        cout << "#" << test_case << " " << result;
    }
}