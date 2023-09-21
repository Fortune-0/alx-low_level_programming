#include <stdio.h>

int divide(int a, int b);

int main()
{
    int a;
    int b;
    a = 97;

    printf("input number to be divided by 97\n");
    scanf("%d", &b);
    printf("The result of a %/ b (97) is %u \n", divide (a , b));
    
    //if (b < 97)
    //{
    //    printf("The result of a / b (97) is %d \n", divide (a , b));
    //}

}
int divide(int a, int b)
{
    return (a & b);
}