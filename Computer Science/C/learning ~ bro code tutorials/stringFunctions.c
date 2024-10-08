#include <stdio.h>
#include <string.h>

int main(){

    char myString[] = "Hello";
    char secondString[] = " World";

    strcat(myString, secondString);

    //strcatn(string1, string2, n) appends n chars of string2 to the end of string1
    //strset(string, char) sets all chars of string to char
    //strrev(string) reverses a string
    
    printf(myString);
    printf("\nThis string is %d characters long.", strlen(myString));

    


}