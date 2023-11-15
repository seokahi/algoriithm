#include <bits/stdc++.h>

using namespace std;

int n, target;
vector<int> arr;
int binarySerach(vector<int> &arr, int target, int start, int end)
{
    if (start > end)
        return -1;
    int mid = (start + end) / 2;
    if (arr[mid] == target)
        return mid;
    else if (arr[mid] > target)
        return binarySerach(arr, target, start, mid);
    else
        return binarySerach(arr, target, mid + 1, end);
}

int main()
{
    cin >> n >> target;
    // 전체 원소 입력받기
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        arr.push_back(x);
    }
    int result = binarySerach(arr, target, 0, n - 1);
    if (result == -1)
    {
        cout << "원소가 존재하지 않습니다." << '\n';
    }
    else
    {
        cout << result + 1 << '\n';
    }
}