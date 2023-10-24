#include <string>
#include <vector>

using namespace std;

int solution(string number)
{
    int answer = 0;
    int sum = 0;
    int num = 0;
    for (char ch : number)
    {
        num = ch - '0';
        sum += num;
    }
    answer = sum % 9;
    return answer;
}