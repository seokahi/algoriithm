#include <iostream>

using namespace std;
int main()
{
    int N = 1260;
    int sum = 0;
    int arr[4] = {500, 100, 50, 10};
    for (int i = 0; i < 4; i++)
    {
        sum += N / arr[i];
        N = N % arr[i];
    }
    cout << sum;
}
