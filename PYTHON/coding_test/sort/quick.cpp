#include <bits/stdc++.h>

using namespace std;

int n = 10;
int arr[10] = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};
void quicksort(int arr[], int start, int end)
{
    if (start >= end)
        return;
    int pivot = start;
    int left = start + 1;
    int right = end;
    while (left <= right)
    {
        while (left <= end && arr[left] <= arr[pivot])
            left++;
        while (right > start && arr[right] >= arr[pivot])
            right--;
        if (left > right)
            swap(arr[pivot], arr[right]);
        else
            swap(arr[left], arr[right]);
    }
    quicksort(arr, start, right - 1);
    quicksort(arr, right + 1, end);
}
int main()
{
    quicksort(arr, 0, n - 1);
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << ' ';
    }
}