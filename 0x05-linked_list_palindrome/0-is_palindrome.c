#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * with_recursion - Auxiliar recursion for is_palindrome
 * @prev: Pointer to head
 * @next: Head of singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int with_recursion(listint_t **prev, listint_t *next)
{
	int ret;

	if (next == NULL)
		return (1);

	ret = with_recursion(prev, next->next);
	if (ret == 0)
		return (0);

	ret = (next->n == (*prev)->n);

	*prev = (*prev)->next;

	return (ret);
}

/**
 * is_palindrome - Function that checks if a singly linked list is a palindrome
 * * An empty list is considered a palindrome
 * @head: Pointer to singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	if (!head)
		return (0);
	return (with_recursion(head, *head));
}