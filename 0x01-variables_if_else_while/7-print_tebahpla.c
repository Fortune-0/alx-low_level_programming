#include <stdio.h>
/**
 * main - print all alphabets in lower case and in reverse
 * Reverse: Always 0
 */
int main(void)
{
	char letter;

	for (letter = 'z'; letter >= 'a'; letter--)
	putchar(letter);
	putchar('\n');
	return (0);
}
