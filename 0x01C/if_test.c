#include <stdio.h>

int main()
 

{
    int i;

    {
       printf("Enter the value ""n"" here\n");
    scanf("%d\n", &i);
    };

    if (i<=30)
        {
            printf("I is less than 30\n", i);
        }

        else
        
        {
            printf("I is greater than 30\n", i++);
        }
}