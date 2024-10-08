#include <stdio.h>

int main(){
    
    printf("\nCounting up\n");
    for (int i = 1; i <= 10; i++)
    {
        printf("%d\n", i);
    }
    
    printf("\nCounting down\n");

    for (int i = -1; i >= -10; i--)
    {
        printf("%d\n", i);
    }
    
    int i = 0;
    while (i != 100)
    {
        printf("\n%d\n", i);
        i+=2;
    }
    


    return 0;
}