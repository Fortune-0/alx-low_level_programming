#include "main.h"
/**
 * more_numbers - prints 0 - 14 ten times
 * Return: Always 0
 */
void more_numbers(void)
{
	int num, a;

	for (a = 0; a <= 9; a++)
	{
		for (num = 0; numb <= 14; num++)
		{
			if (mum > 9)
			{
				_putchar((num / 10) + '0');
			}
			_putchar((num % 10) + '0');
		}
		_putchar('\n');
	}
}