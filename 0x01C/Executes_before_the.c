/** executes before the main function prints a message before the main function 
 */ 
#include <stdio.h>

// Function to print the message
void printMessage() {
    printf("You're beat! and yet, you must allow,\n");
    printf("I bore my house upon my back!\n");
}

int main() {
    // Call the printMessage function before the main function logic
    printMessage();
    
    // Rest of the main function logic goes here
    printf("This is the main ");
    printf("function.\n");
    
    return 0;
}
