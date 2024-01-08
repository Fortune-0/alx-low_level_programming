//What does this code print?
void print(int nb)
{
    printf("%d", nb);
    -- nb;
    if (nb > 0) 
    {
        print(nb);
    }
}

int main(void)
{
    print(4);
    return (0);
}
/**typedef dog dog_t;
struct dog
{
	char = *name;
	float = age;
	char = *owner;
};

void print_dog(struct dog *d);
/** #include "main.h"
//#include <stdio.h>

/**
 * print_number - prints an integer n
 *@n: integer to be printed
 */
/**void print_number(int n)
{/**
	unsigned int n1;

	if (n < 0)
	{
		n1 = -n;
		_putchar('-');
	} else
	{
		n1 = n;
	}

	if (n1 / 10)
	{
		print_number(n1 / 10);
	}

	_putchar((n1 % 10) + '0');
}
*/