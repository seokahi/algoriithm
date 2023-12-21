#include <bits/stdc++.h>

using namespace std;
int n, m;
vector<int> v1;
int result = 0;
int search(vector<int> &arr, int target, int start, int end)
{
    // target은 원하는 합
    // start는 0이고, end는 19가 되어야함.
    int sum = 0;
    while (start <= end)
    {
        sum = 0;
        int mid = (start + end) / 2;
        // 둘의 중간임
        for (int i = 0; i < n; i++)
        {
            if (arr[i] > mid)
            {
                sum += arr[i] - mid;
            }
        }
        if (sum >= target)
        {
            result = mid;
            start = mid + 1;
        }
        else
        {

            end = mid - 1;
        }
    }
    return result;
}
int main()
{

    cin >> n >> m;

    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        v1.push_back(x);
    }
    int max = *max_element(v1.begin(), v1.end());
    // int max_index = 0;
    // for (int i = 0; i < m; i++)
    // {
    //     if (max == v1[i])
    //     {
    //         max_index = i;
    //     }
    // }
    // cout << max_index;
    int cnt = search(v1, m, 0, max);
    cout << cnt;
}