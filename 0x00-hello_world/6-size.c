#include <stdio.h>
/**
 * main -Entry
 * Return: Always 0
 */
int main(void)
{
	char acharacter;
	int ainteger;
	long along;
	long long alonglong;
	float afloat;

	printf("size of a char: %lu byte(s)\n", sizeof(acharacter));
	printf("size of an int: %lu byte(S)\n", sizeof(ainteger));
	printf("size of a long int: %lu byte(s)\n", sizeof(along));
	printf("size of a long long int: %lu byte(s)\n", sizeof(alonglong));
	printf("Size of afloat: %lu byte(s)\n", sizeof(afloat));
	return (0);
}
