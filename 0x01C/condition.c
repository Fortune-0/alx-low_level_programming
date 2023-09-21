#include <stdio.h>
/* check if fortune is a boy*/
int main()
{
    int x;
    int y;
    printf("enter your number\n");
    scanf("%d\n", &x);

    
    printf("enter your number\n"); 
    scanf("%d\n", &y);
    
    {
        printf("the value of x+y is %d + %d = %d\n", x, y, x+y);
    }
    if (x+y>20)
    printf("therefore x+y is greater than 20");

    else
    {
        printf("x+y is less than 20");
    }
    //return 0;
}