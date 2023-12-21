#include <iostream>
#include <String>
using namespace std;

int main()
{
    int n;
    int x = 1, y = 1;
    cin >> n;
    string s;
    cin.ignore();
    getline(cin, s);
    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] == 'R')
        {
            if (y + 1 < n + 1)
            {
                y += 1;
            }
        }
        else if (s[i] == 'L')
        {
            if (y - 1 > 0)
            {
                y -= 1;
            }
        }
        else if (s[i] == 'U')
        {
            if (x - 1 > 0)
            {
                x -= 1;
            }
        }
        else if (s[i] == 'D')
        {
            if (x + 1 < n + 1)
            {
                x += 1;
            }
        }
    }
    cout << x << " " << y;
}
