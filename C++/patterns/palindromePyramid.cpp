#include <iostream>
using namespace std;
int main()
{

    int n;
    cin >> n;

    for (int i = 1; i <= n; i++)
    {
        int k = i;
        for (int j = 1; j <= n - i; j++)
        {
            cout << "  ";
        }
        for (int j = 1; j < i; j++)
        {
            cout << k-- << " ";
        }
        for (int j = 1; j <= i; j++)
        {
            cout << k++ << " ";
        }
        for (int j = 1; j <= n + i; j++)
        {
            cout << "  ";
        }
        cout << endl;
    }

    return 0;
}