#include <stdio.h>

int main()

{
    int j;
    int arr[10];
    printf("input the value of j here\n");
        scanf("%d", &j);
    for (int i = 0; i < 10; i++)
    {
        arr[i] = j * (i+1);
        printf("the value of j %d * %d = %d\n", j, (i+1), arr[i]);
    }
    
}