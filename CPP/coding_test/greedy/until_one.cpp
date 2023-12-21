#include <iostream>

using namespace std;
int main()
{
    int N, M;
    cin >> N >> M;
    int cnt = 0;
    // while (N != 1)
    // {
    //     if (N % M == 0)
    //     {
    //         N = N / M;
    //         cnt += 1;
    //     }
    //     else
    //     {
    //         N -= 1;
    //         cnt += 1;
    //     }
    // }
    while (1)
    {
        int target = (N / M) * M;
        ;
        cnt += N - target;
        N = target;
        if (N < M)
            break;
        N /= M;
        cnt += 1;
    }
    cnt += (N - 1);
    cout << cnt;
}