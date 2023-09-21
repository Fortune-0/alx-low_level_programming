#include <stdio.h>
//#include <math.h>

int main ()
{
    int n;

    printf("Enter the value of n here\n");
    scanf("%d", &n);
    

    for (int i = 0; i < 11; i++)
    {
        printf("%d X %d = %d\n", n, i, n*i);
    }
    return(0);
    
}