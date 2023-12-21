#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr, vector<vector<int>> queries)
{
    vector<int> answer;
    int min = 1000001;
    for (auto n : queries)
    {
        min = 1000001;
        for (int i = n[0]; i <= n[1]; i++)
        {
            if (arr[i] > n[2])
            {
                if (arr[i] < min)
                {
                    min = arr[i];
                }
            }
        }
        if (min == 1000001)
            answer.push_back(-1);
        else
            answer.push_back(min);
    }
    return answer;
}