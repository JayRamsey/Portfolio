#include <limits.h>


int findMax(int, int);


int main(){

    
}


int findMax(int x, int y){
    if (x==y){
        return INT_MIN;
    }
    return (x > y) ? x : y;
}