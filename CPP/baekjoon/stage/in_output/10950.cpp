#include <iostream>

using namespace std;

int main()
{
    int n, A, B;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> A >> B;
        // cout은 따로 개행을 해주지 않음
        cout << A + B << '\n';
    }
    return 0;
}