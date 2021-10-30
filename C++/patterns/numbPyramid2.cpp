#include <iostream>
using namespace std;

int main()
{

    int n;
    cin >> n;
    int gap = n - 1;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= gap; j++)
        {
            cout << " ";
        }
        gap--;
        for (int j = 1; j <= i; j++)
        {
            cout << j << " ";
        }
        cout << endl;
    }

    return 0;
}