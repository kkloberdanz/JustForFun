/*
 * Program: every.c
 * Author: Kyle Kloberdanz
 * Date Created: 7 Sep 2015
 *
 * Input Arguments: delay (in seconds), command (must be in quotes)
 */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>

int main( int argc, char* argv[] ){
    const numArgs = 3;
    while( true ){
        if( argc == numArgs ){
            /* atoi takes a string a returns an int */
            system(argv[2]);
            sleep( atoi(argv[1]) );
        } else if( argc < numArgs ){
            puts( "Error in program: every, not enough input arguments" );
            return 1;
        } else if( argc > numArgs ){
            puts( "Error in program: every, too many input arguments" );
            return 1;
        }
    }
    return 0;
}
