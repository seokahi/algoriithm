#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list)
{
    int answer = 0;
    int mul = 1;
    int sum = 0;
    for (int num : num_list)
    {
        mul *= num;
        sum += num;
    }
    if (mul < sum * sum)
        answer = 1;
    else
        answer = 0;
    return answer;
}