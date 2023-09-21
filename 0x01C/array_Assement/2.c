#include <stdio.h>

int main()
{
    int marks[5];
    for (int i = 0; i < 5; i++)
    {
        printf("Input the score of student %d\n", i);
        scanf("%d", &marks [i]);
    }
    
    for (int i = 0; i < 5; i++)
    {
        printf("The marks score by the students %d is %d\n", i, marks [i]);
    }
    return 0;
}