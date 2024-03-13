#include "search_algos.h"

/**
 * linear search - searching for a value in an array
 * of intergers using linear search
 * @array: A pointer to the first element of an array to search
 * @size: The number of elements in them array
 * @value: The value to search for.
 * Return: if the value is not presentor the aray is NULL
*/
int linear_search(int *array, size_t size, int value)
{
	size_t i;
	/* check if the array or its size is NULL */
	if (array == NULL)
		return (-1);
	/* iterate over all the elements in the array */
	for (i = 0; i < size; i++)
	{
		printf("Value checked array[%lu] = [%d]\n", i, array[i]);
		if (array[i] == value)
			return (i);
	}
	return (-1);
}
