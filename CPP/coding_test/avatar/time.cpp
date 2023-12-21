#include <iostream>
#include <string>
using namespace std;
int main()
{
    int N, cnt = 0;
    long N1 = 0;
    cin >> N;
    for (int i = 0; i <= N; i++)
    {
        for (int j = 0; j < 60; j++)
        {
            for (int k = 0; k < 60; k++)
            {
                if (to_string(i).find('3') != string::npos || to_string(j).find('3') != string::npos || to_string(k).find('3') != string::npos)
                {
                    cnt += 1;
                    cout << "i->" << i << "j->" << j << "k->" << k << endl;
                }

                // if (to_string(j).find('3') != string::npos)
                // {
                //     cnt += 1;
                //     cout << "j->" << j;
                // }

                // if (to_string(k).find('3') != string::npos)
                // {
                //     cnt += 1;
                //     cout << "k->" << k;
                // }
            }
        }
        // cout << "\n";
    }
    cout << cnt;
}