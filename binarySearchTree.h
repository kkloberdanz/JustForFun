#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "binarySearchTree.h"

int main(void){

    BST_node* t = malloc( sizeof(BST_node) );
    //t->word = "";
    //t->left_child = NULL;
    //t->right_child = NULL;

    bst_initialize( t );

    bst_insert_node( t, "Hello");
    bst_insert_node( t, "how");
    bst_insert_node( t, "are");
    bst_insert_node( t, "you");
    bst_insert_node( t, "this"); 
    bst_insert_node( t, "is"); 
    bst_insert_node( t, "a"); 
    bst_insert_node( t, "binary"); 
    bst_insert_node( t, "search"); 
    bst_insert_node( t, "tree"); 
    bst_insert_node( t, "written"); 
    bst_insert_node( t, "in"); 
    bst_insert_node( t, "C"); 
    bst_insert_node( t, "Enjoy!"); 

    char* word = "you";
    int result = bst_search( t, word );

    printf("result = %d\n", result);

    if(result){
        printf("%s, found\n", word);
    } else {
        printf("%s, not found\n", word);
    }

    bst_inorder_traverse(t);
    bst_destroy( t );
    return 0;
}
