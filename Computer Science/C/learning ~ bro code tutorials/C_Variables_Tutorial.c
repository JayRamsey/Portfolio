#include <stdio.h>
#include <stdbool.h>

int main(){

    int x; //declaration
    x = 16777216; //initialisation

    //combined steps
    int y = 16777216;
    int age = 17;

    float floatingPointNumber = 1.234;
    char grade = 'A'; //use single quotes, can only store one char
    char highGrade[] = "A*";
    char name[] = "Hello World";

    //printing variables
    /*
    for formatting:
    d "decimal" is for integers ~ use u for "unsigned" integers
    s "string" is for char arrays
    c "character" is for characters
    f "floating point" is for floating points
    lf "long float" is for doubles
    */
    printf("You are %d years old\n", age);
    printf("Hello %s\n", name);
    printf("Your average grade is %c\n", grade);
    

    //other data types
    double myDouble = 1.128172389127321; //doubles can store more precise decimals.
    long long int myLong = 8916100448256U; //can use long, long int or long long int...
    // ^^^ long int is already what an int by itself is
    bool e = true;
    //shorts store 2 bytes ~ [-32,768, +32767] (%d)
    short int shortInt = 32767;
    //unsigned makes range move to > 0. now up to 65535
    unsigned short int shortUnsignedInt = 65535;


    //can use character format specifier when printing ints
    //this converts it to character in ascii table.
    printf("Conversion of %d to %c", 111, 111);



    return 0;
}