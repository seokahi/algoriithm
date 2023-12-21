#include <string>
#include <vector>

using namespace std;

int solution(int a, int d, vector<bool> included)
{
    int answer = 0;
    int sum = a;
    for (bool flag : included)
    {
        if (flag == true)
            answer += sum;
        sum += d;
    }
    return answer;
}