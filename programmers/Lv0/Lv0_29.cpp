#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr, vector<vector<int>> queries)
{
    vector<int> answer;
    int temp = 0;
    for (auto a : queries)
    {
        temp = arr[a[0]];
        arr[a[0]] = arr[a[1]];
        arr[a[1]] = temp;
    }
    answer = arr;
    return answer;
}