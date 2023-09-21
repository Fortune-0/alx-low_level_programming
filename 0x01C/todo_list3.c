#include <stdio.h>
//#include <string.h>

int main()
{
    char todo[80];
   int days;
   
    printf("Enter the weekday\n", days);
    scanf("%d", &days);

    {
    if (days==1)
        printf("Monday");
        //printf("Enter list of things to do\n");
        //gets(todo);
        scanf("%d", &todo);
    else if (days==2)
        printf("Tuesday");
    else if (days==3)
         printf("Wednesday");
    else if (days==4)
        printf("Thursday");
    else if (days==5)
        printf("Friday");
    else if (days==6)
        printf("Saturday");
    else if (days==7)
        printf("Today is sunday go and REST");
    }
    
}