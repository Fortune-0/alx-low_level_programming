#include <stdio.h>

int main()

{
    int i;
    int j;
    int a[] =  {3, 7, 2, 0, 4, 8, 1};
    int length = 7;

    for (i = 0; i < length; i++)
    {
        for (j = 0; j < (length - 1); j++)
        {
            if (a[j] > a[j + 1])
            {
                int temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }
        }
    }
for (i = 0; i < length; i++)
    printf("a[%d] = %d\n", i, a[i]);
    return 0;
}