
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr, vector<vector<int>> queries)
{
    vector<int> answer;
    for (auto n : queries)
    {
        for (int i = n[0]; i <= n[1]; i++)
        {
            if (i % n[2] == 0)
            {
                arr[i] += 1;
            }
        }
    }
    answer = arr;
    return answer;
}