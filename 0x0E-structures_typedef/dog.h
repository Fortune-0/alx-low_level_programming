#ifndef _DOG_H_
#define _DOG_H_

#include <stdio.h>
#include <stdlib.h>

/*
 * dog_t - Typedef for struct dog
 */
typedef struct dog dog_t;

/*
 * struct dog - store the name iof dog
 * @name: dog name
 * @age: dog age
 * @owner: name of dog owner
 *
 * Desc: struct called "dog" that stores
 * it's details, name, age & name of owner
 */
struct dog

{
	char *name;
	float age;
	char *owner;
};

void init_dog(struct dog *d, char *name, float age, char *owner);
void print_dog(struct dog *d);
dog_t *new_dog(char *name, float age, char *owner);
void free_dog(dog_t *d);

#endif
