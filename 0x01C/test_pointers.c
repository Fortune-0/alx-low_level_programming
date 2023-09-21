#include <stdio.h>

int main()

{
    int *i = 73;
    int j = &i;

printf("the address of i is %d\n", &i);
printf("the value of i is %d\n", i);
printf("The address of i stored in  j is %u\n", j);
return 0;
}

