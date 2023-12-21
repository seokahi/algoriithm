#include <string>
#include <vector>

using namespace std;

int solution(int a, int b)
{
    int answer = 0;
    string c = to_string(a) + to_string(b);
    string d = to_string(b) + to_string(a);
    if (c > d)
        answer = stoi(c);
    else
        answer = stoi(d);
    return answer;
}