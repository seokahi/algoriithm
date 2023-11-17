#include <bits/stdc++.h>

using namespace std;
int main()
{
    cout << "생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요" << endl;
    int n;
    string s;
    cin >> n >> s;
    vector<string> v1;
    int cnt = 0;
    cout << "앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다" << endl;
    for (int i = 0; i < n; i++)
    {
        string ss;
        cin >> ss;
        v1.push_back(ss);
    }
    for (int i = 0; i < n; i++)
    {
        if (s != v1[i])
            cnt += 1;
        else
        {
            cnt += 1;
            cout << cnt;
            break;
        }
    }
}