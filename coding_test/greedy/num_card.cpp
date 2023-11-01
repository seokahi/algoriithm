#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    int N, M, num;
    int x;
    vector<int> v1;
    cin >> N >> M;
    int result = -1;
    // for (int i = 0; i < N; i++)
    // {
    //     v1.clear();
    //     for (int j = 0; j < M; j++)
    //     {
    //         cin >> num;
    //         v1.push_back(num);
    //     }
    //     min = *min_element(v1.begin(), v1.end());
    //     if (min > max)
    //     {
    //         max = min;
    //     }
    // }
    for (int i = 0; i < N; i++)
    {
        int min_value = 100001;
        for (int j = 0; j < M; j++)
        {
            cin >> x;
            min_value = min(x, min_value);
        }
        result = max(result, min_value);
    }
    cout << result;
}