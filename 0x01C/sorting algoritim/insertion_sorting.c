#include <stdio.h>

int sort(int arry[], int o)

{
    int arry;
    int t;
    int k;
    int j;
    
    for (t=1; t<o; t++);

    k = arry[t];
    {
        int j = t-1;
        while (j>=0; && arry[j]>k)
        {
            arry[j+1] = arry[j];
        }
    }

}