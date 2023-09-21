#include <stdio.h>

void swap(int, int);

int main()
{
    int a = 4;
    int b = 3;
    printf("value of a and b before swap %d and %d\n", a, b);
    swap(a, b);
    //printf("the value after the swap is %d and %d\n", a, b);
    return 0;
}
void swap(int a, int b)
{
    int temp;
    temp = a;
    a = b;
    b = temp;
    printf("the value after the swap is %d and %d\n", a, b);
}