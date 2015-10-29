#ifndef BINARYSEARCHTREE_H 
#define BINARYSEARCHTREE_H

typedef struct BST{
    unsigned char* word;
    struct BST* left_child;
    struct BST* right_child;
}BST_node;

/*
 * Before calling, run this: 
 *     BST_node* someNode = malloc( sizeof(BST_node) );
 * 
 * Initializes a node after memory has been allocated
 */
void bst_initialize( BST_node* );

/*
 * Creates a new node in the Binary Search Tree, and inserts the word
 * If the word is already in the tree, then no actions are taken
 */
void bst_insert_node(BST_node* thisNode, unsigned char* w);

/*
 * Traverses the tree, and prints each word in the tree in alphabetical order
 */
void bst_inorder_traverse(BST_node* thisNode);

/*
 * Searches the tree, and returns true if the word is found, false otherwise
 */
int bst_search( BST_node* thisNode, unsigned char* w );

/*
 * IMPLEMENTATION:
 */
void bst_initialize( BST_node* thisNode ){
    thisNode->word = "";
    thisNode->left_child = NULL;
    thisNode->right_child = NULL;
}

void bst_insert_node(BST_node* thisNode, unsigned char* w){
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
            bst_insert_node( thisNode->right_child, w );
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
            bst_insert_node( thisNode->left_child, w );
        }
    }
}

void bst_inorder_traverse(BST_node* thisNode){
    if( thisNode != NULL ){
        bst_inorder_traverse(thisNode->left_child);
        puts(thisNode->word);
        bst_inorder_traverse(thisNode->right_child);
    }
}

int bst_search( BST_node* thisNode, unsigned char* w ){
    int comparison = strcmp(thisNode->word, w);
    /*
     * comparison is:  < 0 if thisNode->word is less than w
     *                 > 0 if thisNode->word is greater than w
     *                == 0 if thisNode->word is equal to w
     */

    /* go right */
    if( comparison < 0) {
        if( thisNode->right_child == NULL ){
            return 0;
        /* if strcmp returns zero, then the word has been found */
        } else if( !strcmp(thisNode->right_child->word, w) ) {
            return 1;
        /* else, word not found, go right */
        } else {
            bst_search( thisNode->right_child, w );
        }
    /* go left */
    } else if ( comparison > 0 ) {

        if( thisNode->left_child == NULL ){
            return 0;
        /* if strcmp returns zero, then the word has been found */
        } else if( !strcmp(thisNode->left_child->word, w) ){
            return 1;
        /* else, word not found, go left */
        } else {
            bst_search( thisNode->left_child, w);
        }
    /* word found */
    } else if ( comparison == 0 ){
        return 1;
    }
}

void bst_destroy(BST_node* thisNode){
    if( thisNode != NULL ){
        bst_destroy( thisNode->left_child );
        bst_destroy( thisNode->right_child );
        free( thisNode );
    }
}
#endif
