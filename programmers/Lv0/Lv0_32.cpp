#include <string>
#include <vector>

using namespace std;

vector<int> solution(int l, int r)
{
    vector<int> answer;
    int flag = 1;
    for (int i = l; i <= r; i++)
    {
        int temp = i;
        flag = 1;
        while (temp != 0)
        {
            if (temp % 10 != 5 && temp % 10 != 0)
            {
                flag = 0;
                break;
            }
            temp /= 10;
        }
        if (flag)
            answer.push_back(i);
    }

    if (answer.size() == 0)
        answer.push_back(-1);
    return answer;
}