#include <iostream>
#include <vector>
#include <stack>
using namespace std;
int main()
{
    // /* vector 이용 */
    // vector<int> v1;
    // v1.push_back(5);
    // v1.push_back(2);
    // v1.push_back(3);
    // v1.push_back(7);
    // v1.pop_back();
    // v1.push_back(1);
    // v1.push_back(4);
    // v1.pop_back();

    // for (auto i = v1.begin(); i < v1.end(); i++)
    // {
    //     cout << *i << " ";
    // }
    // cout << "\n";
    // for (auto i = v1.end() - 1; i >= v1.begin(); i--)
    // {
    //     cout << *i << " ";
    // }
    // /* stack 이용 */
    stack<int> s;
    s.push(5);
    s.push(2);
    s.push(3);
    s.push(7);
    s.pop();
    s.push(1);
    s.push(4);
    s.pop();
    while (!s.empty())
    {
        cout << s.top() << " ";
        s.pop();
    }
}