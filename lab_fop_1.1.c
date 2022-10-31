#include "stdio.h"
int main(){
    float a;
    char str[10];
    printf("Введите вещественное число: ");
    scanf ("%f",&a);
    printf("%f\n",a);
    printf("Введите символы: ");
    scanf ("%s",&str);
    printf("%s\n", str);
    return 0;
}