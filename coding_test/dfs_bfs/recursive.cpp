#include <iostream>

using namespace std;
int factorial_iteractive(int num)
{
    if (num <= 1)
    {
        return 1;
    }
    return num * factorial_iteractive(num - 1);
}

int main()
{
    int m = factorial_iteractive(5);
    cout << m;
}