#include <string>
#include <vector>

using namespace std;

int solution(int a, int b)
{
    int answer = 0;
    string c = to_string(a) + to_string(b);
    int d = 2 * a * b;
    if (stoi(c) > d)
        answer = stoi(c);
    else
        answer = d;
    return answer;
}