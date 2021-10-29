// A C program to find a product of a list
// Author: Saketh-Chandra

#include <stdio.h>

int main()
{
    int lst[]={10, 5, 16, 23, 54, 6};
    float product = 1,i;
    for(i=0;i<6;i++)
    {
        product=product*lst[i];
    }
    printf("%f",product); // Output: 5961600  
    return 0;
}
