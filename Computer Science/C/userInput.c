#include <stdio.h>
#include <string.h>

int main(){

    //scanf only gets up to the next whitespace

    char name[25];
    int age;

    printf("\nWhat's your name? ");
    // scanf("%s", &name);
    fgets(name, 25, stdin);
    name[strlen(name)-1] = '\0';

    printf("How old are you: ");
    scanf("%d", &age);

    printf("Hello %s, how are you?\n", name);
    printf("You are %d years old", age);

    return 0;
}