#include <stdio.h>

int sum(int a, int b);

int main()
{
    int a;
    int b;
    printf("input the value of a\n", a);
    scanf("%d", &a);

    printf("enter the value of b\n", b);
    scanf("%d", &b);
    printf("The result of a + b is %d \n", sum (a , b));

}

int sum(int a, int b)
{
    return (a + b);
    //printf("The result of a + b is %d and %d = %d\n", sum (a , b));
}
//{
    //system("pause");
    //return 0;
//