#include <stdio.h>

int main()
{
    int week;
    printf("Enter the day of the week, between monday - friday\n");
    scanf("%d", &week);

    switch (week)
    {
    case 1:
        printf("monday");
       
        break;
    default:
        printf("pro gamer\n");
    break;
    }
    char art[30];
    printf(" input character\n");
    //scanf("%s", &art);
    // scanf can only handle one string at time
    gets(art);

    /*case 2:
        printf("tuesday");
        break;
    
    default:
    
        break;
        printf("%d", week);
    }*/
}