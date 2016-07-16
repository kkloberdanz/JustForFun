#include <stdio.h>

#define SIZE 6 

typedef enum {
    TRUE  = 1,
    FALSE = 0
} bool_t;

void bubblesort(int a[], int size);
void print_array(int a[], int size); 

void bubblesort(int a[], int size) { 
    bool_t sorted = FALSE;
    int i;
    int tmp;
    while (!sorted) {
        sorted = TRUE; 
        for (i = 0; i < size-1; i++) {
            if (a[i] > a[i+1]) {
                tmp = a[i];
                a[i] = a[i+1];
                a[i+1] = tmp;
                sorted = FALSE;
            }
        }
    }
}

void print_array(int a[], int size) {
    int i;
    for (i = 0; i < size; i++) {
        printf("%d, ", a[i]);
    }
    puts("");
} 

int main(void) {
    int a[SIZE] = {10, 6, 8, 6, 5, 4};
    printf("Unsorted: ");
    print_array(a, SIZE);
    bubblesort(a, SIZE); 
    printf("Sorted:   ");
    print_array(a, SIZE);
    return 0;
}
