/*
 * Program : every.cpp
 * Author  : Kyle Kloberdanz
 * Date    : Created: 7 Sep 2015
 *
 * Input Arguments: delay (in seconds), command 
 */

#include <iostream>

#include <stdlib.h>
#include <unistd.h>

bool is_valid_wait_time(const char*);

int main( int argc, char* argv[] ){ 
    int i = argc;
    std::string command_string;
    for (i = 2; i < argc; i++) {
        std::string cpp_string = argv[i];
        command_string += cpp_string + ' ';
    }

    const char* c_command_string = command_string.c_str(); 

    if (!is_valid_wait_time(argv[1])) {
        std::cout << "every: '" << argv[1] 
            << "' is and invalid wait time" << std::endl;
        std::exit(EXIT_FAILURE);
    }

    const unsigned int wait_time = atoi(argv[1]);
    while (true) { 
        system(c_command_string);
        sleep(wait_time);
    }
    return 0;
}

bool is_valid_wait_time(const char* str) {
    for (int i = 0; str[i] != '\0'; ++i) {
        if ((str[i] < '0') || (str[i] > '9')) {
            return false;
        }
    }
    return true;
}
