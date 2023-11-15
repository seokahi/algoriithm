#include <bits/stdc++.h>

using namespace std;
int n, target;
vector<int> arr;

int binarySearch(vector<int> &arr, int target, int start, int end)
{
    while (start <= end)
    {
        int mid = (start + end) / 2;
        if (arr[mid] == target)
            return mid;
        else if (arr[mid] > target)
            end = mid - 1;
        else
            start = mid + 1;
    }
}

int main()
{
    cin >> n >> target;
    // 전체 원소 입력 받기
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        arr.push_back(x);
    }
    // 이진 탐색 수행 결과 출력
    int result = binarySearch(arr, target, 0, n - 1);
    if (result == -1)
    {
        cout << "-1";
    }
    else
    {
        cout << result;
    }
}