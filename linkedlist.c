#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct node {
    int data;
    struct node* next;
    struct node* prev;
} node_t;

void add_to_list(node_t* head, int data) {
    if (head->next == NULL) {
        head->next = malloc(sizeof(struct node)); 
        head->next->data = data;
        head->next->next = NULL;
        head->next->prev = head;
        return;
    } else {
        add_to_list(head->next, data);
    } 
}

void print_list(node_t* head) {
    if (head->next != NULL) {
        printf("%d, ", head->data);
        print_list(head->next);
    } else {
        printf("%d\n", head->data);
        return;
    }
}

void print_reverse_list(node_t* head) {
    node_t* curr = head;
    while (curr->next != NULL) {
        curr = curr->next;
    }
    
    while (curr->prev != NULL) {
        printf("%d, ", curr->data);
        curr = curr->prev;
    }
    printf("%d\n", curr->data);
}

void destroy_list(node_t* head) { 
    node_t* next = NULL;
    node_t* curr = NULL;
    for (curr = head; curr; curr = next) {
        next = curr->next;
        free(curr);
    }
}

int main() {

    /* Used as an example */
    node_t* l;
    l = malloc(sizeof(struct node));
    l->data = -1;
    l->next = NULL;
    l->prev = NULL;

    int i;
    for (i = 0; i < 10; i++) {
        add_to_list(l, i);
    }

    print_list(l);
    print_reverse_list(l);
    destroy_list(l);
    return 0;
}
