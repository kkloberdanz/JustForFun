#ifndef BINARYSEARCHTREE_H 
#define BINARYSEARCHTREE_H

typedef struct BST{
    unsigned char* word;
    struct BST* left_child;
    struct BST* right_child;
}BST_node;

/*
 * Creates a new node in the Binary Search Tree, and inserts the word
 * If the word is already in the tree, then no actions are taken
 */
void insert_BST_node(BST_node* thisNode, unsigned char* w);

/*
 * Traverses the tree, and prints each word in the tree in alphabetical order
 */
void inorder_traverse(BST_node* thisNode);


/*
 * IMPLEMENTATION:
 */
void insert_BST_node(BST_node* thisNode, unsigned char* w){
    int comparison = strcmp(thisNode->word, w);
    /*
     * comparison is:  < 0 if thisNode->word is less than w
     *                 > 0 if thisNode->word is greater than w
     *                == 0 if thisNode->word is equal to w
     */

    if( comparison < 0 ){
        /* go right */
        if( thisNode->right_child == NULL ){
            /* create new node with word = w */
            thisNode->right_child = malloc( sizeof(BST_node) );
            thisNode->right_child->word = w;
            thisNode->right_child->right_child = NULL;
            thisNode->right_child->left_child = NULL;

        } else {
            /* recursive call, go right */
            insert_BST_node( thisNode->right_child, w );
        }
    } else if( comparison > 0 ){
        /* go left */
        if( thisNode->left_child == NULL ){
            /* create new node with word = w */
            thisNode->left_child = malloc( sizeof(BST_node) );
            thisNode->left_child->word = w;
            thisNode->left_child->right_child = NULL;
            thisNode->left_child->left_child = NULL;
        } else {
            /* recursive call, go left */
            insert_BST_node( thisNode->left_child, w );
        }
    }
}

void inorder_traverse(BST_node* thisNode){
    if( thisNode != NULL ){
        inorder_traverse(thisNode->left_child);
        puts(thisNode->word);
        inorder_traverse(thisNode->right_child);
    }
}
#endif
