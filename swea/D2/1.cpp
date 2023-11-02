#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    int N;
    string s;
    int cnt = 0;
    cin >> N;

    for (int i = 1; i <= N; i++)
    {
        cnt = 0;
        s = to_string(i);
        for (int j = 0; j < s.size(); j++)
        {
            if (s[j] == '3' || s[j] == '6' || s[j] == '9')
            {
                cnt += 1;
            }
        }
        if (s.size() == cnt)
        {
            for (int k = 0; k < cnt; k++)
            {
                cout << "-";
            }
            cout << " ";
        }
        else if (s.size() != cnt && cnt != 0)
        {
            cout << "- ";
        }
        else
        {
            cout << s << " ";
        }
    }
}