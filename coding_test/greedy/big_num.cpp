#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    vector<int> v1;
    int N, M, K, num;
    // int sum = 0, cnt = 0;

    cin >> N >> M >> K;
    int idx = N - 1;
    for (int i = 0; i < N; i++)
    {
        cin >> num;
        v1.push_back(num);
    }
    sort(v1.begin(), v1.end());
    int first = v1[N - 1];
    int second = v1[N - 2];
    int cnt = (M / (K + 1)) * K;
    cnt += M % (K + 1);

    int result = 0;
    result += cnt * first;
    result += (M - cnt) * second;
    cout << result;
    // for (int i = 0; i < M; i++)
    // {
    //     if (cnt == 0)
    //     {
    //         idx = N - 1;
    //     }
    //     if (cnt != K)
    //     {
    //         sum += v1[idx];
    //         cnt++;
    //     }
    //     else
    //     {
    //         idx--;
    //         sum += v1[idx];
    //         cnt = 0;
    //     }
    // }

    // cout << sum;
}