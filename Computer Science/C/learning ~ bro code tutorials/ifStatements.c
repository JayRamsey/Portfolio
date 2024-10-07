#include <stdio.h>

int main(){
    int age;
    printf("\nEnter your age: ");
    scanf("%d", &age);

    if (age >= 18)
    {
        printf("You are atleast 18!");
    }
    //else if, else, etc...
    

    return 0;
}