/*
 * Programmer: Kyle Kloberdanz
 * 
 * This program is an exercise in computing roots without
 * including math.h
 */

#include <stdio.h>

double absoluteValue( double input ){
    if( input < 0 ){
        return input * -1;
    } else {
        return input;
    }
}

double exponent( double base, int power ){
    int i;
    double ans = 1;
    for( i = 0; i < power; i++ ){
        ans = ans * base;
    }
    return ans;
}

double root(double n, int r){
    double e = 0.0000000001;
    double ans = n;
    double guess = n / 5;
    int timeOut = 1000; // used so that the function will not loop indefinitely
    int i = 0;

    while( (absoluteValue(guess - ans) > e) && (i <= timeOut) ){
        guess = ans;
        ans = ( ( (r-1) * guess ) + (n/( exponent(guess, r-1) ) ) ) / r;
        printf("ans = %f\n", ans);
        i++;
    }

    if( i >= timeOut ){
        puts( "ERROR: function has timed out\nThe result will not be accurate!" );
    }

    printf("Number of iterations: %d\n", i);
    return ans;
}

int main(void){
    printf("abs(-3.5) = %f\n", absoluteValue(-3.5) );    
    printf("exponent(3, 4) = %f\n", exponent(3, 4) );
    printf("root(10, 3) = %f\n", root(10,3) );

    return 0;
}
