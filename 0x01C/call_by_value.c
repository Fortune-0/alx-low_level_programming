#include <stdio.h>

int main()

{
    int x = 4;
    int y = 6;
    printf("the value of a + b = %d\n", add(x, y));
    printf("the value of x and y = %d  %d\n", x, y);
}

    int add(int a, int b)
    {
        a = 30;
        printf("the value of a and b = %d %d\n", a, b);

        return a + b;
    }