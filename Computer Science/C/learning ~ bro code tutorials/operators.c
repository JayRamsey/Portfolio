#include <stdio.h>

int main(){

    int x = 5;
    int y = 2;

    //dividing by int y gives int answer - need to add (float) before
    float z = x / (float) y;
    printf("%f", z);


    /*
    % ~ modulus
    ++ ~ increment
    -- ~ decrement

    also:
    += works just like other languages like Python

    x++ == x += 1

    */


    return 0;
}