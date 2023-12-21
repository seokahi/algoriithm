#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int array[] = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};
    for (int i = 0; i < 10; i++)
    {
        int min_index = i;
        for (int j = i + 1; j < 10; j++)
        {
            if (array[min_index] > array[j])
            {
                min_index = j;
            }
        }
        swap(array[i], array[min_index]);
    }
    for (int i = 0; i < 10; i++)
    {
        cout << array[i] << " ";
    }
}