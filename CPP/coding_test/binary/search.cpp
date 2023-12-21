#include <bits/stdc++.h>
using namespace std;

int binarySerach(vector<int> &arr, int target, int start, int end)
{
    while (start <= end)
    {
        int mid = (start + end) / 2;
        if (arr[mid] == target)
        {
            return 1;
        }
        else if (arr[mid] > target)
            end = mid - 1;
        else
            start = mid + 1;
    }
    return -1;
}
int main()
{
    int n;
    cin >> n;
    vector<int> v1;
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        v1.push_back(x);
    }
    sort(v1.begin(), v1.end());
    int m;
    cin >> m;
    vector<int> v2;
    for (int i = 0; i < m; i++)
    {
        int x;
        cin >> x;
        v2.push_back(x);
    }
    for (int i = 0; i < m; i++)
    {
        int result = binarySerach(v1, v2[i], 0, n - 1);
        if (result == -1)
            cout << "no ";
        else
            cout << "yes ";
    }
}