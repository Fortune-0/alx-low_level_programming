#include <stdio.h>

int main()
{
    char list[30];
    
    for(int i = 0; i < list.size(); i++)
{
   printf("%s \n", list[i]);
}

//2. Use a for-each loop: 

for(const auto& value : list)
{
   printf("%s \n", value);
}
}