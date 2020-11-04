#include <wiringPi.h>
#include<stdio.h>
#include<stdlib.h>

int ledControl(int rgy, int num){

    int i = 0;
    int j = 0;
    i = rgv;
    j = num;

    wiringPiSetup();

    pinMode(i, OUTPUT);

    digitalWrite(i, num);
    
    return 0 ;
}
