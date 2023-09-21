#include <stdio.h>
#include <time.h>

// Function to switch power from one generator to another
void switchPower(int fromGenerator, int toGenerator) 
{
    printf("Switching power from Generator %d to Generator %d\n", fromGenerator, toGenerator);
    // Implement the logic to switch power here
}

int main() {

    //int time = 4;

    int currentGenerator = 1; // Initial generator

    printf("Current Generator: Generator %d\n", currentGenerator);

    //Printf("Time to switch power\n");
    // Simulating power switch requests
    switchPower(currentGenerator, 2); // Switching power from Generator 1 to Generator 2
    currentGenerator = 2;

    printf("Current Generator: Generator %d\n", currentGenerator);

    switchPower(currentGenerator, 3); // Switching power from Generator 2 to Generator 3
    currentGenerator = 3;

    printf("Current Generator: Generator %d\n", currentGenerator);

    switchPower(currentGenerator, 1); // Switching power from Generator 3 to Generator 1
    currentGenerator = 1;

    printf("Current Generator: Generator %d\n", currentGenerator);

    return 0;
}
