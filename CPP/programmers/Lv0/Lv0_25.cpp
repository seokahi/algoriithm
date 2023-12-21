#include <string>
#include <vector>
using namespace std;

int solution(vector<int> num_list)
{
    int answer = 0;
    string sum_even = "";
    string sum_odd = "";
    for (int num : num_list)
    {
        if (num % 2)
            sum_odd += to_string(num);
        else
            sum_even += to_string(num);
    }
    answer = stoi(sum_odd) + stoi(sum_even);
    return answer;
}