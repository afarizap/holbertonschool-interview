#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "binary_trees.h"

/**
 * heap_insert - inserts a value into a Max Binary Heap
 * @root: a double pointer to the root node of the Heap
 * @value: the value to store in the node to be inserted
 * Return: pointer to the inserted node, or NULL on failure
 */
heap_t *heap_insert(heap_t **root, int value)
{
	binary_tree_t *my_node = malloc(sizeof(binary_tree_t));

	if (my_node == NULL)
		return (NULL);
	my_node->n = value;
	my_node->left = NULL;
	my_node->right = NULL;
	my_node->parent = root;

	return (my_node);
}