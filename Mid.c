// Online C compiler to run C program online
#include <stdio.h>

int main() {
    // Write C code here
    int nilai;
    printf("masukan nilai anda: ");
    scanf("%d",&nilai);
    if(nilai>=85 && nilai<=100){
        printf("A");
    }
    else if(nilai>=75 && nilai<=84){
        printf("B");
    }
    else if(nilai>60 && nilai<=74){
        printf("C");
    }
    else{
        printf("D");
    }
}