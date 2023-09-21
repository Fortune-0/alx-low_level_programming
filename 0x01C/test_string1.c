#include <stdio.h>

/*char main()
{
    char arr[] = "fortune";
    //arr [] = "fortune";
    printf("arr 0 = %s\n", arr);

    return 0;
}*/
//char main()
//{
    //char art[10] = "favour";
    //for (char i = 0; i < 9; i++)
    //{
    //    printf("%c\n", art[i]);
    //}
    //return 0;
//}
/*char main()

{
    char art[30];
    printf(" input character\n");
    //scanf("%s", &art);
    // scanf can only handle one string at time
    gets(art);
    // gets allows u to input multi word in c, Gets writes to stdin
    
    //puts prints the sstring then move the cursor to next line
    //puts(art);

    
    //for (char i = 0; i < 9; i++) 
    //{
        printf("your name is %s\n", art);
    //}
    return 0;
}*/

char main()
{
    char arr[] = "fortune";
    for (char i = 0; i < 7; i++)
    {
        arr[i] ++;
        //it is now encrypted
        arr[i] --;
        //it is now decrypted
    }
    printf("it is now different %s\n", arr);
{


