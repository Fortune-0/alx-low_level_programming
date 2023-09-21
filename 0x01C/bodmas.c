#include <stdio.h>
#include <math.h>
/*take input from user and perform bodmas on it*/

int bodmas(int a, int b);

int main()

{
    printf("enter an arithmetic express ""no spaces""\n");
    int val1, val2, val3, val4;
    char operator, operator1, operator2, operator3;

    scanf("%d%c%d%c%d", &val1, &operator, &val2, &operator1, &val3);
    switch (operator, operator1)
    {
    //case '*':
        //printf("answer = %d\n", val1 * val2);
        //break;
    case '/':
        printf(" answer = %d\n", val1 / val2);
        break;
    case '*':
        printf(" answer = %d\n", val1 * val2);
        break;
    case '+':
        printf(" answer = %d\n", val1 + val2);
        break;
    case '-':
        printf(" answer = %d\n", val1 - val2);
        break;
    case '%':
        printf(" answer = %d\n", val1 % val2);
        break;
    default:
    printf("operator is invalid");
        break;
    }
    return 0;
}
/*{
    int a;
    int b;

    printf("input the value for A\n", a);
    scanf("%d", &a);
    printf("Input the value for B\n", b);
    scanf("%d", &b);
    
    printf("The result of a * b is %d \n", bodmas (a , b));
    printf("The result of a / b is %d \n", bodmas (a , b));
    printf("The result of a * b is %d \n", bodmas (a , b));
    printf("The result of a + b is %d \n", bodmas (a , b));
    printf("The result of a - b is %d \n", bodmas (a , b));
}

int bodmas(int a, int b)
{
    return (a * b);
    printf("The result of a * b is %d \n", bodmas (a , b));
    return (a / b);
    printf("The result of a / b is %d \n", bodmas (a , b));
    return (a * b);
    printf("The result of a * b is %d \n", bodmas (a , b));
    return (a + b);
    printf("The result of a + b is %d \n", bodmas (a , b));
    return (a - b);
    printf("The result of a - b is %d \n", bodmas (a , b));

}*/