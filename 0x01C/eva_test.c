#include <stdio.h>
#include<conio.h>
#include <dos.h>
int main()

{
    char i[20];
    void textcolor(int color);
    textcolor(2);

    printf("Enter name in capital=");
    scanf("%s", &i);
    for (int j=1; j<=20; j++)
    //j + 1 = j
    {
        printf("Happy birthday%s \2\n",i);
    }
}