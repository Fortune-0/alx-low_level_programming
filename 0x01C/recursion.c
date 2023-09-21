#include <stdio.h>

int main()
{
    int sum(int n);

    int number, results;
    printf("Enter postive integer:\n");
    scanf("%d", &number);

    results = sum(number);

    printf("sum = %d", results);

    return 0;
}
    
        int sum(int n)
        {
            if (n != 0)
            {
            return n + sum(n-1);
            }

        else
        {
            return n;
        }
}