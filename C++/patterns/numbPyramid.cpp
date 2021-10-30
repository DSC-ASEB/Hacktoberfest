#include <iostream>
using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("../input.txt", "r", stdin);
    freopen("../output.txt", "w", stdout);
#endif

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
            cout << i << " ";
        }
        cout << endl;
    }

    return 0;
}