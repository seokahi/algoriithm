#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<pair<int, int>> v1[3];
    v1[0].push_back({1, 7});
    v1[0].push_back({2, 5});
    v1[1].push_back({0, 7});
    v1[2].push_back({0, 5});
    for (int i = 0; i < v1.size(); i++)
    {
        for (int j = 0; j < v1[i].size(); j++)
        {
            cout << v1[i][j].first << " " << v1[i][j].second << endl;
        }
        cout << "\n";
    }
}

////////// 더 많이 쓰고 싶을 때
// #include <iostream>
// #include <vector>
// using namespace std;

// // 사용자 정의 구조체
// struct MyData
// {
//     int first;
//     int second;
//     int third;
// };

// int main()
// {
//     vector<MyData> v1[3];
//     v1[0].push_back({1, 7, 6});
//     v1[0].push_back({2, 5, 3});
//     v1[1].push_back({0, 7, 2});
//     v1[2].push_back({0, 5, 1});

//     for (int i = 0; i < 3; i++)
//     {
//         for (int j = 0; j < v1[i].size(); j++)
//         {
//             cout << v1[i][j].first << " " << v1[i][j].second << " " << v1[i][j].third << endl;
//         }
//         cout << "\n";
//     }

//     return 0;
// }
