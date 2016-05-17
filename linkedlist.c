/*
 * Programmer: Kyle Kloberdanz
 * Date Created: 17 May 2016
 *
 * Description: An apptempt at making a somewhat generic doubly linked 
 *              list. Tested with valgrind, no memory leaks possible
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef union data_type {
    int    i;
    char   c;
    float  f;
} data_t;

typedef struct node {
    data_t data;
    struct node* next;
    struct node* prev;
} node_t;

void add_to_list(node_t* head, int data) {
    if (head->next == NULL) {
        head->next = malloc(sizeof(struct node)); 
        head->next->data.i = data;
        head->next->next = NULL;
        head->next->prev = head;
        return;
    } else {
        add_to_list(head->next, data);
    } 
}

void print_list_i(node_t* head) {
    if (head->next != NULL) {
        printf("%d, ", head->data.i);
        print_list_i(head->next);
    } else {
        printf("%d\n", head->data.i);
        return;
    }
}

void print_list_c(node_t* head) {
    if (head->next != NULL) {
        printf("%c, ", head->data.c);
        print_list_c(head->next);
    } else {
        printf("%c\n", head->data.c);
        return;
    }
}

void print_reverse_list(node_t* head) {
    node_t* curr = head;
    while (curr->next != NULL) {
        curr = curr->next;
    }
    
    while (curr->prev != NULL) {
        printf("%d, ", curr->data.i);
        curr = curr->prev;
    }
    printf("%d\n", curr->data.i);
}

void destroy_list(node_t* head) { 
    node_t* next = NULL;
    node_t* curr = NULL;
    for (curr = head; curr; curr = next) {
        next = curr->next;
        free(curr);
    }
}

void initialize_list(node_t* head, int initial_value) {
    head->data.i = initial_value;
    head->next = NULL;
    head->prev = NULL;
}

int main() {

    /* Used as an example */
    node_t* l;
    l = malloc(sizeof(struct node));
    initialize_list(l, 'a');

    int i;
    for (i = 'b'; i < 'z'+1; i++) {
        add_to_list(l, i);
    }

    print_list_i(l);
    puts("");
    print_reverse_list(l);
    puts("");

    print_list_c(l);
    puts("");
    destroy_list(l);
    return 0;
}
