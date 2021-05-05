#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* insert_node - inserts a number into a sorted sll
* @head: pointer to head of list
* @number: number to insert on list
* Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = number;
    new->next = NULL;

    if (!(*head))
        *head = new;
    else if ((*head)->n > new->n)
        new->next = *head;
    else
    {
        while (current->next != NULL)
        {
            if (current->next->n > new->n)
            {
                new->next = current->next;
                current->next = new;
                return (new);
            }
            current = current->next;
        }           
    }

    return (new);
}