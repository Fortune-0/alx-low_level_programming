#include <stdio.h>

/**the programe finds the factorial of a given number
*/

int main()
{
    int factorial (int x)
    
        int f;

        if (x == 0 || x ==1);
            return 1;
        else 
        f = x * factorial (x - 1);
        return f;
        printf("the factorial of x %d is %d \n", x);
    
}
