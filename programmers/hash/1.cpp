#include <iostream>
#include <vector>
#include <set>
#include <string>
using namespace std;

int main()
{
    bool status = true;
    set<string> s = {"123", "456", "789"};
    bool answer = true;

    for (auto it1 = s.begin(); it1 != s.end(); it1++)
    {
        for (auto it2 = it1; it2 != s.end(); it2++)
        {
            if (it1 != it2)
            {
                if (it2->find(*it1) == 0)
                {
                    answer = false;
                }
                else
                {
                    answer = true;
                    break;
                }
            }
        }
    }

    cout << boolalpha << answer << endl;

    return 0;
}