#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "binarySearchTree.h"

int main(void){

    BST_node* t = malloc( sizeof(BST_node) );
    t->word = "";
    t->left_child = NULL;
    t->right_child = NULL;

    insert_BST_node( t, "Hello");
    insert_BST_node( t, "are");
    insert_BST_node( t, "you");
    insert_BST_node( t, "there");

    inorder_traverse(t);
    return 0;
}
