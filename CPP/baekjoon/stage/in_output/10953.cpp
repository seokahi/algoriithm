#include <iostream>
#include <string>
using namespace std;

int arr_slicing(string str, int a, int b)
{
    int num;
    string s = "";

    for (int i = a; i < b; i++)
    {
        s += str[i];
    }
    return stoi(s);
}

int main()
{
    int n, pos, A, B;
    cin >> n;

    string str;
    cin >> str;
    pos = str.find(',');
    A = arr_slicing(str, 0, pos);
    B = arr_slicing(str, pos, str.length());
    cout << A;
    return 0;
}